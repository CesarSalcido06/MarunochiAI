import * as vscode from 'vscode';
import { MarunochiAPIClient, ChatMessage } from './api';

interface ChatEntry {
    role: 'user' | 'assistant';
    content: string;
    timestamp: Date;
    context?: {
        file?: string;
        selection?: string;
        language?: string;
    };
}

/**
 * Full Chat Panel - Copilot-style sidebar chat experience
 */
export class ChatPanelProvider implements vscode.WebviewViewProvider {
    public static readonly viewType = 'marunochiAI.chatPanel';
    private _view?: vscode.WebviewView;
    private _conversationHistory: ChatEntry[] = [];
    private _isStreaming = false;

    constructor(
        private readonly _extensionUri: vscode.Uri,
        private readonly _apiClient: MarunochiAPIClient
    ) {}

    public resolveWebviewView(
        webviewView: vscode.WebviewView,
        context: vscode.WebviewViewResolveContext,
        _token: vscode.CancellationToken
    ) {
        this._view = webviewView;

        webviewView.webview.options = {
            enableScripts: true,
            localResourceRoots: [this._extensionUri],
        };

        webviewView.webview.html = this._getHtmlForWebview(webviewView.webview);

        // Handle messages from the webview
        webviewView.webview.onDidReceiveMessage(async (data) => {
            switch (data.type) {
                case 'sendMessage':
                    await this._handleUserMessage(data.message);
                    break;
                case 'insertCode':
                    await this._insertCodeToEditor(data.code);
                    break;
                case 'copyCode':
                    await vscode.env.clipboard.writeText(data.code);
                    vscode.window.showInformationMessage('Code copied to clipboard');
                    break;
                case 'clearHistory':
                    this._conversationHistory = [];
                    this._updateWebview();
                    break;
                case 'newChat':
                    this._conversationHistory = [];
                    this._updateWebview();
                    break;
            }
        });
    }

    /**
     * Handle user message and get AI response
     */
    private async _handleUserMessage(message: string): Promise<void> {
        if (this._isStreaming || !message.trim()) {
            return;
        }

        // Get current context
        const editor = vscode.window.activeTextEditor;
        const context: ChatEntry['context'] = {};

        if (editor) {
            context.file = editor.document.fileName;
            context.language = editor.document.languageId;

            if (!editor.selection.isEmpty) {
                context.selection = editor.document.getText(editor.selection);
            }
        }

        // Add user message to history
        const userEntry: ChatEntry = {
            role: 'user',
            content: message,
            timestamp: new Date(),
            context,
        };
        this._conversationHistory.push(userEntry);
        this._updateWebview();

        // Build messages for API
        const messages: ChatMessage[] = this._buildAPIMessages(message, context);

        // Start streaming response
        this._isStreaming = true;
        this._view?.webview.postMessage({ type: 'streamStart' });

        try {
            const response = await this._apiClient.chatCompletion(messages);
            const assistantContent = response.choices[0].message.content;

            // Add assistant response to history
            const assistantEntry: ChatEntry = {
                role: 'assistant',
                content: assistantContent,
                timestamp: new Date(),
            };
            this._conversationHistory.push(assistantEntry);

            this._view?.webview.postMessage({
                type: 'streamEnd',
                content: assistantContent,
            });
        } catch (error) {
            this._view?.webview.postMessage({
                type: 'error',
                message: `Error: ${error}`,
            });
        } finally {
            this._isStreaming = false;
            this._updateWebview();
        }
    }

    /**
     * Build API messages with context
     */
    private _buildAPIMessages(userMessage: string, context: ChatEntry['context']): ChatMessage[] {
        const messages: ChatMessage[] = [];

        // System message with context
        let systemContent = `You are MarunochiAI, an expert coding assistant running locally on the user's machine.
You have access to Qwen2.5-Coder models optimized for code generation.

Guidelines:
- Provide concise, accurate code solutions
- Use markdown code blocks with language identifiers
- Explain your reasoning briefly
- If asked about files, reference the context provided
- Be helpful but not verbose`;

        if (context?.file) {
            systemContent += `\n\nCurrent file: ${context.file}`;
        }
        if (context?.language) {
            systemContent += `\nLanguage: ${context.language}`;
        }

        messages.push({ role: 'system', content: systemContent });

        // Add conversation history (last 10 messages for context)
        const recentHistory = this._conversationHistory.slice(-10);
        for (const entry of recentHistory) {
            if (entry.role === 'user') {
                let content = entry.content;
                if (entry.context?.selection) {
                    content = `[Selected code]\n\`\`\`${entry.context.language || ''}\n${entry.context.selection}\n\`\`\`\n\n${entry.content}`;
                }
                messages.push({ role: 'user', content });
            } else {
                messages.push({ role: 'assistant', content: entry.content });
            }
        }

        // Add current message with selection if any
        let currentMessage = userMessage;
        if (context?.selection) {
            currentMessage = `[Selected code]\n\`\`\`${context.language || ''}\n${context.selection}\n\`\`\`\n\n${userMessage}`;
        }
        messages.push({ role: 'user', content: currentMessage });

        return messages;
    }

    /**
     * Insert code into active editor
     */
    private async _insertCodeToEditor(code: string): Promise<void> {
        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            vscode.window.showWarningMessage('No active editor to insert code');
            return;
        }

        await editor.edit((editBuilder) => {
            if (editor.selection.isEmpty) {
                editBuilder.insert(editor.selection.active, code);
            } else {
                editBuilder.replace(editor.selection, code);
            }
        });
    }

    /**
     * Update webview with current state
     */
    private _updateWebview(): void {
        if (this._view) {
            this._view.webview.postMessage({
                type: 'updateHistory',
                history: this._conversationHistory,
            });
        }
    }

    /**
     * Send a message programmatically (e.g., from commands)
     */
    public async sendMessage(message: string): Promise<void> {
        if (this._view) {
            this._view.show(true);
            await this._handleUserMessage(message);
        }
    }

    /**
     * Get HTML content for the webview
     */
    private _getHtmlForWebview(webview: vscode.Webview): string {
        return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MarunochiAI Chat</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: var(--vscode-font-family);
            font-size: var(--vscode-font-size);
            color: var(--vscode-foreground);
            background: var(--vscode-sideBar-background);
            height: 100vh;
            display: flex;
            flex-direction: column;
        }

        .header {
            padding: 12px 16px;
            border-bottom: 1px solid var(--vscode-panel-border);
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .header-title {
            display: flex;
            align-items: center;
            gap: 8px;
            font-weight: 600;
        }

        .header-title .icon {
            font-size: 18px;
        }

        .header-actions {
            display: flex;
            gap: 8px;
        }

        .header-btn {
            background: none;
            border: none;
            color: var(--vscode-foreground);
            cursor: pointer;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 12px;
        }

        .header-btn:hover {
            background: var(--vscode-toolbar-hoverBackground);
        }

        .status {
            display: flex;
            align-items: center;
            gap: 6px;
            padding: 8px 16px;
            font-size: 11px;
            color: var(--vscode-descriptionForeground);
            border-bottom: 1px solid var(--vscode-panel-border);
        }

        .status-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: #3fb950;
        }

        .status-dot.offline {
            background: #f85149;
        }

        .messages {
            flex: 1;
            overflow-y: auto;
            padding: 16px;
            display: flex;
            flex-direction: column;
            gap: 16px;
        }

        .message {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }

        .message-header {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 12px;
        }

        .message-avatar {
            width: 24px;
            height: 24px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 12px;
            font-weight: 600;
        }

        .message.user .message-avatar {
            background: var(--vscode-button-background);
            color: var(--vscode-button-foreground);
        }

        .message.assistant .message-avatar {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }

        .message-name {
            font-weight: 600;
        }

        .message-time {
            color: var(--vscode-descriptionForeground);
            font-size: 11px;
        }

        .message-content {
            padding-left: 32px;
            line-height: 1.5;
        }

        .message-content p {
            margin-bottom: 8px;
        }

        .message-content code {
            background: var(--vscode-textCodeBlock-background);
            padding: 2px 6px;
            border-radius: 4px;
            font-family: var(--vscode-editor-font-family);
            font-size: 0.9em;
        }

        .code-block {
            position: relative;
            margin: 12px 0;
            border-radius: 8px;
            overflow: hidden;
            background: var(--vscode-editor-background);
            border: 1px solid var(--vscode-panel-border);
        }

        .code-block-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 8px 12px;
            background: var(--vscode-editorGroupHeader-tabsBackground);
            border-bottom: 1px solid var(--vscode-panel-border);
            font-size: 11px;
        }

        .code-block-lang {
            color: var(--vscode-descriptionForeground);
        }

        .code-block-actions {
            display: flex;
            gap: 4px;
        }

        .code-block-btn {
            background: var(--vscode-button-secondaryBackground);
            color: var(--vscode-button-secondaryForeground);
            border: none;
            padding: 4px 8px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 11px;
            display: flex;
            align-items: center;
            gap: 4px;
        }

        .code-block-btn:hover {
            background: var(--vscode-button-secondaryHoverBackground);
        }

        .code-block pre {
            margin: 0;
            padding: 12px;
            overflow-x: auto;
            font-family: var(--vscode-editor-font-family);
            font-size: 13px;
            line-height: 1.4;
        }

        .input-area {
            padding: 12px 16px;
            border-top: 1px solid var(--vscode-panel-border);
            background: var(--vscode-sideBar-background);
        }

        .input-container {
            display: flex;
            gap: 8px;
            align-items: flex-end;
        }

        .input-wrapper {
            flex: 1;
            position: relative;
        }

        #messageInput {
            width: 100%;
            min-height: 40px;
            max-height: 120px;
            padding: 10px 12px;
            border: 1px solid var(--vscode-input-border);
            border-radius: 8px;
            background: var(--vscode-input-background);
            color: var(--vscode-input-foreground);
            font-family: var(--vscode-font-family);
            font-size: var(--vscode-font-size);
            resize: none;
            outline: none;
        }

        #messageInput:focus {
            border-color: var(--vscode-focusBorder);
        }

        #messageInput::placeholder {
            color: var(--vscode-input-placeholderForeground);
        }

        .send-btn {
            width: 40px;
            height: 40px;
            border: none;
            border-radius: 8px;
            background: var(--vscode-button-background);
            color: var(--vscode-button-foreground);
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 16px;
        }

        .send-btn:hover {
            background: var(--vscode-button-hoverBackground);
        }

        .send-btn:disabled {
            opacity: 0.5;
            cursor: not-allowed;
        }

        .context-indicator {
            font-size: 11px;
            color: var(--vscode-descriptionForeground);
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .context-badge {
            background: var(--vscode-badge-background);
            color: var(--vscode-badge-foreground);
            padding: 2px 8px;
            border-radius: 10px;
            font-size: 10px;
        }

        .loading {
            display: flex;
            align-items: center;
            gap: 8px;
            padding-left: 32px;
            color: var(--vscode-descriptionForeground);
        }

        .loading-dots {
            display: flex;
            gap: 4px;
        }

        .loading-dots span {
            width: 6px;
            height: 6px;
            background: var(--vscode-foreground);
            border-radius: 50%;
            animation: bounce 1.4s infinite ease-in-out both;
        }

        .loading-dots span:nth-child(1) { animation-delay: -0.32s; }
        .loading-dots span:nth-child(2) { animation-delay: -0.16s; }

        @keyframes bounce {
            0%, 80%, 100% { transform: scale(0); }
            40% { transform: scale(1); }
        }

        .empty-state {
            flex: 1;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 32px;
            color: var(--vscode-descriptionForeground);
        }

        .empty-state .icon {
            font-size: 48px;
            margin-bottom: 16px;
            opacity: 0.5;
        }

        .empty-state h3 {
            color: var(--vscode-foreground);
            margin-bottom: 8px;
        }

        .empty-state p {
            max-width: 280px;
            line-height: 1.5;
        }

        .suggestions {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-top: 16px;
        }

        .suggestion {
            background: var(--vscode-button-secondaryBackground);
            color: var(--vscode-button-secondaryForeground);
            border: none;
            padding: 6px 12px;
            border-radius: 16px;
            cursor: pointer;
            font-size: 12px;
        }

        .suggestion:hover {
            background: var(--vscode-button-secondaryHoverBackground);
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="header-title">
            <span class="icon">✨</span>
            <span>MarunochiAI</span>
        </div>
        <div class="header-actions">
            <button class="header-btn" id="newChatBtn" title="New Chat">+ New</button>
            <button class="header-btn" id="clearBtn" title="Clear History">Clear</button>
        </div>
    </div>

    <div class="status">
        <span class="status-dot" id="statusDot"></span>
        <span id="statusText">Connected to localhost:8765</span>
    </div>

    <div class="messages" id="messages">
        <div class="empty-state" id="emptyState">
            <div class="icon">🚀</div>
            <h3>Welcome to MarunochiAI</h3>
            <p>Your local AI coding assistant. Ask anything about code, get explanations, refactoring suggestions, and more.</p>
            <div class="suggestions">
                <button class="suggestion" data-prompt="Explain the selected code">Explain code</button>
                <button class="suggestion" data-prompt="How can I improve this code?">Improve code</button>
                <button class="suggestion" data-prompt="Write unit tests for this">Write tests</button>
                <button class="suggestion" data-prompt="Find bugs in this code">Find bugs</button>
            </div>
        </div>
    </div>

    <div class="input-area">
        <div class="context-indicator" id="contextIndicator" style="display: none;">
            <span>Context:</span>
            <span class="context-badge" id="contextFile"></span>
            <span class="context-badge" id="contextSelection" style="display: none;">Selection</span>
        </div>
        <div class="input-container">
            <div class="input-wrapper">
                <textarea
                    id="messageInput"
                    placeholder="Ask MarunochiAI... (Cmd+Enter to send)"
                    rows="1"
                ></textarea>
            </div>
            <button class="send-btn" id="sendBtn" title="Send message">→</button>
        </div>
    </div>

    <script>
        const vscode = acquireVsCodeApi();
        const messagesContainer = document.getElementById('messages');
        const messageInput = document.getElementById('messageInput');
        const sendBtn = document.getElementById('sendBtn');
        const emptyState = document.getElementById('emptyState');
        const contextIndicator = document.getElementById('contextIndicator');
        const contextFile = document.getElementById('contextFile');
        const contextSelection = document.getElementById('contextSelection');
        const statusDot = document.getElementById('statusDot');
        const statusText = document.getElementById('statusText');

        let isStreaming = false;
        let conversationHistory = [];

        // Auto-resize textarea
        messageInput.addEventListener('input', () => {
            messageInput.style.height = 'auto';
            messageInput.style.height = Math.min(messageInput.scrollHeight, 120) + 'px';
        });

        // Send message on Enter (Cmd+Enter or Ctrl+Enter)
        messageInput.addEventListener('keydown', (e) => {
            if ((e.metaKey || e.ctrlKey) && e.key === 'Enter') {
                e.preventDefault();
                sendMessage();
            }
        });

        sendBtn.addEventListener('click', sendMessage);

        document.getElementById('newChatBtn').addEventListener('click', () => {
            vscode.postMessage({ type: 'newChat' });
            conversationHistory = [];
            renderMessages();
        });

        document.getElementById('clearBtn').addEventListener('click', () => {
            vscode.postMessage({ type: 'clearHistory' });
            conversationHistory = [];
            renderMessages();
        });

        // Suggestion buttons
        document.querySelectorAll('.suggestion').forEach(btn => {
            btn.addEventListener('click', () => {
                messageInput.value = btn.dataset.prompt;
                messageInput.focus();
            });
        });

        function sendMessage() {
            const message = messageInput.value.trim();
            if (!message || isStreaming) return;

            vscode.postMessage({ type: 'sendMessage', message });
            messageInput.value = '';
            messageInput.style.height = 'auto';
        }

        function renderMessages() {
            if (conversationHistory.length === 0) {
                emptyState.style.display = 'flex';
                messagesContainer.innerHTML = '';
                messagesContainer.appendChild(emptyState);
                return;
            }

            emptyState.style.display = 'none';
            messagesContainer.innerHTML = '';

            conversationHistory.forEach((entry, index) => {
                const messageEl = createMessageElement(entry);
                messagesContainer.appendChild(messageEl);
            });

            // Add loading indicator if streaming
            if (isStreaming) {
                const loadingEl = document.createElement('div');
                loadingEl.className = 'message assistant';
                loadingEl.innerHTML = \`
                    <div class="message-header">
                        <div class="message-avatar">M</div>
                        <span class="message-name">MarunochiAI</span>
                    </div>
                    <div class="loading">
                        <div class="loading-dots">
                            <span></span><span></span><span></span>
                        </div>
                        <span>Thinking...</span>
                    </div>
                \`;
                messagesContainer.appendChild(loadingEl);
            }

            messagesContainer.scrollTop = messagesContainer.scrollHeight;
        }

        function createMessageElement(entry) {
            const div = document.createElement('div');
            div.className = \`message \${entry.role}\`;

            const time = new Date(entry.timestamp).toLocaleTimeString([], {
                hour: '2-digit',
                minute: '2-digit'
            });

            const isUser = entry.role === 'user';
            const avatar = isUser ? 'U' : 'M';
            const name = isUser ? 'You' : 'MarunochiAI';

            div.innerHTML = \`
                <div class="message-header">
                    <div class="message-avatar">\${avatar}</div>
                    <span class="message-name">\${name}</span>
                    <span class="message-time">\${time}</span>
                </div>
                <div class="message-content">\${formatContent(entry.content)}</div>
            \`;

            return div;
        }

        function formatContent(content) {
            // Escape HTML first
            let formatted = content
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;');

            // Format code blocks
            formatted = formatted.replace(
                /\`\`\`(\\w*)\\n([\\s\\S]*?)\`\`\`/g,
                (match, lang, code) => {
                    const escapedCode = code.trim();
                    return \`
                        <div class="code-block">
                            <div class="code-block-header">
                                <span class="code-block-lang">\${lang || 'code'}</span>
                                <div class="code-block-actions">
                                    <button class="code-block-btn" onclick="copyCode(this)" data-code="\${encodeURIComponent(escapedCode)}">📋 Copy</button>
                                    <button class="code-block-btn" onclick="insertCode(this)" data-code="\${encodeURIComponent(escapedCode)}">⎘ Insert</button>
                                </div>
                            </div>
                            <pre>\${escapedCode}</pre>
                        </div>
                    \`;
                }
            );

            // Format inline code
            formatted = formatted.replace(
                /\`([^\`]+)\`/g,
                '<code>$1</code>'
            );

            // Format bold
            formatted = formatted.replace(
                /\\*\\*([^*]+)\\*\\*/g,
                '<strong>$1</strong>'
            );

            // Format paragraphs
            formatted = formatted.replace(/\\n\\n/g, '</p><p>');
            formatted = formatted.replace(/\\n/g, '<br>');
            formatted = '<p>' + formatted + '</p>';

            return formatted;
        }

        function copyCode(btn) {
            const code = decodeURIComponent(btn.dataset.code);
            vscode.postMessage({ type: 'copyCode', code });
        }

        function insertCode(btn) {
            const code = decodeURIComponent(btn.dataset.code);
            vscode.postMessage({ type: 'insertCode', code });
        }

        // Make functions global for onclick handlers
        window.copyCode = copyCode;
        window.insertCode = insertCode;

        // Handle messages from extension
        window.addEventListener('message', event => {
            const message = event.data;

            switch (message.type) {
                case 'updateHistory':
                    conversationHistory = message.history;
                    renderMessages();
                    break;

                case 'streamStart':
                    isStreaming = true;
                    sendBtn.disabled = true;
                    renderMessages();
                    break;

                case 'streamEnd':
                    isStreaming = false;
                    sendBtn.disabled = false;
                    renderMessages();
                    break;

                case 'error':
                    isStreaming = false;
                    sendBtn.disabled = false;
                    // Show error in chat
                    conversationHistory.push({
                        role: 'assistant',
                        content: message.message,
                        timestamp: new Date()
                    });
                    renderMessages();
                    break;

                case 'updateContext':
                    if (message.file) {
                        contextIndicator.style.display = 'flex';
                        contextFile.textContent = message.file.split('/').pop();
                        contextSelection.style.display = message.hasSelection ? 'inline' : 'none';
                    } else {
                        contextIndicator.style.display = 'none';
                    }
                    break;

                case 'serverStatus':
                    statusDot.className = message.online ? 'status-dot' : 'status-dot offline';
                    statusText.textContent = message.online
                        ? 'Connected to localhost:8765'
                        : 'Disconnected - Server not running';
                    break;
            }
        });

        // Initial render
        renderMessages();
    </script>
</body>
</html>`;
    }
}
