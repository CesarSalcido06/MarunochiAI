import * as vscode from 'vscode';
import { MarunochiAPIClient, SearchResult } from './api';

export class SearchViewProvider implements vscode.TreeDataProvider<SearchResultItem> {
    private _onDidChangeTreeData: vscode.EventEmitter<SearchResultItem | undefined | null | void> =
        new vscode.EventEmitter<SearchResultItem | undefined | null | void>();
    readonly onDidChangeTreeData: vscode.Event<SearchResultItem | undefined | null | void> =
        this._onDidChangeTreeData.event;

    private results: SearchResult[] = [];

    constructor(private apiClient: MarunochiAPIClient) {}

    setResults(results: SearchResult[]) {
        this.results = results;
        this._onDidChangeTreeData.fire();
    }

    getTreeItem(element: SearchResultItem): vscode.TreeItem {
        return element;
    }

    getChildren(element?: SearchResultItem): Thenable<SearchResultItem[]> {
        if (!element) {
            return Promise.resolve(
                this.results.map(
                    r =>
                        new SearchResultItem(
                            r.metadata.name,
                            r.filepath,
                            r.metadata.line_range[0],
                            r.similarity,
                            vscode.TreeItemCollapsibleState.None
                        )
                )
            );
        }
        return Promise.resolve([]);
    }
}

class SearchResultItem extends vscode.TreeItem {
    constructor(
        public readonly label: string,
        private filepath: string,
        private line: number,
        private similarity: number,
        public readonly collapsibleState: vscode.TreeItemCollapsibleState
    ) {
        super(label, collapsibleState);

        this.tooltip = `${filepath}:${line} (${similarity.toFixed(3)})`;
        this.description = `${filepath.split('/').pop()}:${line}`;

        this.command = {
            command: 'vscode.open',
            title: 'Open File',
            arguments: [
                vscode.Uri.file(filepath),
                {
                    selection: new vscode.Range(
                        new vscode.Position(line - 1, 0),
                        new vscode.Position(line - 1, 0)
                    ),
                },
            ],
        };
    }
}
