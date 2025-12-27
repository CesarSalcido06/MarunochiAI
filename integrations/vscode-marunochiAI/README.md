# MarunochiAI for Visual Studio Code

The most powerful VSCode extension for AI-powered coding assistance with semantic code understanding.

![MarunochiAI Logo](https://img.shields.io/badge/MarunochiAI-0.2.0-blue)
![VSCode](https://img.shields.io/badge/VSCode-1.80+-green)
![License](https://img.shields.io/badge/license-MIT-orange)

## ✨ Features

### 🔍 Semantic Code Search
Search your entire codebase using natural language queries powered by hybrid vector + keyword search.

### 🤖 AI-Powered Completions
Get context-aware code completions powered by Qwen2.5-Coder (7B/14B) running locally via Ollama.

### 💬 Inline Chat
Chat with MarunochiAI directly in VSCode to ask coding questions, get explanations, or brainstorm solutions.

### 🛠️ Code Actions
- **Explain Code**: Get detailed explanations of selected code
- **Refactor Code**: AI-powered refactoring suggestions
- **Debug Code**: Identify potential bugs and issues
- **Generate Tests**: Create comprehensive unit tests

### 📊 Real-Time Indexing
Automatically indexes your workspace on startup and keeps it in sync with file changes.

### 🎨 Beautiful UI
- Sidebar views for search results and chat
- Syntax-highlighted code previews
- Quick pick for rapid navigation

## 📦 Installation

### Prerequisites

1. **Install MarunochiAI server**:
   ```bash
   # Clone repository
   git clone https://github.com/CesarSalcido06/MarunochiAI
   cd MarunochiAI

   # Install dependencies
   pip install -e .

   # Start server
   marunochithe server
   ```

2. **Install Ollama** (for AI inference):
   ```bash
   # macOS/Linux
   curl -fsSL https://ollama.ai/install.sh | sh

   # Pull model
   ollama pull qwen2.5-coder:7b
   ```

### Install Extension

#### From Source (Development)

```bash
cd integrations/vscode-marunochiAI
npm install
npm run compile

# Open in VSCode
code .

# Press F5 to launch Extension Development Host
```

#### From Marketplace (Coming Soon)

Search for "MarunochiAI" in VSCode Extensions marketplace.

## ⚙️ Configuration

Open VSCode Settings and configure:

```json
{
  "marunochiAI.apiUrl": "http://localhost:8765",
  "marunochiAI.apiKey": "",
  "marunochiAI.model": "auto",
  "marunochiAI.autoIndex": true,
  "marunochiAI.enableCompletion": true,
  "marunochiAI.searchLimit": 10,
  "marunochiAI.enableInlineChat": true
}
```

### Settings

| Setting | Default | Description |
|---------|---------|-------------|
| `marunochiAI.apiUrl` | `http://localhost:8765` | MarunochiAI server URL |
| `marunochiAI.apiKey` | `""` | Optional API key |
| `marunochiAI.model` | `auto` | Model selection (auto/7b/14b/custom) |
| `marunochiAI.autoIndex` | `true` | Auto-index workspace on startup |
| `marunochiAI.enableCompletion` | `true` | Enable AI completions |
| `marunochiAI.searchLimit` | `10` | Max search results |
| `marunochiAI.enableInlineChat` | `true` | Enable inline chat features |

## 🚀 Usage

### Commands

Access via Command Palette (`Cmd+Shift+P` / `Ctrl+Shift+P`):

- **MarunochiAI: Index Workspace** - Index current workspace
- **MarunochiAI: Search Code** - Semantic code search
- **MarunochiAI: Open Chat** - Open chat panel
- **MarunochiAI: Explain Code** - Explain selected code
- **MarunochiAI: Refactor Code** - Get refactoring suggestions
- **MarunochiAI: Debug Code** - Debug selected code
- **MarunochiAI: Generate Tests** - Generate unit tests
- **MarunochiAI: Show Statistics** - View indexing stats

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Cmd+Shift+F` | Search Code |
| `Cmd+Shift+C` | Open Chat |
| `Cmd+Shift+E` | Explain Code (with selection) |

### Context Menu

Right-click on selected code to access:
- 💡 Explain with MarunochiAI
- 🔧 Refactor with MarunochiAI
- 🐛 Debug with MarunochiAI
- 🧪 Generate Tests

## 🎯 Examples

### Semantic Search

1. Press `Cmd+Shift+F` or run "MarunochiAI: Search Code"
2. Enter query: `"authentication function"`
3. Browse results with similarity scores
4. Click to jump to code

### Code Explanation

1. Select code in editor
2. Press `Cmd+Shift+E` or right-click → "Explain with MarunochiAI"
3. View detailed explanation in preview panel

### AI-Powered Refactoring

1. Select code to refactor
2. Right-click → "Refactor with MarunochiAI"
3. Review suggestions
4. Click "Apply" to update code

### Interactive Chat

1. Click MarunochiAI icon in Activity Bar
2. Open Chat view
3. Type your question
4. Get streaming AI responses

## 🏗️ Architecture

```
┌─────────────────────────────────────┐
│    VSCode Extension (TypeScript)    │
│  ┌────────┬─────────┬────────────┐  │
│  │ Search │ Chat    │ Completion │  │
│  │ View   │ View    │ Provider   │  │
│  └───┬────┴────┬────┴──────┬─────┘  │
│      │         │           │        │
│      └─────────┴───────────┘        │
│         API Client (axios)          │
└──────────────┬──────────────────────┘
               │ HTTP/REST
┌──────────────▼──────────────────────┐
│     MarunochiAI Server :8765        │
│  ┌──────────────────────────────┐   │
│  │  Hybrid Search (RRF Fusion)  │   │
│  │  Vector + Keyword + Graph    │   │
│  └──────────────────────────────┘   │
│  ┌──────────────────────────────┐   │
│  │  Ollama (Qwen2.5-Coder)      │   │
│  │  7B/14B Auto-Routing         │   │
│  └──────────────────────────────┘   │
└─────────────────────────────────────┘
```

## 🤝 Multi-Agent Integration

MarunochiAI works as part of a multi-agent system:

- **BenchAI**: Orchestrates complex tasks, routes to MarunochiAI for coding
- **DottscavisAI**: Handles creative/multimedia tasks
- **MarunochiAI**: Specializes in code understanding and generation

The extension automatically benefits from distributed intelligence when connected to BenchAI.

## 📊 Performance

- **Search latency**: <200ms
- **Completion latency**: <500ms
- **Indexing**: ~45s for 10K files
- **Memory usage**: ~100MB

## 🐛 Troubleshooting

### Extension not working

1. Check server is running:
   ```bash
   curl http://localhost:8765/health
   ```

2. View extension logs:
   - Open Developer Tools: `Help → Toggle Developer Tools`
   - Check Console for errors

### No completions showing

1. Ensure `marunochiAI.enableCompletion` is `true`
2. Wait for workspace indexing to complete
3. Check Ollama is running: `ollama list`

### Search returns no results

Run "MarunochiAI: Index Workspace" to reindex.

## 🛣️ Roadmap

- [ ] Streaming completions for faster response
- [ ] Multi-file refactoring
- [ ] Code review integration
- [ ] Git commit message generation
- [ ] Documentation generation
- [ ] VS Code for Web support

## 📝 License

MIT License - See main MarunochiAI repository

## 🙏 Credits

- [Visual Studio Code](https://code.visualstudio.com/)
- [Ollama](https://ollama.ai/)
- [Qwen2.5-Coder](https://huggingface.co/Qwen/Qwen2.5-Coder)
- [MarunochiAI](https://github.com/CesarSalcido06/MarunochiAI)

## 📞 Support

- [GitHub Issues](https://github.com/CesarSalcido06/MarunochiAI/issues)
- [Documentation](https://github.com/CesarSalcido06/MarunochiAI/docs)

---

**Made with ❤️ by the MarunochiAI team**

*The most powerful self-hosted coding assistant*
