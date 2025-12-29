# MarunochiAI for Neovim

Ultimate Cursor/Copilot-style AI coding assistant for Neovim.

## Features

- **Chat Sidebar** - Right-side panel like Cursor's Cmd+L
- **Inline Edit** - Modify code in place like Cursor's Cmd+K
- **Ghost Completions** - Copilot-style suggestions as you type
- **Code Actions** - Explain, refactor, fix with AI

## Installation (LazyVim)

Add to `lua/plugins/ai.lua`:

```lua
return {
  {
    dir = "~/MarunochiAI/integrations/nvim-marunochiAI",
    config = function()
      require("marunochiAI").setup({
        api_url = "http://localhost:8765",
        ghost_text = true,
      })
    end,
  },
}
```

## Keybindings

### Chat
| Key | Mode | Action |
|-----|------|--------|
| `<leader>ac` | Normal | Toggle chat sidebar |

### Inline Edit
| Key | Mode | Action |
|-----|------|--------|
| `<leader>ae` | Visual | Edit selected code with AI |
| `<leader>ag` | Normal | Generate code at cursor |

### Ghost Completions
| Key | Mode | Action |
|-----|------|--------|
| `Tab` | Insert | Accept suggestion |
| `Ctrl+]` | Insert | Dismiss suggestion |
| `Ctrl+Space` | Insert | Trigger manually |
| `<leader>at` | Normal | Toggle on/off |

### Code Actions
| Key | Mode | Action |
|-----|------|--------|
| `<leader>ax` | Visual | Explain selection |
| `<leader>ar` | Visual | Refactor selection |
| `<leader>af` | Visual | Fix selection |

## Commands

```vim
:AI              " Toggle chat
:AI <message>    " Send message
:AIEdit          " Edit selection
:AIGenerate      " Generate at cursor
```

## Workflow

### 1. Chat Sidebar
Press `<leader>ac` to open the chat panel on the right. Type your message in the input box at the bottom and press Enter.

### 2. Inline Edit (Cursor Cmd+K style)
1. Select code in visual mode
2. Press `<leader>ae`
3. Type instruction (e.g., "add error handling")
4. AI modifies code in place

### 3. Ghost Completions (Copilot style)
As you type, suggestions appear in gray. Press `Tab` to accept.

### 4. Code Actions
Select code, then:
- `<leader>ax` - Get explanation in chat
- `<leader>ar` - Get refactoring suggestions
- `<leader>af` - Get bug fixes

## Requirements

- Neovim 0.8+
- MarunochiAI server running

```bash
cd ~/MarunochiAI
pip install -e .
marunochithe server
```

## Architecture

```
┌─────────────────────┬──────────────────┐
│                     │  Chat Sidebar    │
│   Your Code         │  ─────────────── │
│                     │  You: ...        │
│   [ghost text]      │  AI: ...         │
│                     │  ─────────────── │
│                     │  [input box]     │
└─────────────────────┴──────────────────┘
```
