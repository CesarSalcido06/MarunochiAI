import * as vscode from 'vscode';
import { MarunochiAPIClient } from './api';

/**
 * Inline Completion Provider for Copilot-like ghost text suggestions.
 * Shows grayed-out code suggestions that can be accepted with Tab.
 */
export class MarunochiInlineCompletionProvider implements vscode.InlineCompletionItemProvider {
    private debounceTimer: NodeJS.Timeout | null = null;
    private lastCompletionTime = 0;
    private cache = new Map<string, { completion: string; timestamp: number }>();
    private readonly CACHE_TTL = 30000; // 30 seconds
    private readonly DEBOUNCE_MS = 150; // 150ms debounce
    private readonly MIN_PREFIX_LENGTH = 3; // Minimum chars before triggering

    constructor(private apiClient: MarunochiAPIClient) {}

    async provideInlineCompletionItems(
        document: vscode.TextDocument,
        position: vscode.Position,
        context: vscode.InlineCompletionContext,
        token: vscode.CancellationToken
    ): Promise<vscode.InlineCompletionItem[] | vscode.InlineCompletionList> {
        // Don't complete in comments or strings (basic check)
        const lineText = document.lineAt(position.line).text;
        const beforeCursor = lineText.substring(0, position.character);

        // Skip if line is a comment
        if (this.isComment(beforeCursor, document.languageId)) {
            return [];
        }

        // Skip if prefix is too short
        const trimmedPrefix = beforeCursor.trim();
        if (trimmedPrefix.length < this.MIN_PREFIX_LENGTH) {
            return [];
        }

        // Debounce the completion request
        return new Promise((resolve) => {
            if (this.debounceTimer) {
                clearTimeout(this.debounceTimer);
            }

            this.debounceTimer = setTimeout(async () => {
                if (token.isCancellationRequested) {
                    resolve([]);
                    return;
                }

                try {
                    const items = await this.generateCompletions(document, position, token);
                    resolve(items);
                } catch (error) {
                    console.error('MarunochiAI: Completion error:', error);
                    resolve([]);
                }
            }, this.DEBOUNCE_MS);
        });
    }

    private async generateCompletions(
        document: vscode.TextDocument,
        position: vscode.Position,
        token: vscode.CancellationToken
    ): Promise<vscode.InlineCompletionItem[]> {
        // Gather context
        const { prefix, suffix } = this.gatherContext(document, position);

        // Check cache
        const cacheKey = this.getCacheKey(prefix, suffix);
        const cached = this.cache.get(cacheKey);
        if (cached && Date.now() - cached.timestamp < this.CACHE_TTL) {
            return this.createCompletionItems(cached.completion, position);
        }

        // Check cancellation before API call
        if (token.isCancellationRequested) {
            return [];
        }

        try {
            const completion = await this.apiClient.getInlineCompletion({
                prefix,
                suffix,
                language: document.languageId,
                filepath: document.fileName,
                maxTokens: 150,
            });

            // Check cancellation after API call
            if (token.isCancellationRequested) {
                return [];
            }

            // Validate and clean completion
            const cleanedCompletion = this.cleanCompletion(completion, prefix);

            if (!cleanedCompletion) {
                return [];
            }

            // Cache the result
            this.cache.set(cacheKey, {
                completion: cleanedCompletion,
                timestamp: Date.now(),
            });

            // Cleanup old cache entries
            this.cleanupCache();

            return this.createCompletionItems(cleanedCompletion, position);
        } catch (error) {
            console.error('MarunochiAI: API error:', error);
            return [];
        }
    }

    private gatherContext(
        document: vscode.TextDocument,
        position: vscode.Position
    ): { prefix: string; suffix: string } {
        // Get prefix: current line up to cursor + 50 lines before
        const prefixStartLine = Math.max(0, position.line - 50);
        const prefixRange = new vscode.Range(
            new vscode.Position(prefixStartLine, 0),
            position
        );
        const prefix = document.getText(prefixRange);

        // Get suffix: rest of current line + 20 lines after
        const suffixEndLine = Math.min(document.lineCount - 1, position.line + 20);
        const suffixRange = new vscode.Range(
            position,
            new vscode.Position(suffixEndLine, document.lineAt(suffixEndLine).text.length)
        );
        const suffix = document.getText(suffixRange);

        return { prefix, suffix };
    }

    private createCompletionItems(
        completion: string,
        position: vscode.Position
    ): vscode.InlineCompletionItem[] {
        if (!completion) {
            return [];
        }

        const item = new vscode.InlineCompletionItem(
            completion,
            new vscode.Range(position, position)
        );

        return [item];
    }

    private cleanCompletion(completion: string, prefix: string): string {
        if (!completion) {
            return '';
        }

        // Remove markdown code blocks if present
        let cleaned = completion
            .replace(/^```[\w]*\n?/gm, '')
            .replace(/\n?```$/gm, '')
            .trim();

        // Remove any leading explanation text
        const codeStart = cleaned.search(/^[\s]*[a-zA-Z0-9_({[\]'"`.]/m);
        if (codeStart > 0) {
            cleaned = cleaned.substring(codeStart);
        }

        // If completion starts with the end of prefix, remove overlap
        const lastPrefixLine = prefix.split('\n').pop() || '';
        if (cleaned.startsWith(lastPrefixLine.trim())) {
            cleaned = cleaned.substring(lastPrefixLine.trim().length);
        }

        // Limit to reasonable length (max 500 chars)
        if (cleaned.length > 500) {
            cleaned = cleaned.substring(0, 500);
            // Try to end at a complete line or statement
            const lastNewline = cleaned.lastIndexOf('\n');
            const lastSemi = cleaned.lastIndexOf(';');
            const lastBrace = cleaned.lastIndexOf('}');
            const cutPoint = Math.max(lastNewline, lastSemi, lastBrace);
            if (cutPoint > 0) {
                cleaned = cleaned.substring(0, cutPoint + 1);
            }
        }

        return cleaned.trim();
    }

    private isComment(text: string, languageId: string): boolean {
        const trimmed = text.trim();

        // Common comment patterns
        if (trimmed.startsWith('//') || trimmed.startsWith('#') || trimmed.startsWith('--')) {
            return true;
        }
        if (trimmed.includes('/*') && !trimmed.includes('*/')) {
            return true;
        }

        return false;
    }

    private getCacheKey(prefix: string, suffix: string): string {
        // Use last 200 chars of prefix and first 100 chars of suffix
        const prefixKey = prefix.slice(-200);
        const suffixKey = suffix.slice(0, 100);
        return `${prefixKey}|||${suffixKey}`;
    }

    private cleanupCache(): void {
        const now = Date.now();
        for (const [key, value] of this.cache.entries()) {
            if (now - value.timestamp > this.CACHE_TTL) {
                this.cache.delete(key);
            }
        }
    }

    // Optional: Handle when user accepts completion
    handleDidShowCompletionItem?(completionItem: vscode.InlineCompletionItem): void {
        // Could log telemetry here
    }
}

/**
 * Status bar item to show completion status
 */
export class CompletionStatusBar {
    private statusBarItem: vscode.StatusBarItem;
    private isEnabled = true;

    constructor() {
        this.statusBarItem = vscode.window.createStatusBarItem(
            vscode.StatusBarAlignment.Right,
            100
        );
        this.statusBarItem.command = 'marunochiAI.toggleCompletion';
        this.updateStatus();
        this.statusBarItem.show();
    }

    toggle(): void {
        this.isEnabled = !this.isEnabled;
        this.updateStatus();
    }

    isCompletionEnabled(): boolean {
        return this.isEnabled;
    }

    private updateStatus(): void {
        if (this.isEnabled) {
            this.statusBarItem.text = '$(sparkle) Marunochi';
            this.statusBarItem.tooltip = 'MarunochiAI: Completions enabled (click to disable)';
            this.statusBarItem.backgroundColor = undefined;
        } else {
            this.statusBarItem.text = '$(circle-slash) Marunochi';
            this.statusBarItem.tooltip = 'MarunochiAI: Completions disabled (click to enable)';
            this.statusBarItem.backgroundColor = new vscode.ThemeColor('statusBarItem.warningBackground');
        }
    }

    dispose(): void {
        this.statusBarItem.dispose();
    }
}
