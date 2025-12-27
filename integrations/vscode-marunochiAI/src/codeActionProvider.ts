import * as vscode from 'vscode';
import { MarunochiAPIClient } from './api';

export class MarunochiCodeActionProvider implements vscode.CodeActionProvider {
    constructor(private apiClient: MarunochiAPIClient) {}

    public provideCodeActions(
        document: vscode.TextDocument,
        range: vscode.Range | vscode.Selection,
        context: vscode.CodeActionContext,
        token: vscode.CancellationToken
    ): vscode.CodeAction[] {
        const actions: vscode.CodeAction[] = [];

        // Only show actions when there's a selection
        if (!range.isEmpty) {
            // Explain code action
            const explainAction = new vscode.CodeAction(
                '💡 Explain with MarunochiAI',
                vscode.CodeActionKind.RefactorInline
            );
            explainAction.command = {
                command: 'marunochiAI.explainCode',
                title: 'Explain Code',
            };
            actions.push(explainAction);

            // Refactor code action
            const refactorAction = new vscode.CodeAction(
                '🔧 Refactor with MarunochiAI',
                vscode.CodeActionKind.Refactor
            );
            refactorAction.command = {
                command: 'marunochiAI.refactorCode',
                title: 'Refactor Code',
            };
            actions.push(refactorAction);

            // Debug code action
            const debugAction = new vscode.CodeAction(
                '🐛 Debug with MarunochiAI',
                vscode.CodeActionKind.QuickFix
            );
            debugAction.command = {
                command: 'marunochiAI.debugCode',
                title: 'Debug Code',
            };
            actions.push(debugAction);

            // Generate tests action
            const testAction = new vscode.CodeAction(
                '🧪 Generate Tests',
                vscode.CodeActionKind.RefactorExtract
            );
            testAction.command = {
                command: 'marunochiAI.generateTests',
                title: 'Generate Tests',
            };
            actions.push(testAction);
        }

        return actions;
    }
}
