# MarunochiAI for Neovim

Minimal AI coding assistant for Neovim.

## Installation (LazyVim)

Add to `lua/plugins/ai.lua`:

```lua
return {
  {
    dir = "~/MarunochiAI/integrations/nvim-marunochiAI",
    config = function()
      require("marunochiAI").setup({
        api_url = "http://localhost:8765",
      })
    end,
  },
}
```

## Usage

### Chat

Press **`<leader>ac`** to open chat (floating window).

In chat:
- `i` or `Enter` - Type message
- `q` or `Esc` - Close
- `C` - Clear history

### Code Actions

Select code in visual mode, then:
- `<leader>ae` - Explain
- `<leader>ar` - Refactor
- `<leader>af` - Fix

### Command

```vim
:AI              " Open chat
:AI hello        " Send message
```

## Requirements

- Neovim 0.8+
- MarunochiAI server running

```bash
cd ~/MarunochiAI
pip install -e .
marunochithe server
```
