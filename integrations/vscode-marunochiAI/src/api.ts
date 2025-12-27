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

export class MarunochiAPIClient {
    private client: AxiosInstance;

    constructor(private baseURL: string, private apiKey?: string) {
        this.client = axios.create({
            baseURL,
            headers: apiKey ? { Authorization: `Bearer ${apiKey}` } : {},
            timeout: 30000,
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

    async chatCompletion(messages: ChatMessage[]): Promise<ChatCompletionResponse> {
        const response = await this.client.post('/v1/chat/completions', {
            messages,
            stream: false,
        });
        return response.data;
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
