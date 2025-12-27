import * as vscode from 'vscode';
import { MarunochiAPIClient } from './api';
import { SearchViewProvider } from './searchView';
import { ChatViewProvider } from './chatView';
import { MarunochiCompletionProvider } from './completionProvider';
import { MarunochiCodeActionProvider } from './codeActionProvider';

let apiClient: MarunochiAPIClient;
let searchViewProvider: SearchViewProvider;
let chatViewProvider: ChatViewProvider;

export function activate(context: vscode.ExtensionContext) {
    console.log('MarunochiAI extension is now active!');

    // Initialize API client
    const config = vscode.workspace.getConfiguration('marunochiAI');
    apiClient = new MarunochiAPIClient(
        config.get('apiUrl', 'http://localhost:8765'),
        config.get('apiKey', '')
    );

    // Register views
    searchViewProvider = new SearchViewProvider(apiClient);
    chatViewProvider = new ChatViewProvider(apiClient);

    context.subscriptions.push(
        vscode.window.registerTreeDataProvider('marunochiAI.searchView', searchViewProvider),
        vscode.window.registerWebviewViewProvider('marunochiAI.chatView', chatViewProvider)
    );

    // Register completion provider
    if (config.get('enableCompletion', true)) {
        const completionProvider = new MarunochiCompletionProvider(apiClient);
        context.subscriptions.push(
            vscode.languages.registerCompletionItemProvider(
                { scheme: 'file' },
                completionProvider,
                '.', ':', '(', '[', '{', ' '
            )
        );
    }

    // Register code action provider
    const codeActionProvider = new MarunochiCodeActionProvider(apiClient);
    context.subscriptions.push(
        vscode.languages.registerCodeActionsProvider(
            { scheme: 'file' },
            codeActionProvider
        )
    );

    // Register commands
    context.subscriptions.push(
        vscode.commands.registerCommand('marunochiAI.indexWorkspace', indexWorkspace),
        vscode.commands.registerCommand('marunochiAI.searchCode', searchCode),
        vscode.commands.registerCommand('marunochiAI.openChat', openChat),
        vscode.commands.registerCommand('marunochiAI.explainCode', explainCode),
        vscode.commands.registerCommand('marunochiAI.refactorCode', refactorCode),
        vscode.commands.registerCommand('marunochiAI.debugCode', debugCode),
        vscode.commands.registerCommand('marunochiAI.generateTests', generateTests),
        vscode.commands.registerCommand('marunochiAI.showStats', showStats)
    );

    // Auto-index workspace on startup
    if (config.get('autoIndex', true)) {
        setTimeout(() => indexWorkspace(true), 2000);
    }

    vscode.window.showInformationMessage('MarunochiAI is ready!');
}

async function indexWorkspace(silent: boolean = false) {
    const workspaceFolder = vscode.workspace.workspaceFolders?.[0];
    if (!workspaceFolder) {
        vscode.window.showErrorMessage('No workspace folder open');
        return;
    }

    const path = workspaceFolder.uri.fsPath;

    if (!silent) {
        vscode.window.showInformationMessage(`Indexing workspace: ${path}`);
    }

    try {
        const result = await apiClient.indexCodebase(path, true);

        const message = `✓ Indexed ${result.total_files} files, ${result.total_chunks} chunks in ${result.duration_ms}ms`;
        if (!silent) {
            vscode.window.showInformationMessage(message);
        }
    } catch (error) {
        vscode.window.showErrorMessage(`Failed to index: ${error}`);
    }
}

async function searchCode() {
    const query = await vscode.window.showInputBox({
        prompt: 'Search codebase semantically',
        placeHolder: 'e.g., authentication function',
    });

    if (!query) {
        return;
    }

    try {
        const results = await apiClient.searchCodebase(query, 20);

        if (results.length === 0) {
            vscode.window.showInformationMessage('No results found');
            return;
        }

        // Update search view
        searchViewProvider.setResults(results);

        // Show quick pick
        const items = results.map(r => ({
            label: `$(file-code) ${r.metadata.name}`,
            description: `${r.filepath}:${r.metadata.line_range[0]}`,
            detail: `Similarity: ${r.similarity.toFixed(3)} | ${r.metadata.chunk_type}`,
            result: r,
        }));

        const selected = await vscode.window.showQuickPick(items, {
            placeHolder: `Found ${results.length} results`,
        });

        if (selected) {
            const uri = vscode.Uri.file(selected.result.filepath);
            const document = await vscode.workspace.openTextDocument(uri);
            const editor = await vscode.window.showTextDocument(document);

            const line = selected.result.metadata.line_range[0] - 1;
            const position = new vscode.Position(line, 0);
            editor.selection = new vscode.Selection(position, position);
            editor.revealRange(new vscode.Range(position, position));
        }
    } catch (error) {
        vscode.window.showErrorMessage(`Search failed: ${error}`);
    }
}

async function openChat() {
    const message = await vscode.window.showInputBox({
        prompt: 'Chat with MarunochiAI',
        placeHolder: 'Ask anything about coding...',
    });

    if (!message) {
        return;
    }

    chatViewProvider.sendMessage(message);
}

async function explainCode() {
    const editor = vscode.window.activeTextEditor;
    if (!editor) {
        return;
    }

    const selection = editor.selection;
    const code = editor.document.getText(selection);

    if (!code) {
        vscode.window.showWarningMessage('Please select code to explain');
        return;
    }

    const prompt = `Explain this code:\n\n\`\`\`${editor.document.languageId}\n${code}\n\`\`\``;

    const response = await apiClient.chatCompletion([
        { role: 'user', content: prompt },
    ]);

    showMarkdownPreview('Code Explanation', response.choices[0].message.content);
}

async function refactorCode() {
    const editor = vscode.window.activeTextEditor;
    if (!editor) {
        return;
    }

    const selection = editor.selection;
    const code = editor.document.getText(selection);

    if (!code) {
        vscode.window.showWarningMessage('Please select code to refactor');
        return;
    }

    const prompt = `Refactor this code to improve readability and performance:\n\n\`\`\`${editor.document.languageId}\n${code}\n\`\`\``;

    vscode.window.withProgress(
        {
            location: vscode.ProgressLocation.Notification,
            title: 'Refactoring code...',
            cancellable: false,
        },
        async () => {
            const response = await apiClient.chatCompletion([
                { role: 'user', content: prompt },
            ]);

            const suggestion = response.choices[0].message.content;

            // Extract code blocks
            const codeBlockRegex = /```[\w]*\n([\s\S]*?)\n```/g;
            const matches = [...suggestion.matchAll(codeBlockRegex)];

            if (matches.length > 0) {
                const refactoredCode = matches[0][1];

                const action = await vscode.window.showInformationMessage(
                    'Refactoring suggestion ready',
                    'Apply',
                    'Show Preview'
                );

                if (action === 'Apply') {
                    editor.edit(editBuilder => {
                        editBuilder.replace(selection, refactoredCode);
                    });
                } else if (action === 'Show Preview') {
                    showMarkdownPreview('Refactoring Suggestion', suggestion);
                }
            } else {
                showMarkdownPreview('Refactoring Suggestion', suggestion);
            }
        }
    );
}

async function debugCode() {
    const editor = vscode.window.activeTextEditor;
    if (!editor) {
        return;
    }

    const selection = editor.selection;
    const code = editor.document.getText(selection);

    if (!code) {
        vscode.window.showWarningMessage('Please select code to debug');
        return;
    }

    const prompt = `Debug this code and identify potential issues:\n\n\`\`\`${editor.document.languageId}\n${code}\n\`\`\``;

    const response = await apiClient.chatCompletion([
        { role: 'user', content: prompt },
    ]);

    showMarkdownPreview('Debug Analysis', response.choices[0].message.content);
}

async function generateTests() {
    const editor = vscode.window.activeTextEditor;
    if (!editor) {
        return;
    }

    const selection = editor.selection;
    const code = editor.document.getText(selection);

    if (!code) {
        vscode.window.showWarningMessage('Please select code to generate tests for');
        return;
    }

    const prompt = `Generate comprehensive unit tests for this code:\n\n\`\`\`${editor.document.languageId}\n${code}\n\`\`\``;

    vscode.window.withProgress(
        {
            location: vscode.ProgressLocation.Notification,
            title: 'Generating tests...',
            cancellable: false,
        },
        async () => {
            const response = await apiClient.chatCompletion([
                { role: 'user', content: prompt },
            ]);

            showMarkdownPreview('Generated Tests', response.choices[0].message.content);
        }
    );
}

async function showStats() {
    try {
        const stats = await apiClient.getStats();

        const message = `
**MarunochiAI Statistics**

Vector Index:
- Total chunks: ${stats.vector.total_chunks}
- Files indexed: ${stats.vector.total_files || 'N/A'}

Keyword Index:
- Total chunks: ${stats.keyword.total_chunks}

Search:
- RRF k: ${stats.rrf_k}
- Fusion enabled: ${stats.fusion_enabled}
- Watcher running: ${stats.watcher_running}
        `.trim();

        showMarkdownPreview('MarunochiAI Statistics', message);
    } catch (error) {
        vscode.window.showErrorMessage(`Failed to get stats: ${error}`);
    }
}

function showMarkdownPreview(title: string, content: string) {
    const panel = vscode.window.createWebviewPanel(
        'marunochiAI.preview',
        title,
        vscode.ViewColumn.Beside,
        {}
    );

    panel.webview.html = getWebviewContent(title, content);
}

function getWebviewContent(title: string, markdown: string): string {
    // Convert markdown to HTML (basic conversion)
    let html = markdown
        .replace(/```(\w+)?\n([\s\S]*?)```/g, '<pre><code class="language-$1">$2</code></pre>')
        .replace(/`([^`]+)`/g, '<code>$1</code>')
        .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
        .replace(/\*([^*]+)\*/g, '<em>$1</em>')
        .replace(/\n\n/g, '</p><p>')
        .replace(/\n/g, '<br/>');

    html = `<p>${html}</p>`;

    return `
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>${title}</title>
            <style>
                body {
                    font-family: var(--vscode-font-family);
                    padding: 20px;
                    color: var(--vscode-foreground);
                }
                code {
                    background-color: var(--vscode-textCodeBlock-background);
                    padding: 2px 4px;
                    border-radius: 3px;
                }
                pre {
                    background-color: var(--vscode-textCodeBlock-background);
                    padding: 10px;
                    border-radius: 5px;
                    overflow-x: auto;
                }
                pre code {
                    background: none;
                    padding: 0;
                }
            </style>
        </head>
        <body>
            <h1>${title}</h1>
            ${html}
        </body>
        </html>
    `;
}

export function deactivate() {
    console.log('MarunochiAI extension deactivated');
}
