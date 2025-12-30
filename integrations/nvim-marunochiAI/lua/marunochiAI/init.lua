-- MarunochiAI - Ultimate Coding Assistant for Neovim
-- Cursor/Copilot-style AI experience
local M = {}

M.config = {
  api_url = "http://localhost:8765",
  ghost_text = true,  -- Enable Copilot-style completions
}

function M.setup(opts)
  M.config = vim.tbl_extend("force", M.config, opts or {})

  -- Initialize modules
  local api = require("marunochiAI.api")
  local chat = require("marunochiAI.chat")
  local edit = require("marunochiAI.edit")
  local complete = require("marunochiAI.complete")
  local search = require("marunochiAI.search")

  api.setup(M.config)
  search.setup()

  -- Setup ghost completions
  if M.config.ghost_text then
    complete.setup()
  end

  -- ══════════════════════════════════════════════════════════════════
  -- KEYBINDINGS (Cursor/Copilot style)
  -- ══════════════════════════════════════════════════════════════════

  -- Chat sidebar: <leader>ac (like Cursor's Cmd+L)
  vim.keymap.set("n", "<leader>ac", chat.toggle, { desc = "AI: Chat" })

  -- Inline edit: <leader>ae (like Cursor's Cmd+K)
  vim.keymap.set("v", "<leader>ae", function()
    vim.cmd("normal! ")  -- Exit visual mode
    edit.edit_selection()
  end, { desc = "AI: Edit selection" })

  -- Generate at cursor: <leader>ag
  vim.keymap.set("n", "<leader>ag", edit.generate_at_cursor, { desc = "AI: Generate" })

  -- Accept ghost completion: Tab
  vim.keymap.set("i", "<Tab>", function()
    if complete.accept() then
      return ""  -- Consumed
    end
    return vim.api.nvim_replace_termcodes("<Tab>", true, false, true)
  end, { expr = true, desc = "AI: Accept completion" })

  -- Dismiss ghost completion: Ctrl+]
  vim.keymap.set("i", "<C-]>", complete.dismiss, { desc = "AI: Dismiss" })

  -- Manual trigger: Ctrl+Space
  vim.keymap.set("i", "<C-Space>", complete.trigger, { desc = "AI: Trigger completion" })

  -- Toggle ghost text: <leader>at
  vim.keymap.set("n", "<leader>at", complete.toggle, { desc = "AI: Toggle completions" })

  -- Semantic search: <leader>as
  vim.keymap.set("n", "<leader>as", search.search, { desc = "AI: Search codebase" })
  vim.keymap.set("n", "<leader>aS", search.search_context, { desc = "AI: Search word under cursor" })

  -- Index project: <leader>ai
  vim.keymap.set("n", "<leader>ai", function() search.index_project() end, { desc = "AI: Index project" })

  -- Code actions
  vim.keymap.set("v", "<leader>ax", function()
    vim.cmd("normal! ")
    local s = vim.fn.line("'<")
    local e = vim.fn.line("'>")
    local lines = vim.api.nvim_buf_get_lines(0, s - 1, e, false)
    local code = table.concat(lines, "\n")
    chat.ask_about_code("Explain this code:", code, vim.bo.filetype)
  end, { desc = "AI: Explain" })

  vim.keymap.set("v", "<leader>ar", function()
    vim.cmd("normal! ")
    local s = vim.fn.line("'<")
    local e = vim.fn.line("'>")
    local lines = vim.api.nvim_buf_get_lines(0, s - 1, e, false)
    local code = table.concat(lines, "\n")
    chat.ask_about_code("Refactor this code:", code, vim.bo.filetype)
  end, { desc = "AI: Refactor" })

  vim.keymap.set("v", "<leader>af", function()
    vim.cmd("normal! ")
    local s = vim.fn.line("'<")
    local e = vim.fn.line("'>")
    local lines = vim.api.nvim_buf_get_lines(0, s - 1, e, false)
    local code = table.concat(lines, "\n")
    chat.ask_about_code("Fix bugs in this code:", code, vim.bo.filetype)
  end, { desc = "AI: Fix" })

  -- ══════════════════════════════════════════════════════════════════
  -- COMMANDS
  -- ══════════════════════════════════════════════════════════════════

  vim.api.nvim_create_user_command("AI", function(cmd)
    if cmd.args == "" then
      chat.toggle()
    else
      chat.open()
      chat.send(cmd.args)
    end
  end, { nargs = "*", desc = "MarunochiAI Chat" })

  vim.api.nvim_create_user_command("AIEdit", function()
    edit.edit_selection()
  end, { range = true, desc = "Edit with AI" })

  vim.api.nvim_create_user_command("AIGenerate", function()
    edit.generate_at_cursor()
  end, { desc = "Generate with AI" })

  -- ══════════════════════════════════════════════════════════════════

  vim.notify("MarunochiAI ready | <leader>ac=Chat | <leader>as=Search | Tab=Accept", vim.log.levels.INFO)
end

return M
