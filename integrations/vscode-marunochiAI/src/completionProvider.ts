import * as vscode from 'vscode';
import { MarunochiAPIClient } from './api';

export class MarunochiCompletionProvider implements vscode.CompletionItemProvider {
    constructor(private apiClient: MarunochiAPIClient) {}

    async provideCompletionItems(
        document: vscode.TextDocument,
        position: vscode.Position,
        token: vscode.CancellationToken
    ): Promise<vscode.CompletionItem[]> {
        const linePrefix = document.lineAt(position).text.substr(0, position.character);

        // Get context (surrounding code)
        const contextRange = new vscode.Range(
            new vscode.Position(Math.max(0, position.line - 20), 0),
            position
        );
        const context = document.getText(contextRange);

        try {
            const messages = [
                {
                    role: 'system' as const,
                    content: 'You are a code completion assistant. Provide concise, accurate code completions.',
                },
                {
                    role: 'user' as const,
                    content: `Complete this code:\n\n${context}\n\nCursor is after: ${linePrefix}`,
                },
            ];

            const response = await this.apiClient.chatCompletion(messages);
            const completion = response.choices[0].message.content;

            const items: vscode.CompletionItem[] = [];
            const lines = completion.split('\n');

            for (const line of lines) {
                if (line.trim()) {
                    const item = new vscode.CompletionItem(
                        line,
                        vscode.CompletionItemKind.Snippet
                    );
                    item.detail = 'MarunochiAI';
                    item.documentation = 'AI-powered completion';
                    items.push(item);
                }
            }

            return items;
        } catch (error) {
            console.error('Completion failed:', error);
            return [];
        }
    }
}
