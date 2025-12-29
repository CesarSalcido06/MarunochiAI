---MarunochiAI Ghost Text - Copilot-style inline completions
---@class MarunochiGhost
local M = {}

local api = require("marunochiAI.api")

-- State
M.enabled = true
M.suggestion = nil
M.suggestion_lines = {}
M.ghost_ns = vim.api.nvim_create_namespace("marunochiAI_ghost")
M.debounce_timer = nil
M.last_request_id = 0

-- Configuration
local config = {
  debounce_ms = 300,
  max_lines = 10,
  trigger_on_insert = true,
}

---Setup ghost text
---@param opts table|nil Configuration options
function M.setup(opts)
  opts = opts or {}
  config = vim.tbl_deep_extend("force", config, opts)

  if config.trigger_on_insert then
    M.setup_autocmds()
  end
end

---Setup autocommands for automatic suggestions
function M.setup_autocmds()
  local group = vim.api.nvim_create_augroup("MarunochiGhost", { clear = true })

  -- Trigger on text change in insert mode
  vim.api.nvim_create_autocmd({ "TextChangedI", "TextChangedP" }, {
    group = group,
    callback = function()
      if M.enabled then
        M.request_suggestion_debounced()
      end
    end,
  })

  -- Clear on leaving insert mode
  vim.api.nvim_create_autocmd("InsertLeave", {
    group = group,
    callback = function()
      M.clear_suggestion()
    end,
  })

  -- Clear on cursor move
  vim.api.nvim_create_autocmd("CursorMovedI", {
    group = group,
    callback = function()
      -- Only clear if we moved to a different line
      if M.suggestion then
        local cursor = vim.api.nvim_win_get_cursor(0)
        if cursor[1] ~= M.suggestion.line then
          M.clear_suggestion()
        end
      end
    end,
  })
end

---Clear current suggestion
function M.clear_suggestion()
  local bufnr = vim.api.nvim_get_current_buf()
  vim.api.nvim_buf_clear_namespace(bufnr, M.ghost_ns, 0, -1)
  M.suggestion = nil
  M.suggestion_lines = {}
end

---Request suggestion with debounce
function M.request_suggestion_debounced()
  if M.debounce_timer then
    vim.fn.timer_stop(M.debounce_timer)
  end

  M.debounce_timer = vim.fn.timer_start(config.debounce_ms, function()
    M.request_suggestion()
  end)
end

---Request a completion suggestion
function M.request_suggestion()
  local bufnr = vim.api.nvim_get_current_buf()
  local cursor = vim.api.nvim_win_get_cursor(0)
  local line = cursor[1]
  local col = cursor[2]

  -- Get context
  local lines = vim.api.nvim_buf_get_lines(bufnr, 0, -1, false)
  local current_line = lines[line] or ""
  local prefix = current_line:sub(1, col)

  -- Don't trigger on empty lines or just whitespace
  if prefix:match("^%s*$") and #lines < 3 then
    return
  end

  -- Build context (lines before cursor)
  local context_start = math.max(1, line - 50)
  local before_lines = vim.list_slice(lines, context_start, line - 1)
  local before_context = table.concat(before_lines, "\n")

  -- Lines after cursor
  local after_start = math.min(line + 1, #lines)
  local after_end = math.min(line + 10, #lines)
  local after_lines = vim.list_slice(lines, after_start, after_end)
  local after_context = table.concat(after_lines, "\n")

  local filetype = vim.api.nvim_buf_get_option(bufnr, "filetype")
  local suffix = current_line:sub(col + 1)

  -- Increment request ID
  M.last_request_id = M.last_request_id + 1
  local request_id = M.last_request_id

  -- Build FIM-style prompt
  local messages = {
    {
      role = "system",
      content = string.format(
        [[You are a code completion assistant for %s.
Complete the code at the cursor position.
Output ONLY the completion text, no explanations.
Be concise - complete the current line or add 1-3 lines max.
No markdown, no backticks.]],
        filetype
      ),
    },
    {
      role = "user",
      content = string.format(
        [[<prefix>
%s
%s</prefix><suffix>%s
%s</suffix>

Complete the code at the cursor (between prefix and suffix):]],
        before_context:sub(-1000),
        prefix,
        suffix,
        after_context:sub(1, 500)
      ),
    },
  }

  api.chat_completion(messages, function(success, response)
    -- Check if this is still the latest request
    if request_id ~= M.last_request_id then
      return
    end

    vim.schedule(function()
      if not success then
        return
      end

      local completion = response.choices[1].message.content

      -- Clean up
      completion = completion:gsub("^```%w*\n?", ""):gsub("\n?```$", ""):gsub("^%s+", "")

      if completion == "" then
        return
      end

      -- Check cursor hasn't moved
      local new_cursor = vim.api.nvim_win_get_cursor(0)
      if new_cursor[1] ~= line then
        return
      end

      -- Store and display suggestion
      M.suggestion = {
        text = completion,
        line = line,
        col = col,
        bufnr = bufnr,
      }
      M.suggestion_lines = vim.split(completion, "\n")

      M.display_suggestion()
    end)
  end)
end

---Display the current suggestion as virtual text
function M.display_suggestion()
  if not M.suggestion then
    return
  end

  local bufnr = M.suggestion.bufnr
  local line = M.suggestion.line

  -- Clear previous
  vim.api.nvim_buf_clear_namespace(bufnr, M.ghost_ns, 0, -1)

  if #M.suggestion_lines == 0 then
    return
  end

  -- First line as inline virtual text
  local first_line = M.suggestion_lines[1]
  vim.api.nvim_buf_set_extmark(bufnr, M.ghost_ns, line - 1, M.suggestion.col, {
    virt_text = { { first_line, "Comment" } },
    virt_text_pos = "inline",
  })

  -- Additional lines as virtual lines below
  if #M.suggestion_lines > 1 then
    local virt_lines = {}
    for i = 2, math.min(#M.suggestion_lines, config.max_lines) do
      table.insert(virt_lines, { { M.suggestion_lines[i], "Comment" } })
    end
    if #virt_lines > 0 then
      vim.api.nvim_buf_set_extmark(bufnr, M.ghost_ns, line - 1, 0, {
        virt_lines = virt_lines,
        virt_lines_above = false,
      })
    end
  end
end

---Accept the current suggestion (Tab)
function M.accept()
  if not M.suggestion then
    -- Fall through to normal Tab behavior
    return false
  end

  local bufnr = M.suggestion.bufnr
  local line = M.suggestion.line
  local col = M.suggestion.col

  -- Insert the suggestion
  local current_line = vim.api.nvim_buf_get_lines(bufnr, line - 1, line, false)[1] or ""
  local prefix = current_line:sub(1, col)
  local suffix = current_line:sub(col + 1)

  -- Build new lines
  local new_lines = {}
  for i, suggestion_line in ipairs(M.suggestion_lines) do
    if i == 1 then
      table.insert(new_lines, prefix .. suggestion_line)
    else
      table.insert(new_lines, suggestion_line)
    end
  end

  -- Add suffix to last line
  if #new_lines > 0 then
    new_lines[#new_lines] = new_lines[#new_lines] .. suffix
  end

  -- Apply
  vim.api.nvim_buf_set_lines(bufnr, line - 1, line, false, new_lines)

  -- Move cursor to end of insertion
  local new_line = line + #new_lines - 1
  local new_col = #new_lines[#new_lines] - #suffix
  vim.api.nvim_win_set_cursor(0, { new_line, new_col })

  -- Clear suggestion
  M.clear_suggestion()

  return true
end

---Accept only the first word of the suggestion
function M.accept_word()
  if not M.suggestion then
    return false
  end

  local first_line = M.suggestion_lines[1] or ""
  local word = first_line:match("^(%S+)") or first_line:match("^(%s+%S+)")

  if not word or word == "" then
    return false
  end

  local bufnr = M.suggestion.bufnr
  local line = M.suggestion.line
  local col = M.suggestion.col

  -- Insert just the word
  local current_line = vim.api.nvim_buf_get_lines(bufnr, line - 1, line, false)[1] or ""
  local new_line = current_line:sub(1, col) .. word .. current_line:sub(col + 1)
  vim.api.nvim_buf_set_lines(bufnr, line - 1, line, false, { new_line })

  -- Move cursor
  vim.api.nvim_win_set_cursor(0, { line, col + #word })

  -- Clear and retrigger
  M.clear_suggestion()
  M.request_suggestion_debounced()

  return true
end

---Dismiss the current suggestion (Esc)
function M.dismiss()
  if M.suggestion then
    M.clear_suggestion()
    return true
  end
  return false
end

---Toggle ghost text on/off
function M.toggle()
  M.enabled = not M.enabled
  if not M.enabled then
    M.clear_suggestion()
  end
  vim.notify("MarunochiAI Ghost Text: " .. (M.enabled and "ON" or "OFF"), vim.log.levels.INFO)
end

---Manually trigger suggestion
function M.trigger()
  M.clear_suggestion()
  M.request_suggestion()
end

return M
