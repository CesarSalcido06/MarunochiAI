import * as vscode from 'vscode';
import { MarunochiAPIClient, ChatMessage } from './api';

export class ChatViewProvider implements vscode.WebviewViewProvider {
    private _view?: vscode.WebviewView;
    private history: ChatMessage[] = [];

    constructor(private apiClient: MarunochiAPIClient) {}

    public resolveWebviewView(
        webviewView: vscode.WebviewView,
        context: vscode.WebviewViewResolveContext,
        _token: vscode.CancellationToken
    ) {
        this._view = webviewView;

        webviewView.webview.options = {
            enableScripts: true,
        };

        webviewView.webview.html = this.getHtmlForWebview(webviewView.webview);

        webviewView.webview.onDidReceiveMessage(async data => {
            switch (data.type) {
                case 'sendMessage':
                    await this.handleUserMessage(data.message);
                    break;
            }
        });
    }

    public async sendMessage(message: string) {
        if (this._view) {
            await this.handleUserMessage(message);
        }
    }

    private async handleUserMessage(message: string) {
        this.history.push({ role: 'user', content: message });

        // Display user message
        this._view?.webview.postMessage({
            type: 'userMessage',
            message,
        });

        try {
            const response = await this.apiClient.chatCompletion(this.history);
            const assistantMessage = response.choices[0].message.content;

            this.history.push({ role: 'assistant', content: assistantMessage });

            this._view?.webview.postMessage({
                type: 'assistantMessage',
                message: assistantMessage,
            });
        } catch (error) {
            this._view?.webview.postMessage({
                type: 'error',
                message: `Error: ${error}`,
            });
        }
    }

    private getHtmlForWebview(webview: vscode.Webview) {
        return `
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>MarunochiAI Chat</title>
                <style>
                    body {
                        font-family: var(--vscode-font-family);
                        padding: 10px;
                        color: var(--vscode-foreground);
                    }
                    #chat {
                        height: calc(100vh - 100px);
                        overflow-y: auto;
                        margin-bottom: 10px;
                    }
                    .message {
                        margin-bottom: 15px;
                        padding: 10px;
                        border-radius: 5px;
                    }
                    .user {
                        background: var(--vscode-input-background);
                    }
                    .assistant {
                        background: var(--vscode-editor-background);
                    }
                    #input-container {
                        display: flex;
                        gap: 5px;
                    }
                    #message-input {
                        flex: 1;
                        padding: 8px;
                        background: var(--vscode-input-background);
                        color: var(--vscode-input-foreground);
                        border: 1px solid var(--vscode-input-border);
                    }
                    button {
                        padding: 8px 15px;
                        background: var(--vscode-button-background);
                        color: var(--vscode-button-foreground);
                        border: none;
                        cursor: pointer;
                    }
                    button:hover {
                        background: var(--vscode-button-hoverBackground);
                    }
                </style>
            </head>
            <body>
                <div id="chat"></div>
                <div id="input-container">
                    <input type="text" id="message-input" placeholder="Ask anything..." />
                    <button onclick="sendMessage()">Send</button>
                </div>

                <script>
                    const vscode = acquireVsCodeApi();
                    const chat = document.getElementById('chat');
                    const input = document.getElementById('message-input');

                    window.addEventListener('message', event => {
                        const message = event.data;
                        if (message.type === 'userMessage') {
                            addMessage('You', message.message, 'user');
                        } else if (message.type === 'assistantMessage') {
                            addMessage('MarunochiAI', message.message, 'assistant');
                        } else if (message.type === 'error') {
                            addMessage('Error', message.message, 'assistant');
                        }
                    });

                    function addMessage(sender, text, className) {
                        const div = document.createElement('div');
                        div.className = 'message ' + className;
                        div.innerHTML = '<strong>' + sender + ':</strong><br/>' + text.replace(/\n/g, '<br/>');
                        chat.appendChild(div);
                        chat.scrollTop = chat.scrollHeight;
                    }

                    function sendMessage() {
                        const message = input.value.trim();
                        if (message) {
                            vscode.postMessage({
                                type: 'sendMessage',
                                message: message
                            });
                            input.value = '';
                        }
                    }

                    input.addEventListener('keypress', e => {
                        if (e.key === 'Enter') {
                            sendMessage();
                        }
                    });
                </script>
            </body>
            </html>
        `;
    }
}
