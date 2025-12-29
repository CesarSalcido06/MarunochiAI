import * as vscode from 'vscode';
import { MarunochiAPIClient } from './api';
import { MarunochiInlineCompletionProvider, CompletionStatusBar } from './inlineCompletionProvider';
import { InlineChatController, quickEdit } from './inlineChat';
import { ChatPanelProvider } from './chatPanel';
// Note: searchView.ts kept for backwards compatibility but not used

let apiClient: MarunochiAPIClient;
let statusBar: CompletionStatusBar;
let inlineChatController: InlineChatController;
let chatPanelProvider: ChatPanelProvider;

export function activate(context: vscode.ExtensionContext) {
    console.log('MarunochiAI extension activating...');

    // Initialize API client
    const config = vscode.workspace.getConfiguration('marunochiAI');
    apiClient = new MarunochiAPIClient(
        config.get('apiUrl', 'http://localhost:8765'),
        config.get('apiKey', '')
    );

    // Check server health
    checkServerHealth();

    // Initialize status bar
    statusBar = new CompletionStatusBar();
    context.subscriptions.push(statusBar);

    // Initialize inline chat controller
    inlineChatController = new InlineChatController(apiClient);
    context.subscriptions.push(inlineChatController);

    // Register Chat Panel (Sidebar)
    chatPanelProvider = new ChatPanelProvider(context.extensionUri, apiClient);
    context.subscriptions.push(
        vscode.window.registerWebviewViewProvider(
            ChatPanelProvider.viewType,
            chatPanelProvider,
            {
                webviewOptions: {
                    retainContextWhenHidden: true,
                },
            }
        )
    );

    // Register inline completion provider (ghost text)
    if (config.get('enableCompletion', true)) {
        const inlineProvider = new MarunochiInlineCompletionProvider(apiClient);
        context.subscriptions.push(
            vscode.languages.registerInlineCompletionItemProvider(
                { pattern: '**/*' }, // All files
                inlineProvider
            )
        );
    }

    // Register commands individually with error handling
    const registerCommand = (name: string, handler: (...args: unknown[]) => unknown) => {
        try {
            const disposable = vscode.commands.registerCommand(name, handler);
            context.subscriptions.push(disposable);
            console.log(`MarunochiAI: Registered command ${name}`);
        } catch (error) {
            console.error(`MarunochiAI: Failed to register ${name}:`, error);
        }
    };

    // Toggle completions
    registerCommand('marunochiAI.toggleCompletion', () => {
        statusBar.toggle();
        const enabled = statusBar.isCompletionEnabled();
        vscode.window.showInformationMessage(
            `MarunochiAI: Completions ${enabled ? 'enabled' : 'disabled'}`
        );
    });

    // Open chat panel
    registerCommand('marunochiAI.openChat', async () => {
        await vscode.commands.executeCommand('marunochiAI.chatPanel.focus');
    });

    // Send message to chat
    registerCommand('marunochiAI.askChat', async () => {
        const message = await vscode.window.showInputBox({
            prompt: 'Ask MarunochiAI',
            placeHolder: 'Ask anything about code...',
        });
        if (message) {
            await vscode.commands.executeCommand('marunochiAI.chatPanel.focus');
            chatPanelProvider.sendMessage(message);
        }
    });

    // Explain selection in chat
    registerCommand('marunochiAI.explainInChat', async () => {
        const editor = vscode.window.activeTextEditor;
        if (editor && !editor.selection.isEmpty) {
            await vscode.commands.executeCommand('marunochiAI.chatPanel.focus');
            chatPanelProvider.sendMessage('Explain this code in detail');
        }
    });

    // Inline chat (Cmd+I)
    registerCommand('marunochiAI.inlineChat', () => {
        inlineChatController.startInlineChat();
    });

    // Quick actions
    registerCommand('marunochiAI.explain', () => quickEdit(apiClient, 'explain'));
    registerCommand('marunochiAI.refactor', () => quickEdit(apiClient, 'refactor'));
    registerCommand('marunochiAI.fix', () => quickEdit(apiClient, 'fix'));
    registerCommand('marunochiAI.document', () => quickEdit(apiClient, 'document'));
    registerCommand('marunochiAI.generateTests', () => quickEdit(apiClient, 'test'));

    // Index workspace
    registerCommand('marunochiAI.indexWorkspace', async () => {
        const workspaceFolder = vscode.workspace.workspaceFolders?.[0];
        if (!workspaceFolder) {
            vscode.window.showErrorMessage('No workspace folder open');
            return;
        }

        await vscode.window.withProgress(
            {
                location: vscode.ProgressLocation.Notification,
                title: 'MarunochiAI: Indexing workspace...',
                cancellable: false,
            },
            async () => {
                try {
                    const result = await apiClient.indexCodebase(workspaceFolder.uri.fsPath, true);
                    vscode.window.showInformationMessage(
                        `Indexed ${result.total_files} files (${result.total_chunks} chunks) in ${result.duration_ms}ms`
                    );
                } catch (error) {
                    vscode.window.showErrorMessage(`Index failed: ${error}`);
                }
            }
        );
    });

    // Search code
    registerCommand('marunochiAI.searchCode', async () => {
        const query = await vscode.window.showInputBox({
            prompt: 'Search codebase with AI',
            placeHolder: 'e.g., authentication function, error handler',
        });

        if (!query) return;

        await vscode.window.withProgress(
            {
                location: vscode.ProgressLocation.Notification,
                title: 'Searching...',
                cancellable: false,
            },
            async () => {
                try {
                    const results = await apiClient.searchCodebase(query, 10);

                    if (results.length === 0) {
                        vscode.window.showInformationMessage('No results found');
                        return;
                    }

                    const items = results.map((r) => ({
                        label: `$(file-code) ${r.metadata.name}`,
                        description: `${r.filepath}:${r.metadata.line_range[0]}`,
                        detail: `${(r.similarity * 100).toFixed(0)}% match`,
                        result: r,
                    }));

                    const selected = await vscode.window.showQuickPick(items, {
                        placeHolder: `Found ${results.length} results`,
                    });

                    if (selected) {
                        const uri = vscode.Uri.file(selected.result.filepath);
                        const doc = await vscode.workspace.openTextDocument(uri);
                        const editor = await vscode.window.showTextDocument(doc);

                        const line = selected.result.metadata.line_range[0] - 1;
                        const pos = new vscode.Position(line, 0);
                        editor.selection = new vscode.Selection(pos, pos);
                        editor.revealRange(new vscode.Range(pos, pos), vscode.TextEditorRevealType.InCenter);
                    }
                } catch (error) {
                    vscode.window.showErrorMessage(`Search failed: ${error}`);
                }
            }
        );
    });

    // Trigger inline completion manually
    registerCommand('marunochiAI.triggerCompletion', () => {
        vscode.commands.executeCommand('editor.action.inlineSuggest.trigger');
    });

    console.log('MarunochiAI extension activated');
}

async function checkServerHealth(): Promise<void> {
    try {
        const healthy = await apiClient.healthCheck();
        if (!healthy) {
            vscode.window.showWarningMessage(
                'MarunochiAI: Server not responding. Start it with: marunochithe server'
            );
        }
    } catch {
        vscode.window.showWarningMessage('MarunochiAI: Could not connect to server');
    }
}

export function deactivate() {
    console.log('MarunochiAI extension deactivated');
}
