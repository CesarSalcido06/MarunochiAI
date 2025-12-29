# nvim-marunochiAI

Cursor/Copilot-style AI coding assistant for Neovim, powered by local LLMs.

## Features

- **Inline Edit** (`Ctrl+I`) - Edit selection or generate code at cursor (like Cursor's Cmd+K)
- **Ghost Text** - Copilot-style completions as you type (Tab to accept)
- **Chat Panel** (`Ctrl+L`) - Sidebar chat with streaming responses
- **Quick Actions** - Explain, refactor, fix, document, test selection
- **Semantic Search** - Find code by natural language

## Installation

### LazyVim

Add to `lua/plugins/marunochiAI.lua`:

```lua
return {
  {
    dir = "~/MarunochiAI/integrations/nvim-marunochiAI",
    name = "marunochiAI",
    dependencies = {
      "nvim-telescope/telescope.nvim",  -- Optional: for search UI
    },
    config = function()
      require("marunochiAI").setup({
        api_url = "http://localhost:8765",
        ghost_text = true,
        ghost_debounce = 300,
      })
    end,
    lazy = false,
  },
}
```

### lazy.nvim (Standard)

```lua
{
  dir = "~/MarunochiAI/integrations/nvim-marunochiAI",
  config = function()
    require("marunochiAI").setup()
  end,
}
```

### packer.nvim

```lua
use {
  '~/MarunochiAI/integrations/nvim-marunochiAI',
  config = function()
    require('marunochiAI').setup()
  end
}
```

## Keybindings

### Core

| Key | Mode | Action |
|-----|------|--------|
| `<leader>ai` | Normal/Visual | **Inline edit** - Edit selection or generate at cursor |
| `<leader>ac` | Normal | **Toggle chat** panel (floating window) |
| `Tab` | Insert | **Accept** ghost completion |
| `Ctrl+Right` | Insert | Accept word only |
| `Ctrl+]` | Insert | Dismiss suggestion |
| `Ctrl+Space` | Insert | Trigger suggestion manually |
| `<leader>ag` | Normal | Toggle ghost text on/off |

### Quick Actions (Visual Mode)

| Key | Action |
|-----|--------|
| `<leader>ae` | Explain selection |
| `<leader>ar` | Refactor selection |
| `<leader>af` | Fix/debug selection |
| `<leader>ad` | Add documentation |
| `<leader>at` | Generate tests |

### Chat Panel

| Key | Action |
|-----|--------|
| `i` / `a` / `Enter` | Send message |
| `yc` | Copy code block |
| `Ctrl+y` | Insert code to editor |
| `C` | Clear history |
| `q` / `Esc` | Close chat |

## Commands

```vim
:MarunochiChat [message]  " Toggle chat / send message
:MarunochiEdit            " Inline edit (same as Ctrl+I)
:MarunochiExplain         " Explain selected code
:MarunochiRefactor        " Refactor selection
:MarunochiDebug           " Fix/debug selection
:MarunochiTests           " Generate tests
:MarunochiSearch [query]  " Semantic code search
:MarunochiIndex [path]    " Index codebase
:MarunochiGhost           " Toggle ghost text
```

## Configuration

```lua
require("marunochiAI").setup({
  -- API
  api_url = "http://localhost:8765",
  api_key = nil,        -- Optional
  model = nil,          -- nil=auto, "7b", "14b"

  -- Features
  ghost_text = true,    -- Copilot-style completions
  ghost_debounce = 300, -- Debounce ms
  auto_index = false,   -- Index on startup

  -- Keymaps (set to false to disable any)
  keymaps = {
    inline_edit = "<leader>ai",  -- Inline edit
    toggle_chat = "<leader>ac",  -- Chat panel
    accept_completion = "<Tab>",
    accept_word = "<C-Right>",
    dismiss = "<C-]>",
    trigger = "<C-Space>",
    explain = "<leader>ae",
    refactor = "<leader>ar",
    fix = "<leader>af",
    document = "<leader>ad",
    test = "<leader>at",
  },
})
```

## Workflow

### 1. Ghost Text (Copilot-style)

As you type, completions appear as gray ghost text:

```
function calculate|  -- cursor here
         _total(items)  -- ghost suggestion
```

Press **Tab** to accept, **Ctrl+]** to dismiss.

### 2. Inline Edit (Cursor-style)

Select code and press **`<leader>ai`**:

```
1. Select code (or cursor on line)
2. Press <leader>ai
3. Type instruction: "add error handling"
4. Accept/Preview/Cancel
```

### 3. Chat Panel

Press **`<leader>ac`** to open chat (floating window):

```
# MarunochiAI Chat

**You:**
How do I implement binary search?

**MarunochiAI:**
Here's an efficient binary search...
```

### 4. Quick Actions

Select code in visual mode, then:
- `<leader>ae` - Explain what it does
- `<leader>ar` - Refactor it
- `<leader>af` - Fix bugs
- `<leader>ad` - Add docs
- `<leader>at` - Generate tests

## Requirements

- Neovim >= 0.8.0
- MarunochiAI server running
- `curl` (for HTTP requests)

## Server Setup

```bash
# Install
cd ~/MarunochiAI
pip install -e .

# Download model
ollama pull qwen2.5-coder:7b

# Start server
marunochithe server
```

## Architecture

```
┌─────────────────────────────────────┐
│     Neovim (nvim-marunochiAI)       │
│  ┌────────┬────────┬─────────────┐  │
│  │ Ghost  │ Inline │    Chat     │  │
│  │  Text  │  Edit  │   Panel     │  │
│  └────────┴────────┴─────────────┘  │
│           API Client (curl)         │
└──────────────┬──────────────────────┘
               │ HTTP/REST
┌──────────────▼──────────────────────┐
│    MarunochiAI Server :8765         │
│  ┌──────────────────────────────┐   │
│  │  Ollama (Qwen2.5-Coder)      │   │
│  │  7B fast / 14B powerful      │   │
│  └──────────────────────────────┘   │
└─────────────────────────────────────┘
```

## Troubleshooting

### Ghost text not appearing
```vim
:MarunochiGhost  " Check if enabled
" Ensure server is running: marunochithe server
```

### Completions slow
```lua
-- Increase debounce
require("marunochiAI").setup({
  ghost_debounce = 500,  -- 500ms
})
```

### Server not responding
```bash
# Check server
curl http://localhost:8765/health

# Start server
marunochithe server
```

## License

MIT

---

**Local AI, private, fast, free.**
