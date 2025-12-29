import * as vscode from 'vscode';
import { MarunochiAPIClient, ChatMessage } from './api';

/**
 * Inline Chat Controller - Cursor/Copilot style inline editing
 * Activated with Cmd+I, shows input box inline, applies edits with preview
 */
export class InlineChatController {
    private decoration: vscode.TextEditorDecorationType;
    private previewDecoration: vscode.TextEditorDecorationType;
    private isActive = false;

    constructor(private apiClient: MarunochiAPIClient) {
        // Decoration for highlighting the code being edited
        this.decoration = vscode.window.createTextEditorDecorationType({
            backgroundColor: 'rgba(88, 166, 255, 0.1)',
            border: '1px solid rgba(88, 166, 255, 0.4)',
            borderRadius: '3px',
        });

        // Decoration for showing proposed changes (green for additions)
        this.previewDecoration = vscode.window.createTextEditorDecorationType({
            backgroundColor: 'rgba(46, 160, 67, 0.15)',
            border: '1px dashed rgba(46, 160, 67, 0.5)',
            after: {
                contentText: ' (Tab to accept, Esc to cancel)',
                color: 'rgba(150, 150, 150, 0.8)',
                fontStyle: 'italic',
            },
        });
    }

    /**
     * Start inline chat at current cursor position
     */
    async startInlineChat(): Promise<void> {
        const editor = vscode.window.activeTextEditor;
        if (!editor || this.isActive) {
            return;
        }

        this.isActive = true;
        const selection = editor.selection;
        const hasSelection = !selection.isEmpty;

        // Highlight the selected region or current line
        const targetRange = hasSelection
            ? selection
            : editor.document.lineAt(selection.active.line).range;

        editor.setDecorations(this.decoration, [targetRange]);

        try {
            // Show input box for the prompt
            const prompt = await vscode.window.showInputBox({
                prompt: hasSelection ? 'Edit selection with AI' : 'Generate code with AI',
                placeHolder: hasSelection
                    ? 'e.g., "refactor to use async/await", "add error handling"'
                    : 'e.g., "add a function to validate email", "create a class for..."',
                ignoreFocusOut: false,
            });

            if (!prompt) {
                editor.setDecorations(this.decoration, []);
                this.isActive = false;
                return;
            }

            // Show progress
            await vscode.window.withProgress(
                {
                    location: vscode.ProgressLocation.Notification,
                    title: 'MarunochiAI',
                    cancellable: true,
                },
                async (progress, token) => {
                    progress.report({ message: 'Generating edit...' });

                    const result = await this.generateEdit(
                        editor,
                        targetRange,
                        prompt,
                        hasSelection,
                        token
                    );

                    if (token.isCancellationRequested || !result) {
                        editor.setDecorations(this.decoration, []);
                        return;
                    }

                    // Show preview and wait for confirmation
                    await this.showPreviewAndConfirm(editor, targetRange, result);
                }
            );
        } catch (error) {
            console.error('MarunochiAI: Inline chat error:', error);
            vscode.window.showErrorMessage(`MarunochiAI: ${error}`);
        } finally {
            editor.setDecorations(this.decoration, []);
            this.isActive = false;
        }
    }

    /**
     * Generate edit using AI
     */
    private async generateEdit(
        editor: vscode.TextEditor,
        range: vscode.Range,
        prompt: string,
        isEdit: boolean,
        token: vscode.CancellationToken
    ): Promise<string | null> {
        const document = editor.document;
        const selectedText = document.getText(range);

        // Get surrounding context (50 lines before, 20 after)
        const contextStartLine = Math.max(0, range.start.line - 50);
        const contextEndLine = Math.min(document.lineCount - 1, range.end.line + 20);

        const beforeContext = document.getText(
            new vscode.Range(contextStartLine, 0, range.start.line, range.start.character)
        );
        const afterContext = document.getText(
            new vscode.Range(range.end.line, range.end.character, contextEndLine, document.lineAt(contextEndLine).text.length)
        );

        const messages: ChatMessage[] = isEdit
            ? [
                  {
                      role: 'system',
                      content: `You are an expert code editor. You will modify the provided code according to the user's instructions.
Language: ${document.languageId}
File: ${document.fileName}

Rules:
- Output ONLY the modified code, no explanations
- No markdown code blocks or backticks
- Preserve the indentation style of the original
- Keep changes minimal and focused on the request
- If the request is unclear, make reasonable assumptions`,
                  },
                  {
                      role: 'user',
                      content: `Context before:
\`\`\`
${beforeContext.slice(-500)}
\`\`\`

Code to edit:
\`\`\`
${selectedText}
\`\`\`

Context after:
\`\`\`
${afterContext.slice(0, 300)}
\`\`\`

Instruction: ${prompt}

Output only the modified code:`,
                  },
              ]
            : [
                  {
                      role: 'system',
                      content: `You are an expert code generator. Generate code according to the user's instructions.
Language: ${document.languageId}
File: ${document.fileName}

Rules:
- Output ONLY the code, no explanations
- No markdown code blocks or backticks
- Match the indentation style of the surrounding code
- Generate clean, idiomatic code`,
                  },
                  {
                      role: 'user',
                      content: `Context:
\`\`\`
${beforeContext.slice(-500)}
[INSERT CODE HERE]
${afterContext.slice(0, 300)}
\`\`\`

Generate code for: ${prompt}

Output only the code:`,
                  },
              ];

        try {
            const response = await this.apiClient.chatCompletion(messages);

            if (token.isCancellationRequested) {
                return null;
            }

            let result = response.choices[0].message.content;

            // Clean up the result
            result = result
                .replace(/^```[\w]*\n?/gm, '')
                .replace(/\n?```$/gm, '')
                .trim();

            return result;
        } catch (error) {
            console.error('MarunochiAI: Edit generation error:', error);
            throw new Error('Failed to generate edit');
        }
    }

    /**
     * Show preview of changes and wait for confirmation
     */
    private async showPreviewAndConfirm(
        editor: vscode.TextEditor,
        range: vscode.Range,
        newText: string
    ): Promise<void> {
        const document = editor.document;
        const originalText = document.getText(range);

        // Create a temporary preview using decorations
        // For now, we'll use a quick pick to confirm

        const diff = this.createSimpleDiff(originalText, newText);

        const choice = await vscode.window.showQuickPick(
            [
                {
                    label: '$(check) Accept',
                    description: 'Apply the changes',
                    action: 'accept',
                },
                {
                    label: '$(eye) Preview Diff',
                    description: 'View changes in diff editor',
                    action: 'diff',
                },
                {
                    label: '$(x) Cancel',
                    description: 'Discard changes',
                    action: 'cancel',
                },
            ],
            {
                placeHolder: `Changes: ${diff.added} lines added, ${diff.removed} lines removed`,
            }
        );

        if (!choice || choice.action === 'cancel') {
            return;
        }

        if (choice.action === 'diff') {
            // Show diff in a new editor
            await this.showDiffEditor(document.uri, range, originalText, newText);

            // Ask again after viewing diff
            const accept = await vscode.window.showQuickPick(
                [
                    { label: '$(check) Accept Changes', action: 'accept' },
                    { label: '$(x) Cancel', action: 'cancel' },
                ],
                { placeHolder: 'Apply these changes?' }
            );

            if (accept?.action !== 'accept') {
                return;
            }
        }

        // Apply the changes
        await editor.edit((editBuilder) => {
            editBuilder.replace(range, newText);
        });

        vscode.window.showInformationMessage('MarunochiAI: Changes applied');
    }

    /**
     * Show changes in a diff editor
     */
    private async showDiffEditor(
        uri: vscode.Uri,
        range: vscode.Range,
        original: string,
        modified: string
    ): Promise<void> {
        // Create virtual documents for diff
        const originalUri = vscode.Uri.parse(`marunochiAI-original:${uri.path}`);
        const modifiedUri = vscode.Uri.parse(`marunochiAI-modified:${uri.path}`);

        // Register content providers temporarily
        const originalProvider = new (class implements vscode.TextDocumentContentProvider {
            provideTextDocumentContent(): string {
                return original;
            }
        })();

        const modifiedProvider = new (class implements vscode.TextDocumentContentProvider {
            provideTextDocumentContent(): string {
                return modified;
            }
        })();

        const disposables = [
            vscode.workspace.registerTextDocumentContentProvider('marunochiAI-original', originalProvider),
            vscode.workspace.registerTextDocumentContentProvider('marunochiAI-modified', modifiedProvider),
        ];

        try {
            await vscode.commands.executeCommand(
                'vscode.diff',
                originalUri,
                modifiedUri,
                'MarunochiAI: Proposed Changes'
            );
        } finally {
            // Cleanup after a delay to allow the diff to open
            setTimeout(() => {
                disposables.forEach((d) => d.dispose());
            }, 5000);
        }
    }

    /**
     * Create a simple diff summary
     */
    private createSimpleDiff(original: string, modified: string): { added: number; removed: number } {
        const originalLines = original.split('\n');
        const modifiedLines = modified.split('\n');

        return {
            added: Math.max(0, modifiedLines.length - originalLines.length),
            removed: Math.max(0, originalLines.length - modifiedLines.length),
        };
    }

    dispose(): void {
        this.decoration.dispose();
        this.previewDecoration.dispose();
    }
}

/**
 * Quick Edit command - Apply simple transformations without confirmation
 */
export async function quickEdit(
    apiClient: MarunochiAPIClient,
    transformation: 'explain' | 'refactor' | 'fix' | 'document' | 'test'
): Promise<void> {
    const editor = vscode.window.activeTextEditor;
    if (!editor) {
        return;
    }

    const selection = editor.selection;
    if (selection.isEmpty) {
        vscode.window.showWarningMessage('Please select code first');
        return;
    }

    const selectedText = editor.document.getText(selection);
    const language = editor.document.languageId;

    const prompts: Record<string, string> = {
        explain: `Explain this ${language} code concisely:\n\n${selectedText}`,
        refactor: `Refactor this ${language} code to be more clean, readable, and efficient. Output only the refactored code:\n\n${selectedText}`,
        fix: `Fix any bugs or issues in this ${language} code. Output only the fixed code:\n\n${selectedText}`,
        document: `Add documentation/comments to this ${language} code. Output only the documented code:\n\n${selectedText}`,
        test: `Generate unit tests for this ${language} code:\n\n${selectedText}`,
    };

    const isReplace = ['refactor', 'fix', 'document'].includes(transformation);

    await vscode.window.withProgress(
        {
            location: vscode.ProgressLocation.Notification,
            title: `MarunochiAI: ${transformation}...`,
            cancellable: true,
        },
        async (progress, token) => {
            try {
                const response = await apiClient.chatCompletion([
                    { role: 'user', content: prompts[transformation] },
                ]);

                if (token.isCancellationRequested) {
                    return;
                }

                let result = response.choices[0].message.content
                    .replace(/^```[\w]*\n?/gm, '')
                    .replace(/\n?```$/gm, '')
                    .trim();

                if (isReplace) {
                    // Replace selection with result
                    await editor.edit((edit) => {
                        edit.replace(selection, result);
                    });
                } else {
                    // Show in panel (for explain, test)
                    const panel = vscode.window.createWebviewPanel(
                        'marunochiAI.result',
                        `MarunochiAI: ${transformation}`,
                        vscode.ViewColumn.Beside,
                        {}
                    );

                    panel.webview.html = `
                        <!DOCTYPE html>
                        <html>
                        <head>
                            <style>
                                body { font-family: var(--vscode-font-family); padding: 20px; }
                                pre { background: var(--vscode-textCodeBlock-background); padding: 15px; overflow-x: auto; }
                                code { font-family: var(--vscode-editor-font-family); }
                            </style>
                        </head>
                        <body>
                            <h2>${transformation.charAt(0).toUpperCase() + transformation.slice(1)}</h2>
                            <pre><code>${escapeHtml(result)}</code></pre>
                        </body>
                        </html>
                    `;
                }
            } catch (error) {
                vscode.window.showErrorMessage(`MarunochiAI: ${error}`);
            }
        }
    );
}

function escapeHtml(text: string): string {
    return text
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
}
