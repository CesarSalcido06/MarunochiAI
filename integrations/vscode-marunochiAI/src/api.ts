import axios, { AxiosInstance } from 'axios';

export interface ChatMessage {
    role: 'system' | 'user' | 'assistant';
    content: string;
}

export interface SearchResult {
    filepath: string;
    content: string;
    similarity: number;
    metadata: {
        name: string;
        language: string;
        chunk_type: string;
        line_range: [number, number];
    };
}

export interface ChatCompletionResponse {
    id: string;
    choices: Array<{
        message: ChatMessage;
        finish_reason: string;
    }>;
}

export interface IndexResult {
    total_files: number;
    total_chunks: number;
    duration_ms: number;
    watcher_started?: boolean;
}

export interface Stats {
    vector: {
        total_chunks: number;
        total_files?: number;
    };
    keyword: {
        total_chunks: number;
    };
    rrf_k: number;
    fusion_enabled: boolean;
    watcher_running: boolean;
}

export interface CompletionRequest {
    prefix: string;
    suffix: string;
    language: string;
    filepath: string;
    maxTokens?: number;
}

export class MarunochiAPIClient {
    private client: AxiosInstance;

    constructor(private baseURL: string, private apiKey?: string) {
        this.client = axios.create({
            baseURL,
            headers: apiKey ? { Authorization: `Bearer ${apiKey}` } : {},
            timeout: 10000, // 10s for completions
        });
    }

    async searchCodebase(query: string, limit: number = 10): Promise<SearchResult[]> {
        const response = await this.client.post('/v1/codebase/search', {
            query,
            limit,
        });
        return response.data.results;
    }

    async indexCodebase(path: string, watch: boolean = false): Promise<IndexResult> {
        const response = await this.client.post(
            `/v1/codebase/index?codebase_path=${encodeURIComponent(path)}&watch=${watch}`
        );
        return response.data;
    }

    async getStats(): Promise<Stats> {
        const response = await this.client.get('/v1/codebase/stats');
        return response.data;
    }

    async chatCompletion(messages: ChatMessage[], stream: boolean = false): Promise<ChatCompletionResponse> {
        const response = await this.client.post('/v1/chat/completions', {
            messages,
            stream,
        });
        return response.data;
    }

    /**
     * Get inline code completion using Fill-in-the-Middle (FIM) format
     */
    async getInlineCompletion(request: CompletionRequest): Promise<string> {
        const { prefix, suffix, language, filepath, maxTokens = 150 } = request;

        // Use FIM-style prompt for code completion
        const prompt = `<|fim_prefix|>${prefix}<|fim_suffix|>${suffix}<|fim_middle|>`;

        const messages: ChatMessage[] = [
            {
                role: 'system',
                content: `You are an expert code completion assistant. Complete the code at the cursor position.
Language: ${language}
File: ${filepath}
Rules:
- Output ONLY the code to insert at the cursor
- No explanations, no markdown, no code blocks
- Match the existing code style and indentation
- Keep completions concise (1-3 lines typically)
- If completing a function call, include the closing parenthesis
- If completing a statement, include the semicolon if appropriate`,
            },
            {
                role: 'user',
                content: prompt,
            },
        ];

        const response = await this.client.post('/v1/chat/completions', {
            messages,
            max_tokens: maxTokens,
            temperature: 0.2, // Low temperature for more deterministic completions
            stream: false,
        });

        return response.data.choices[0].message.content.trim();
    }

    /**
     * Streaming chat for inline edits
     */
    async *streamChat(messages: ChatMessage[]): AsyncGenerator<string> {
        const response = await this.client.post('/v1/chat/completions', {
            messages,
            stream: true,
        }, {
            responseType: 'stream',
            timeout: 60000, // 60s for streaming
        });

        const stream = response.data;
        let buffer = '';

        for await (const chunk of stream) {
            buffer += chunk.toString();
            const lines = buffer.split('\n');
            buffer = lines.pop() || '';

            for (const line of lines) {
                if (line.startsWith('data: ')) {
                    const data = line.slice(6);
                    if (data === '[DONE]') {
                        return;
                    }
                    try {
                        const parsed = JSON.parse(data);
                        const content = parsed.choices?.[0]?.delta?.content;
                        if (content) {
                            yield content;
                        }
                    } catch {
                        // Ignore parse errors
                    }
                }
            }
        }
    }

    async healthCheck(): Promise<boolean> {
        try {
            const response = await this.client.get('/health');
            return response.data.status === 'healthy';
        } catch {
            return false;
        }
    }
}
