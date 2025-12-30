-- MarunochiAI Ghost Completions (Copilot-style)
local M = {}
local api = require("marunochiAI.api")

local ns = vim.api.nvim_create_namespace("marunochiAI_ghost")

local state = {
  enabled = true,
  suggestion = nil,
  timer = nil,
  request_id = 0,
  debounce_ms = 200,  -- Reduced from 500ms for faster response
  -- Cache for recent completions
  cache = {},
  cache_ttl = 30000,  -- 30 seconds TTL
  -- Confidence threshold (0.0 - 1.0)
  min_confidence = 0.5,
}

-- Calculate confidence score for a completion (heuristic-based)
local function calculate_confidence(completion, prefix, suffix, filetype)
  local score = 0.7  -- Base confidence

  -- Penalize very short completions (likely incomplete)
  if #completion < 3 then
    score = score - 0.3
  elseif #completion > 500 then
    -- Very long completions may be hallucinations
    score = score - 0.2
  end

  -- Boost if completion matches common patterns
  local ends_well = completion:match("[;%}%)%]\"']%s*$")
    or completion:match(":%s*$")  -- Python
    or completion:match("end%s*$")  -- Lua
    or completion:match("fi%s*$")  -- Bash
  if ends_well then
    score = score + 0.15
  end

  -- Penalize if completion repeats the prefix (model echoing)
  if prefix:len() > 5 and completion:find(prefix:sub(-10), 1, true) then
    score = score - 0.4
  end

  -- Boost single-line completions (usually more accurate)
  local line_count = select(2, completion:gsub("\n", "\n")) + 1
  if line_count == 1 then
    score = score + 0.1
  elseif line_count > 5 then
    score = score - 0.1
  end

  -- Clamp to 0.0 - 1.0
  return math.max(0.0, math.min(1.0, score))
end

-- Determine if we should request multi-line or single-line completion
local function should_multiline(prefix, suffix, filetype)
  -- If at end of line and line ends with opening brace/paren, expect multi-line
  if suffix:match("^%s*$") then
    if prefix:match("[%{%(%[]%s*$") then
      return true, 5  -- Multi-line, up to 5 lines
    end
    if prefix:match(":%s*$") and (filetype == "python" or filetype == "yaml") then
      return true, 5
    end
    if prefix:match("then%s*$") or prefix:match("do%s*$") then
      return true, 3  -- Lua/shell blocks
    end
  end

  -- If there's content after cursor, single line is safer
  if #suffix > 0 and not suffix:match("^%s*$") then
    return false, 1
  end

  -- Default: allow up to 3 lines
  return false, 3
end

-- Generate cache key from context
local function get_cache_key(prefix, suffix)
  -- Use hash of prefix (last 200 chars) + suffix (first 100 chars)
  local key_content = prefix:sub(-200) .. "|||" .. suffix:sub(1, 100)
  -- Simple hash using string.byte sum
  local hash = 0
  for i = 1, #key_content do
    hash = (hash * 31 + string.byte(key_content, i)) % 2147483647
  end
  return tostring(hash)
end

-- Check cache for completion
local function get_cached(key)
  local entry = state.cache[key]
  if entry then
    local age = vim.loop.now() - entry.timestamp
    if age < state.cache_ttl then
      return entry.completion
    else
      -- Expired, remove it
      state.cache[key] = nil
    end
  end
  return nil
end

-- Store completion in cache
local function set_cached(key, completion)
  state.cache[key] = {
    completion = completion,
    timestamp = vim.loop.now(),
  }
  -- Cleanup old entries (keep max 50)
  local count = 0
  local oldest_key, oldest_time = nil, math.huge
  for k, v in pairs(state.cache) do
    count = count + 1
    if v.timestamp < oldest_time then
      oldest_key = k
      oldest_time = v.timestamp
    end
  end
  if count > 50 and oldest_key then
    state.cache[oldest_key] = nil
  end
end

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

-- Request completion with FIM format and caching
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

  -- Don't complete on empty/whitespace only (unless file has content)
  if prefix:match("^%s*$") and #lines < 5 then
    return
  end

  -- Build context before and after cursor
  local before_lines = vim.list_slice(lines, math.max(1, line - 30), line - 1)
  local after_lines = vim.list_slice(lines, line + 1, math.min(#lines, line + 10))

  local before = table.concat(before_lines, "\n")
  local suffix = current_line:sub(col + 1)
  local after = table.concat(after_lines, "\n")

  -- Full prefix includes lines before + current line prefix
  local full_prefix = before
  if #before > 0 then
    full_prefix = full_prefix .. "\n"
  end
  full_prefix = full_prefix .. prefix

  -- Full suffix includes rest of line + lines after
  local full_suffix = suffix
  if #after > 0 then
    full_suffix = full_suffix .. "\n" .. after
  end

  -- Check cache first
  local cache_key = get_cache_key(full_prefix, full_suffix)
  local cached = get_cached(cache_key)
  if cached then
    display_suggestion(bufnr, line, col, cached)
    return
  end

  state.request_id = state.request_id + 1
  local request_id = state.request_id

  -- Determine completion style based on context
  local is_multiline, max_lines = should_multiline(prefix, full_suffix, filetype)
  local line_hint = is_multiline
    and string.format("Complete the block (up to %d lines).", max_lines)
    or string.format("Complete this line (up to %d lines max).", max_lines)

  -- Use FIM (Fill-in-Middle) style prompt for better completions
  local messages = {
    {
      role = "system",
      content = "You are a code completion engine. Complete the code at the <CURSOR> position. "
        .. "Output ONLY the completion text that should be inserted. "
        .. "No explanations, no markdown, no backticks. " .. line_hint,
    },
    {
      role = "user",
      content = string.format(
        "Language: %s\n\n<PREFIX>\n%s<CURSOR>%s\n<SUFFIX>\n\nComplete at <CURSOR>:",
        filetype,
        full_prefix:sub(-1000),  -- Last 1000 chars of prefix
        full_suffix:sub(1, 500)  -- First 500 chars of suffix
      ),
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
      -- Clean up common artifacts
      completion = completion:gsub("^```%w*\n?", ""):gsub("\n?```$", "")
      completion = completion:gsub("^%s+", "")  -- Trim leading whitespace
      completion = completion:gsub("<CURSOR>", "")  -- Remove cursor marker if echoed
      completion = completion:gsub("<PREFIX>", ""):gsub("<SUFFIX>", "")

      -- Truncate to max_lines if needed
      local comp_lines = vim.split(completion, "\n")
      if #comp_lines > max_lines then
        comp_lines = vim.list_slice(comp_lines, 1, max_lines)
        completion = table.concat(comp_lines, "\n")
      end

      if completion ~= "" then
        -- Check confidence before showing
        local confidence = calculate_confidence(completion, prefix, full_suffix, filetype)

        if confidence >= state.min_confidence then
          -- Cache the result
          set_cached(cache_key, completion)
          display_suggestion(bufnr, line, col, completion)
        end
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
