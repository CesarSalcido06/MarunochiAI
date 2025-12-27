---MarunochiAI completion source for nvim-cmp
---@class MarunochiCompletion
local M = {}

local api = require("marunochiAI.api")

---Setup completion source
function M.setup()
  -- Try to register with nvim-cmp
  local has_cmp, cmp = pcall(require, "cmp")
  if not has_cmp then
    vim.notify("nvim-cmp not found, completion disabled", vim.log.levels.WARN)
    return
  end

  local source = {}

  ---Get completion items
  ---@param params table
  ---@param callback function
  function source:complete(params, callback)
    local cursor = params.context.cursor
    local line = params.context.cursor_line
    local before_cursor = line:sub(1, cursor.col - 1)

    -- Get file context
    local bufnr = vim.api.nvim_get_current_buf()
    local lines = vim.api.nvim_buf_get_lines(bufnr, 0, -1, false)
    local context = table.concat(lines, "\n")

    -- Build prompt for AI
    local messages = {
      {
        role = "system",
        content = "You are a code completion assistant. Provide concise, accurate code completions based on context.",
      },
      {
        role = "user",
        content = string.format(
          "Complete the following code:\n\n%s\n\nCursor is after: %s",
          context,
          before_cursor
        ),
      },
    }

    -- Request completion from MarunochiAI
    api.chat_completion(messages, function(success, response)
      if not success then
        callback({ items = {}, isIncomplete = false })
        return
      end

      local completion_text = response.choices[1].message.content

      -- Parse completion text into items
      local items = {}
      for line_text in completion_text:gmatch("[^\r\n]+") do
        if line_text ~= "" and not line_text:match("^%s*$") then
          table.insert(items, {
            label = line_text,
            kind = cmp.lsp.CompletionItemKind.Text,
            documentation = "AI-powered completion from MarunochiAI",
          })
        end
      end

      callback({ items = items, isIncomplete = false })
    end)
  end

  ---Get trigger characters
  function source:get_trigger_characters()
    return { ".", ":", "(", "[", "{", " " }
  end

  ---Check if source is available
  function source:is_available()
    return true
  end

  ---Get source name
  function source:get_debug_name()
    return "marunochiAI"
  end

  -- Register source with cmp
  cmp.register_source("marunochiAI", source)

  -- Add to sources if not already there
  local config = cmp.get_config()
  local sources = config.sources or {}
  local found = false
  for _, s in ipairs(sources) do
    if s.name == "marunochiAI" then
      found = true
      break
    end
  end

  if not found then
    table.insert(sources, { name = "marunochiAI", priority = 100 })
    cmp.setup({ sources = sources })
  end

  vim.notify("MarunochiAI completion source registered", vim.log.levels.INFO)
end

return M
