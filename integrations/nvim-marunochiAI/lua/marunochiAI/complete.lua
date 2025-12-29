-- MarunochiAI Ghost Completions (Copilot-style)
local M = {}
local api = require("marunochiAI.api")

local ns = vim.api.nvim_create_namespace("marunochiAI_ghost")

local state = {
  enabled = true,
  suggestion = nil,
  timer = nil,
  request_id = 0,
  debounce_ms = 500,
}

-- Clear current suggestion
function M.clear()
  if state.suggestion then
    local bufnr = state.suggestion.bufnr
    if vim.api.nvim_buf_is_valid(bufnr) then
      vim.api.nvim_buf_clear_namespace(bufnr, ns, 0, -1)
    end
    state.suggestion = nil
  end
end

-- Display suggestion as virtual text
local function display_suggestion(bufnr, line, col, text)
  M.clear()

  local lines = vim.split(text, "\n")
  if #lines == 0 or (lines[1] == "" and #lines == 1) then
    return
  end

  state.suggestion = {
    bufnr = bufnr,
    line = line,
    col = col,
    text = text,
    lines = lines,
  }

  -- First line as inline virtual text
  vim.api.nvim_buf_set_extmark(bufnr, ns, line - 1, col, {
    virt_text = { { lines[1], "Comment" } },
    virt_text_pos = "inline",
  })

  -- Additional lines below
  if #lines > 1 then
    local virt_lines = {}
    for i = 2, #lines do
      table.insert(virt_lines, { { lines[i], "Comment" } })
    end
    vim.api.nvim_buf_set_extmark(bufnr, ns, line - 1, 0, {
      virt_lines = virt_lines,
    })
  end
end

-- Request completion
local function request_completion()
  local bufnr = vim.api.nvim_get_current_buf()
  local cursor = vim.api.nvim_win_get_cursor(0)
  local line = cursor[1]
  local col = cursor[2]
  local filetype = vim.bo[bufnr].filetype

  -- Get context
  local lines = vim.api.nvim_buf_get_lines(bufnr, 0, -1, false)
  local current_line = lines[line] or ""
  local prefix = current_line:sub(1, col)

  -- Don't complete on empty/whitespace only
  if prefix:match("^%s*$") and #lines < 5 then
    return
  end

  local before = table.concat(vim.list_slice(lines, math.max(1, line - 30), line - 1), "\n")
  local after = table.concat(vim.list_slice(lines, line + 1, math.min(#lines, line + 10)), "\n")

  state.request_id = state.request_id + 1
  local request_id = state.request_id

  local messages = {
    {
      role = "system",
      content = "Complete the code. Output ONLY the completion (what comes next). "
        .. "No explanations. Be concise (1-3 lines max). No markdown.",
    },
    {
      role = "user",
      content = "Language: " .. filetype .. "\n"
        .. "Context:\n" .. before:sub(-800) .. "\n" .. prefix
        .. "[CURSOR]" .. current_line:sub(col + 1) .. "\n" .. after:sub(1, 300)
        .. "\n\nComplete at [CURSOR]:",
    },
  }

  api.chat(messages, function(success, response)
    -- Ignore if outdated
    if request_id ~= state.request_id then return end
    if not success then return end

    vim.schedule(function()
      -- Check cursor hasn't moved
      local new_cursor = vim.api.nvim_win_get_cursor(0)
      if new_cursor[1] ~= line or new_cursor[2] ~= col then
        return
      end

      local completion = response.choices[1].message.content
      completion = completion:gsub("^```%w*\n?", ""):gsub("\n?```$", ""):gsub("^%s+", "")

      if completion ~= "" then
        display_suggestion(bufnr, line, col, completion)
      end
    end)
  end)
end

-- Accept suggestion (Tab)
function M.accept()
  if not state.suggestion then
    return false
  end

  local s = state.suggestion
  local bufnr = s.bufnr
  local line = s.line
  local col = s.col

  -- Get current line
  local current = vim.api.nvim_buf_get_lines(bufnr, line - 1, line, false)[1] or ""
  local prefix = current:sub(1, col)
  local suffix = current:sub(col + 1)

  -- Build new lines
  local new_lines = {}
  for i, suggestion_line in ipairs(s.lines) do
    if i == 1 then
      table.insert(new_lines, prefix .. suggestion_line)
    else
      table.insert(new_lines, suggestion_line)
    end
  end
  new_lines[#new_lines] = new_lines[#new_lines] .. suffix

  -- Apply
  vim.api.nvim_buf_set_lines(bufnr, line - 1, line, false, new_lines)

  -- Move cursor
  local new_line = line + #new_lines - 1
  local new_col = #new_lines[#new_lines] - #suffix
  vim.api.nvim_win_set_cursor(0, { new_line, new_col })

  M.clear()
  return true
end

-- Dismiss suggestion
function M.dismiss()
  M.clear()
end

-- Toggle on/off
function M.toggle()
  state.enabled = not state.enabled
  if not state.enabled then
    M.clear()
  end
  vim.notify("Ghost completions: " .. (state.enabled and "ON" or "OFF"), vim.log.levels.INFO)
end

-- Trigger manually
function M.trigger()
  M.clear()
  request_completion()
end

-- Setup autocommands
function M.setup()
  local group = vim.api.nvim_create_augroup("MarunochiComplete", { clear = true })

  vim.api.nvim_create_autocmd("TextChangedI", {
    group = group,
    callback = function()
      if not state.enabled then return end

      if state.timer then
        vim.fn.timer_stop(state.timer)
      end

      state.timer = vim.fn.timer_start(state.debounce_ms, function()
        vim.schedule(request_completion)
      end)
    end,
  })

  vim.api.nvim_create_autocmd("InsertLeave", {
    group = group,
    callback = M.clear,
  })

  vim.api.nvim_create_autocmd("CursorMovedI", {
    group = group,
    callback = function()
      if state.suggestion then
        local cursor = vim.api.nvim_win_get_cursor(0)
        if cursor[1] ~= state.suggestion.line then
          M.clear()
        end
      end
    end,
  })
end

return M
