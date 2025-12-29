-- MarunochiAI - Minimal AI Assistant for Neovim
local M = {}

M.config = {
  api_url = "http://localhost:8765",
}

function M.setup(opts)
  M.config = vim.tbl_extend("force", M.config, opts or {})

  -- Setup API
  local api = require("marunochiAI.api")
  api.setup(M.config)

  local chat = require("marunochiAI.chat")

  -- ════════════════════════════════════════════════════════════
  -- KEYMAPS
  -- ════════════════════════════════════════════════════════════

  -- Toggle chat: <leader>ac
  vim.keymap.set("n", "<leader>ac", chat.toggle, { desc = "AI Chat" })

  -- Code actions (visual mode)
  vim.keymap.set("v", "<leader>ae", function()
    M.action("explain")
  end, { desc = "AI Explain" })

  vim.keymap.set("v", "<leader>ar", function()
    M.action("refactor")
  end, { desc = "AI Refactor" })

  vim.keymap.set("v", "<leader>af", function()
    M.action("fix")
  end, { desc = "AI Fix" })

  -- ════════════════════════════════════════════════════════════
  -- COMMANDS
  -- ════════════════════════════════════════════════════════════

  vim.api.nvim_create_user_command("AI", function(cmd)
    if cmd.args == "" then
      chat.toggle()
    else
      chat.open()
      chat.send(cmd.args)
    end
  end, { nargs = "*", desc = "MarunochiAI" })

  vim.notify("MarunochiAI: <leader>ac = chat", vim.log.levels.INFO)
end

-- Perform action on selected code
function M.action(action_type)
  -- Get selection
  local start_line = vim.fn.line("'<")
  local end_line = vim.fn.line("'>")

  if start_line == 0 then
    vim.notify("Select code first", vim.log.levels.WARN)
    return
  end

  local lines = vim.api.nvim_buf_get_lines(0, start_line - 1, end_line, false)
  local code = table.concat(lines, "\n")
  local filetype = vim.bo.filetype

  local prompts = {
    explain = "Explain this code:",
    refactor = "Refactor this code to be cleaner:",
    fix = "Fix any bugs in this code:",
  }

  local chat = require("marunochiAI.chat")
  chat.send_with_code(prompts[action_type] or "Help with:", code, filetype)
end

return M
