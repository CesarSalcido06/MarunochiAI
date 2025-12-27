# nvim-marunochiAI

The most powerful Neovim plugin for AI-powered coding assistance with semantic code understanding.

## ✨ Features

- **🔍 Semantic Code Search**: Search your entire codebase using natural language
- **🤖 AI-Powered Completion**: Context-aware code completions via nvim-cmp
- **💬 Inline Chat**: Chat with MarunochiAI directly in Neovim
- **📖 Code Explanation**: Explain any code selection
- **🔧 Code Refactoring**: AI-powered refactoring suggestions
- **🐛 Debug Assistance**: Identify potential issues in code
- **📡 Real-time Indexing**: Automatic codebase indexing with file watching
- **🎨 Beautiful UI**: Telescope integration for search results

## 📦 Installation

### Using [lazy.nvim](https://github.com/folke/lazy.nvim)

```lua
{
  "CesarSalcido06/MarunochiAI",
  dir = "/path/to/MarunochiAI/integrations/nvim-marunochiAI",
  dependencies = {
    "nvim-telescope/telescope.nvim",  -- Optional but recommended
    "hrsh7th/nvim-cmp",                -- Optional for completions
  },
  config = function()
    require("marunochiAI").setup({
      api_url = "http://localhost:8765",
      auto_index = true,
      search_limit = 10,
      enable_completion = true,
      enable_inline_chat = true,
    })
  end,
}
```

### Using [packer.nvim](https://github.com/wbthomason/packer.nvim)

```lua
use {
  "CesarSalcido06/MarunochiAI",
  opt = { dir = "/path/to/MarunochiAI/integrations/nvim-marunochiAI" },
  requires = {
    "nvim-telescope/telescope.nvim",
    "hrsh7th/nvim-cmp",
  },
  config = function()
    require("marunochiAI").setup()
  end
}
```

## ⚙️ Configuration

```lua
require("marunochiAI").setup({
  -- API Configuration
  api_url = "http://localhost:8765",  -- MarunochiAI server URL
  api_key = nil,                       -- Optional API key
  model = nil,                         -- Auto-select (7b/14b)

  -- Features
  auto_index = true,                   -- Auto-index workspace on startup
  search_limit = 5,                    -- Default search result limit
  enable_completion = true,            -- Enable AI completions
  enable_inline_chat = true,           -- Enable chat features
})
```

## 🚀 Commands

### Code Search

```vim
:MarunochiIndex [path]           " Index codebase (defaults to cwd)
:MarunochiSearch <query>         " Search codebase semantically
:MarunochiStats                  " Show indexing statistics
```

### Chat & Code Assistance

```vim
:MarunochiChat [message]         " Open chat window
:MarunochiExplain                " Explain selected code
:MarunochiRefactor               " Refactor selected code
:MarunochiDebug                  " Debug selected code
```

### Health Check

```vim
:MarunochiHealth                 " Check server health
```

## 🔥 Usage Examples

### Semantic Search with Telescope

```vim
" Search for authentication-related code
:MarunochiSearch user authentication function

" Results appear in Telescope picker with:
" - Similarity scores
" - File paths and line numbers
" - Syntax-highlighted previews
" - Jump to code with <CR>
```

### AI-Powered Completions

MarunochiAI automatically provides completions when typing if `enable_completion = true`:

```lua
-- Type: function calculate
-- MarunochiAI suggests:
function calculate_total(items)
  local sum = 0
  for _, item in ipairs(items) do
    sum = sum + item.price
  end
  return sum
end
```

### Code Explanation

```vim
" Select code in visual mode
:'<,'>MarunochiExplain

" Opens chat window with detailed explanation
```

### Inline Chat

```vim
:MarunochiChat How do I implement a binary search?

" Interactive chat window opens with streaming response
" Press <CR> to continue conversation
" Press q to close
```

## 🎯 Keybindings (Recommended)

Add these to your Neovim config:

```lua
vim.keymap.set('n', '<leader>ms', ':MarunochiSearch ', { desc = 'Search codebase' })
vim.keymap.set('n', '<leader>mi', ':MarunochiIndex<CR>', { desc = 'Index codebase' })
vim.keymap.set('n', '<leader>mc', ':MarunochiChat<CR>', { desc = 'Open chat' })
vim.keymap.set('v', '<leader>me', ':MarunochiExplain<CR>', { desc = 'Explain code' })
vim.keymap.set('v', '<leader>mr', ':MarunochiRefactor<CR>', { desc = 'Refactor code' })
vim.keymap.set('v', '<leader>md', ':MarunochiDebug<CR>', { desc = 'Debug code' })
```

## 🔧 Requirements

- Neovim >= 0.8.0
- `curl` command available
- MarunochiAI server running (`marunochithe server`)
- **Optional**:
  - [telescope.nvim](https://github.com/nvim-telescope/telescope.nvim) - For beautiful search UI
  - [nvim-cmp](https://github.com/hrsh7th/nvim-cmp) - For AI completions

## 🏗️ Architecture

```
┌─────────────────────────────────────┐
│      Neovim (nvim-marunochiAI)      │
│  ┌────────┬─────────┬────────────┐  │
│  │ Search │ Chat    │ Completion │  │
│  └───┬────┴────┬────┴──────┬─────┘  │
│      │         │           │        │
│      └─────────┴───────────┘        │
│              API Client             │
└──────────────┬──────────────────────┘
               │ HTTP/REST
┌──────────────▼──────────────────────┐
│     MarunochiAI Server :8765        │
│  ┌──────────────────────────────┐   │
│  │  Hybrid Search (RRF Fusion)  │   │
│  │  ChromaDB + SQLite FTS5      │   │
│  └──────────────────────────────┘   │
│  ┌──────────────────────────────┐   │
│  │  Ollama (Qwen2.5-Coder)      │   │
│  │  7B/14B Auto-Routing         │   │
│  └──────────────────────────────┘   │
└─────────────────────────────────────┘
```

## 🤝 Integration with BenchAI & DottscavisAI

MarunochiAI works seamlessly as part of a multi-agent system:

- **BenchAI**: Routes complex tasks to MarunochiAI for code understanding
- **DottscavisAI**: Handles creative/multimedia tasks
- **MarunochiAI**: Specializes in code analysis and generation

The plugin automatically benefits from this distributed intelligence when connected to BenchAI.

## 📊 Performance

- **Search latency**: <200ms (hybrid mode)
- **Indexing**: ~45s for 10K files
- **Completion**: <500ms per suggestion
- **Memory**: ~100MB for indexed codebase

## 🐛 Troubleshooting

### Server not responding

```vim
:MarunochiHealth
" Check if server is running: marunochithe server
```

### No search results

```vim
:MarunochiIndex
" Re-index current workspace
```

### Completions not working

Ensure nvim-cmp is installed and MarunochiAI completion source is enabled:

```lua
require('cmp').setup({
  sources = {
    { name = 'marunochiAI' },
    -- other sources...
  }
})
```

## 📝 License

MIT License - See main MarunochiAI repository

## 🙏 Credits

Built with:
- [Neovim](https://neovim.io/)
- [Telescope](https://github.com/nvim-telescope/telescope.nvim)
- [nvim-cmp](https://github.com/hrsh7th/nvim-cmp)
- [MarunochiAI](https://github.com/CesarSalcido06/MarunochiAI)

---

**Made with ❤️ by the MarunochiAI team**
