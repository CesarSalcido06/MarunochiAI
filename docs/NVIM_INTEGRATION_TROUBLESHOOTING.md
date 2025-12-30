# Neovim Integration Troubleshooting Log

**Date:** December 29, 2025
**Status:** RESOLVED - All features working

## Summary

Successfully debugged and fixed the MarunochiAI Neovim plugin to work seamlessly with LazyVim. The plugin now provides Cursor/Copilot-style AI assistance with:
- Floating chat panel
- Ghost completions (inline suggestions)
- Code actions (explain, refactor, fix)

---

## Issues Found & Resolved

### Issue 1: Plugin Config Mismatch

**Problem:** The `~/.config/nvim/lua/plugins/marunochiAI.lua` config referenced commands that didn't exist in the actual plugin.

**Expected (config):**
```lua
{ "<leader>mc", "<cmd>MarunochiToggle<cr>" }
{ "<leader>ma", "<cmd>MarunochiChat<cr>" }
```

**Actual (plugin):**
```lua
vim.api.nvim_create_user_command("AI", ...)
vim.api.nvim_create_user_command("AIEdit", ...)
```

**Fix:** Updated the plugin config to match actual commands and removed invalid keybindings.

---

### Issue 2: LazyVim Layout Conflicts

**Problem:** Opening chat with `botright vnew` and `belowright split` triggered LazyVim's file explorer and created unwanted windows (two folder panels on left, empty rectangle at bottom).

**Root Cause:** LazyVim intercepts `vnew` commands and applies its own window management.

**Fix:** Rewrote `chat.lua` to use **floating windows** via `nvim_open_win()` instead of splits:
```lua
state.chat_win = vim.api.nvim_open_win(chat_buf, false, {
  relative = "editor",
  width = WIDTH,
  height = chat_height,
  row = 0,
  col = editor_width - WIDTH - 1,
  style = "minimal",
  border = "rounded",
  title = " Chat ",
  title_pos = "center",
})
```

---

### Issue 3: Keybinding Conflicts

**Problem:** Both BenchAI and MarunochiAI plugins used `<leader>a*` keybindings:
- `<leader>ae` - BenchAI (Explain) vs MarunochiAI (Edit)
- `<leader>ar` - BenchAI (Improve) vs MarunochiAI (Refactor)
- `<leader>af` - BenchAI (Fix) vs MarunochiAI (Fix)

**Fix:** Disabled BenchAI keybindings. MarunochiAI owns `<leader>a*`, BenchAI accessible via `:BenchAI` command.

---

### Issue 4: Streaming JSON Format Error

**Problem:** AI responses weren't appearing in chat. The server's streaming endpoint returned Python dict repr instead of JSON:

**Broken (Python repr):**
```
data: {'id': 'xxx', 'choices': [{'delta': {'content': 'Hello'}, 'finish_reason': None}]}
```

**Expected (JSON):**
```
data: {"id": "xxx", "choices": [{"delta": {"content": "Hello"}, "finish_reason": null}]}
```

**Root Cause:** Server used f-string formatting instead of `json.dumps()`:
```python
# BROKEN
yield f"data: {chunk_data}\n\n"

# FIXED
yield f"data: {json.dumps(chunk_data)}\n\n"
```

**Fix:**
1. Updated `server.py` to use `json.dumps()` for all streaming chunks
2. Added fallback Python→JSON converter in `api.lua` for robustness

---

### Issue 5: Double Response Bug

**Problem:** Each message received two AI responses.

**Root Cause:** The `on_done` callback was firing twice:
1. When `[DONE]` token received in `on_stdout`
2. When curl process exited in `on_exit`

**Fix:** Added guards in both `api.lua` and `chat.lua`:
```lua
-- api.lua
local state = { done = false }
if state.done then return end
state.done = true

-- chat.lua
local response_added = false
if response_added then return end
response_added = true
```

---

### Issue 6: LazyVim Plugin Order Warning

**Problem:** Warning on startup about lazy.nvim import order.

**Fix:** Added to `lazy.lua`:
```lua
vim.g.lazyvim_check_order = false
```

---

### Issue 7: BenchAI Plugin Structure

**Problem:** `benchai.lua` had unusual structure mixing module code with plugin spec, causing lazy.nvim issues.

**Fix:** Rewrote as clean lazy.nvim plugin with proper structure.

---

## Files Modified

### MarunochiAI Repository
1. **`integrations/nvim-marunochiAI/lua/marunochiAI/chat.lua`**
   - Complete rewrite using floating windows
   - LazyVim compatible layout

2. **`integrations/nvim-marunochiAI/lua/marunochiAI/api.lua`**
   - Added Python→JSON converter fallback
   - Fixed double callback issue with state tracking
   - Added proper whitespace trimming for `[DONE]` detection

3. **`marunochithe/api/server.py`**
   - Added `import json`
   - Changed streaming to use `json.dumps()` for proper JSON output

### User Neovim Config (~/.config/nvim/)
1. **`lua/plugins/marunochiAI.lua`** - Fixed to match actual plugin commands
2. **`lua/plugins/benchai.lua`** - Simplified structure, disabled keybindings
3. **`lua/config/lazy.lua`** - Disabled false positive order warning

---

## Current Working Features

| Feature | Keybinding | Status |
|---------|------------|--------|
| Chat Panel | `<leader>ac` | Working |
| Edit Selection | `<leader>ae` (visual) | Working |
| Generate Code | `<leader>ag` | Working |
| Explain Code | `<leader>ax` (visual) | Working |
| Refactor Code | `<leader>ar` (visual) | Working |
| Fix Bugs | `<leader>af` (visual) | Working |
| Ghost Completions | Auto (500ms debounce) | Working |
| Accept Completion | `Tab` | Working |
| Dismiss Completion | `Ctrl+]` | Working |
| Trigger Completion | `Ctrl+Space` | Working |
| Toggle Completions | `<leader>at` | Working |

---

## Lessons Learned

1. **LazyVim Compatibility:** Always use floating windows for custom UI panels to avoid conflicts with LazyVim's window management.

2. **JSON Serialization:** Never use Python f-strings with dicts for API responses. Always use `json.dumps()`.

3. **Async Callbacks:** When using jobstart with both `on_stdout` and `on_exit`, guard against double execution with state flags.

4. **Plugin Structure:** lazy.nvim plugin files should return a clean spec table, not mix module code with the return.

5. **Keybinding Namespaces:** Plan keybinding prefixes across all plugins to avoid conflicts.

---

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                      Neovim                              │
│  ┌─────────────────────────────────────────────────┐    │
│  │            MarunochiAI Plugin                    │    │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────────────┐   │    │
│  │  │ chat.lua│ │edit.lua │ │ complete.lua    │   │    │
│  │  │(floating│ │(inline  │ │ (ghost text)    │   │    │
│  │  │ panel)  │ │ edits)  │ │                 │   │    │
│  │  └────┬────┘ └────┬────┘ └────────┬────────┘   │    │
│  │       └───────────┼───────────────┘            │    │
│  │                   ▼                            │    │
│  │             ┌──────────┐                       │    │
│  │             │ api.lua  │                       │    │
│  │             │ (curl)   │                       │    │
│  │             └────┬─────┘                       │    │
│  └──────────────────┼──────────────────────────────┘    │
└─────────────────────┼───────────────────────────────────┘
                      │ HTTP
                      ▼
┌─────────────────────────────────────────────────────────┐
│              MarunochiAI Server (8765)                  │
│  ┌─────────────────────────────────────────────────┐    │
│  │              FastAPI + Streaming                 │    │
│  │                    │                            │    │
│  │                    ▼                            │    │
│  │    ┌──────────────────────────────────┐        │    │
│  │    │  Ollama (qwen2.5-coder:7b/14b)   │        │    │
│  │    └──────────────────────────────────┘        │    │
│  └─────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────┘
```

---

## Testing Checklist

- [x] Server health check: `curl http://localhost:8765/health`
- [x] Non-streaming API: Returns proper JSON
- [x] Streaming API: Returns proper JSON with `json.dumps()`
- [x] Chat panel opens without layout issues
- [x] Messages send and receive correctly
- [x] Single response (no duplicates)
- [x] Ghost completions appear after typing
- [x] Tab accepts completions
- [x] No LazyVim warnings on startup
