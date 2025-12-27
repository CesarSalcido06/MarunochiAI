---@class MarunochiAI
---@field config MarunochiConfig
local M = {}

---@class MarunochiConfig
---@field api_url string Base URL for MarunochiAI API
---@field api_key string|nil Optional API key for authentication
---@field model string|nil Model to use (7b, 14b, custom)
---@field auto_index boolean Auto-index workspace on startup
---@field search_limit number Default search result limit
---@field enable_completion boolean Enable AI-powered completion
---@field enable_inline_chat boolean Enable inline chat
local default_config = {
  api_url = "http://localhost:8765",
  api_key = nil,
  model = nil, -- Auto-select
  auto_index = true,
  search_limit = 5,
  enable_completion = true,
  enable_inline_chat = true,
}

M.config = default_config

---Setup MarunochiAI plugin
---@param opts MarunochiConfig|nil User configuration
function M.setup(opts)
  M.config = vim.tbl_deep_extend("force", default_config, opts or {})

  -- Load submodules
  local api = require("marunochiAI.api")
  local search = require("marunochiAI.search")
  local completion = require("marunochiAI.completion")
  local chat = require("marunochiAI.chat")

  -- Initialize API client
  api.setup(M.config)

  -- Create user commands
  vim.api.nvim_create_user_command("MarunochiIndex", function(cmd_opts)
    local path = cmd_opts.args ~= "" and cmd_opts.args or vim.fn.getcwd()
    search.index_codebase(path, true)
  end, {
    nargs = "?",
    desc = "Index current workspace for semantic search",
  })

  vim.api.nvim_create_user_command("MarunochiSearch", function(cmd_opts)
    if cmd_opts.args == "" then
      vim.notify("Usage: :MarunochiSearch <query>", vim.log.levels.ERROR)
      return
    end
    search.search_codebase(cmd_opts.args)
  end, {
    nargs = "+",
    desc = "Search codebase semantically",
  })

  vim.api.nvim_create_user_command("MarunochiChat", function(cmd_opts)
    chat.open_chat(cmd_opts.args)
  end, {
    nargs = "*",
    desc = "Open chat with MarunochiAI",
  })

  vim.api.nvim_create_user_command("MarunochiExplain", function()
    chat.explain_selection()
  end, {
    range = true,
    desc = "Explain selected code",
  })

  vim.api.nvim_create_user_command("MarunochiRefactor", function()
    chat.refactor_selection()
  end, {
    range = true,
    desc = "Refactor selected code",
  })

  vim.api.nvim_create_user_command("MarunochiDebug", function()
    chat.debug_selection()
  end, {
    range = true,
    desc = "Debug selected code",
  })

  -- Setup completion if enabled
  if M.config.enable_completion then
    completion.setup()
  end

  -- Auto-index workspace
  if M.config.auto_index then
    vim.defer_fn(function()
      local cwd = vim.fn.getcwd()
      search.index_codebase(cwd, false)
    end, 1000) -- Delay 1 second after startup
  end

  vim.notify("MarunochiAI loaded", vim.log.levels.INFO)
end

---Get current configuration
---@return MarunochiConfig
function M.get_config()
  return M.config
end

return M
