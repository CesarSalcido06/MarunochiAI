---@class MarunochiAI
---@field config MarunochiConfig
---Cursor/Copilot-style AI coding assistant for Neovim
local M = {}

---@class MarunochiConfig
---@field api_url string Base URL for MarunochiAI API
---@field api_key string|nil Optional API key
---@field model string|nil Model to use (auto, 7b, 14b)
---@field auto_index boolean Auto-index workspace on startup
---@field ghost_text boolean Enable ghost text completions
---@field ghost_debounce number Ghost text debounce in ms
---@field keymaps MarunochiKeymaps Keymap configuration
local default_config = {
  api_url = "http://localhost:8765",
  api_key = nil,
  model = nil, -- Auto-select
  auto_index = false,
  ghost_text = true,
  ghost_debounce = 300,
  keymaps = {
    -- Inline edit (like Cursor Cmd+K / Copilot Cmd+I)
    inline_edit = "<C-i>",
    -- Toggle chat panel (like Cursor Cmd+L)
    toggle_chat = "<C-l>",
    -- Accept ghost completion
    accept_completion = "<Tab>",
    -- Accept word
    accept_word = "<C-Right>",
    -- Dismiss suggestion
    dismiss = "<C-]>",
    -- Trigger suggestion manually
    trigger = "<C-Space>",
    -- Quick actions (visual mode)
    explain = "<leader>ae",
    refactor = "<leader>ar",
    fix = "<leader>af",
    document = "<leader>ad",
    test = "<leader>at",
  },
}

M.config = default_config

---Setup MarunochiAI plugin
---@param opts MarunochiConfig|nil User configuration
function M.setup(opts)
  M.config = vim.tbl_deep_extend("force", default_config, opts or {})

  -- Load modules
  local api = require("marunochiAI.api")
  local chat = require("marunochiAI.chat")
  local inline = require("marunochiAI.inline")
  local ghost = require("marunochiAI.ghost")
  local search = require("marunochiAI.search")

  -- Initialize API
  api.setup(M.config)

  -- Setup ghost text
  if M.config.ghost_text then
    ghost.setup({
      debounce_ms = M.config.ghost_debounce,
      trigger_on_insert = true,
    })
  end

  -- ═══════════════════════════════════════════════════════════════════
  -- KEYMAPS (Cursor/Copilot style)
  -- ═══════════════════════════════════════════════════════════════════

  local km = M.config.keymaps

  -- Inline Edit: Ctrl+I (like Cursor's Cmd+K)
  -- Works in normal mode (edit current line) and visual mode (edit selection)
  vim.keymap.set({ "n", "v" }, km.inline_edit, function()
    inline.start_inline_edit()
  end, { desc = "MarunochiAI: Inline Edit" })

  -- Toggle Chat: Ctrl+L (like Cursor's Cmd+L)
  vim.keymap.set("n", km.toggle_chat, function()
    chat.toggle_chat()
  end, { desc = "MarunochiAI: Toggle Chat" })

  -- Ghost Text: Tab to accept
  vim.keymap.set("i", km.accept_completion, function()
    if not ghost.accept() then
      -- Fall back to normal tab
      return vim.api.nvim_replace_termcodes("<Tab>", true, false, true)
    end
  end, { expr = true, desc = "MarunochiAI: Accept Completion" })

  -- Ghost Text: Ctrl+Right to accept word
  vim.keymap.set("i", km.accept_word, function()
    ghost.accept_word()
  end, { desc = "MarunochiAI: Accept Word" })

  -- Ghost Text: Dismiss
  vim.keymap.set("i", km.dismiss, function()
    ghost.dismiss()
  end, { desc = "MarunochiAI: Dismiss Suggestion" })

  -- Ghost Text: Manual trigger
  vim.keymap.set("i", km.trigger, function()
    ghost.trigger()
  end, { desc = "MarunochiAI: Trigger Suggestion" })

  -- Toggle ghost text
  vim.keymap.set("n", "<leader>ag", function()
    ghost.toggle()
  end, { desc = "MarunochiAI: Toggle Ghost Text" })

  -- ═══════════════════════════════════════════════════════════════════
  -- QUICK ACTIONS (Visual Mode)
  -- ═══════════════════════════════════════════════════════════════════

  vim.keymap.set("v", km.explain, function()
    vim.cmd("normal! ")
    inline.quick_action("explain")
  end, { desc = "MarunochiAI: Explain Selection" })

  vim.keymap.set("v", km.refactor, function()
    vim.cmd("normal! ")
    inline.quick_action("refactor")
  end, { desc = "MarunochiAI: Refactor Selection" })

  vim.keymap.set("v", km.fix, function()
    vim.cmd("normal! ")
    inline.quick_action("fix")
  end, { desc = "MarunochiAI: Fix Selection" })

  vim.keymap.set("v", km.document, function()
    vim.cmd("normal! ")
    inline.quick_action("document")
  end, { desc = "MarunochiAI: Document Selection" })

  vim.keymap.set("v", km.test, function()
    vim.cmd("normal! ")
    inline.quick_action("test")
  end, { desc = "MarunochiAI: Generate Tests" })

  -- ═══════════════════════════════════════════════════════════════════
  -- USER COMMANDS
  -- ═══════════════════════════════════════════════════════════════════

  -- Main chat command
  vim.api.nvim_create_user_command("MarunochiChat", function(cmd_opts)
    if cmd_opts.args ~= "" then
      chat.open_chat(cmd_opts.args)
    else
      chat.toggle_chat()
    end
  end, { nargs = "*", desc = "Open MarunochiAI chat" })

  -- Inline edit command
  vim.api.nvim_create_user_command("MarunochiEdit", function()
    inline.start_inline_edit()
  end, { range = true, desc = "Inline edit with AI" })

  -- Quick actions
  vim.api.nvim_create_user_command("MarunochiExplain", function()
    inline.quick_action("explain")
  end, { range = true, desc = "Explain selected code" })

  vim.api.nvim_create_user_command("MarunochiRefactor", function()
    inline.quick_action("refactor")
  end, { range = true, desc = "Refactor selected code" })

  vim.api.nvim_create_user_command("MarunochiDebug", function()
    inline.quick_action("fix")
  end, { range = true, desc = "Fix/debug selected code" })

  vim.api.nvim_create_user_command("MarunochiTests", function()
    inline.quick_action("test")
  end, { range = true, desc = "Generate tests for selection" })

  -- Search
  vim.api.nvim_create_user_command("MarunochiSearch", function(cmd_opts)
    if cmd_opts.args == "" then
      vim.ui.input({ prompt = "Search: " }, function(query)
        if query and query ~= "" then
          search.search_codebase(query)
        end
      end)
    else
      search.search_codebase(cmd_opts.args)
    end
  end, { nargs = "*", desc = "Semantic code search" })

  -- Index
  vim.api.nvim_create_user_command("MarunochiIndex", function(cmd_opts)
    local path = cmd_opts.args ~= "" and cmd_opts.args or vim.fn.getcwd()
    search.index_codebase(path, true)
  end, { nargs = "?", desc = "Index codebase" })

  -- Ghost text toggle
  vim.api.nvim_create_user_command("MarunochiGhost", function()
    ghost.toggle()
  end, { desc = "Toggle ghost text completions" })

  -- ═══════════════════════════════════════════════════════════════════
  -- AUTO-INDEX (optional)
  -- ═══════════════════════════════════════════════════════════════════

  if M.config.auto_index then
    vim.defer_fn(function()
      search.index_codebase(vim.fn.getcwd(), false)
    end, 2000)
  end

  -- ═══════════════════════════════════════════════════════════════════
  -- NOTIFY
  -- ═══════════════════════════════════════════════════════════════════

  vim.notify("MarunochiAI loaded | Ctrl+I: Edit | Ctrl+L: Chat | Tab: Accept", vim.log.levels.INFO)
end

---Get configuration
---@return MarunochiConfig
function M.get_config()
  return M.config
end

return M
