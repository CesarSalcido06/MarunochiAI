-- MarunochiAI Semantic Code Search
local M = {}
local api = require("marunochiAI.api")

local state = {
  results_buf = nil,
  results_win = nil,
  results = {},
  indexed = false,
}

-- Index the current project
function M.index_project(path)
  path = path or vim.fn.getcwd()

  vim.notify("MarunochiAI: Indexing " .. path .. "...", vim.log.levels.INFO)

  local url = api.config.api_url .. "/v1/codebase/index?codebase_path=" .. vim.fn.fnameescape(path) .. "&watch=false"

  local cmd = { "curl", "-s", "-X", "POST", url }

  vim.fn.jobstart(cmd, {
    stdout_buffered = true,
    on_stdout = function(_, data)
      if data and data[1] ~= "" then
        local raw = table.concat(data, "")
        local ok, result = pcall(vim.fn.json_decode, raw)
        if ok and result then
          state.indexed = true
          local msg = string.format(
            "Indexed %d files, %d chunks in %dms",
            result.successful_files or 0,
            result.indexed_chunks or 0,
            result.duration_ms or 0
          )
          vim.schedule(function()
            vim.notify("MarunochiAI: " .. msg, vim.log.levels.INFO)
          end)
        else
          vim.schedule(function()
            vim.notify("MarunochiAI: Indexing failed", vim.log.levels.ERROR)
          end)
        end
      end
    end,
    on_stderr = function(_, data)
      if data and data[1] ~= "" then
        vim.schedule(function()
          vim.notify("MarunochiAI: " .. table.concat(data, ""), vim.log.levels.ERROR)
        end)
      end
    end,
  })
end

-- Get stats about the index
function M.stats()
  local url = api.config.api_url .. "/v1/codebase/stats"

  vim.fn.jobstart({ "curl", "-s", url }, {
    stdout_buffered = true,
    on_stdout = function(_, data)
      if data and data[1] ~= "" then
        local raw = table.concat(data, "")
        local ok, result = pcall(vim.fn.json_decode, raw)
        if ok and result then
          local vector = result.vector or {}
          local msg = string.format(
            "Index: %d chunks, %d files | Fusion: %s",
            vector.total_chunks or 0,
            vector.total_files or 0,
            result.fusion_enabled and "enabled" or "disabled"
          )
          vim.schedule(function()
            vim.notify("MarunochiAI: " .. msg, vim.log.levels.INFO)
          end)
        end
      end
    end,
  })
end

-- Close results window
local function close_results()
  if state.results_win and vim.api.nvim_win_is_valid(state.results_win) then
    vim.api.nvim_win_close(state.results_win, true)
  end
  state.results_win = nil
  state.results_buf = nil
end

-- Open file at specific line from search result
local function open_result(index)
  local result = state.results[index]
  if not result then return end

  close_results()

  -- Open the file
  vim.cmd("edit " .. vim.fn.fnameescape(result.filepath))

  -- Go to line
  local line = result.line_start or 1
  vim.api.nvim_win_set_cursor(0, { line, 0 })

  -- Center the view
  vim.cmd("normal! zz")
end

-- Display search results in floating window
local function display_results(query, results)
  close_results()

  state.results = results

  -- Create buffer
  state.results_buf = vim.api.nvim_create_buf(false, true)
  vim.bo[state.results_buf].buftype = "nofile"
  vim.bo[state.results_buf].bufhidden = "wipe"
  vim.bo[state.results_buf].filetype = "markdown"

  -- Build content
  local lines = {
    "# Search Results: " .. query,
    "",
    string.format("Found %d results", #results),
    "",
    "Press number (1-9) to open, q/Esc to close",
    "",
    "---",
    "",
  }

  for i, result in ipairs(results) do
    local meta = result.metadata or {}
    local filepath = result.filepath or "unknown"
    local name = meta.name or "unnamed"
    local chunk_type = meta.chunk_type or "code"
    local language = meta.language or "unknown"
    local line_range = meta.line_range or { 0, 0 }
    local similarity = result.similarity or 0

    -- Shorten filepath
    local short_path = filepath:gsub(vim.fn.getcwd() .. "/", "")

    table.insert(lines, string.format("## %d. %s (%s)", i, name, chunk_type))
    table.insert(lines, string.format("**File:** `%s:%d-%d`", short_path, line_range[1], line_range[2]))
    table.insert(lines, string.format("**Language:** %s | **Score:** %.3f", language, similarity))
    table.insert(lines, "")
    table.insert(lines, "```" .. language)

    -- Show content preview (first 10 lines)
    local content = result.content or ""
    local content_lines = vim.split(content, "\n")
    for j, line in ipairs(content_lines) do
      if j <= 10 then
        table.insert(lines, line)
      end
    end
    if #content_lines > 10 then
      table.insert(lines, "... (" .. (#content_lines - 10) .. " more lines)")
    end

    table.insert(lines, "```")
    table.insert(lines, "")

    -- Store line info for opening
    state.results[i].line_start = line_range[1]
  end

  vim.api.nvim_buf_set_lines(state.results_buf, 0, -1, false, lines)
  vim.bo[state.results_buf].modifiable = false

  -- Calculate window size
  local width = math.min(100, math.floor(vim.o.columns * 0.8))
  local height = math.min(40, math.floor(vim.o.lines * 0.8))

  -- Open floating window
  state.results_win = vim.api.nvim_open_win(state.results_buf, true, {
    relative = "editor",
    width = width,
    height = height,
    row = math.floor((vim.o.lines - height) / 2),
    col = math.floor((vim.o.columns - width) / 2),
    style = "minimal",
    border = "rounded",
    title = " Semantic Search ",
    title_pos = "center",
  })
  vim.wo[state.results_win].wrap = true

  -- Keymaps for results window
  local opts = { buffer = state.results_buf, silent = true, nowait = true }

  vim.keymap.set("n", "q", close_results, opts)
  vim.keymap.set("n", "<Esc>", close_results, opts)

  -- Number keys to open results
  for i = 1, 9 do
    vim.keymap.set("n", tostring(i), function()
      open_result(i)
    end, opts)
  end

  -- Enter on line opens closest result
  vim.keymap.set("n", "<CR>", function()
    local cursor = vim.api.nvim_win_get_cursor(state.results_win)
    local line = cursor[1]
    -- Find which result section we're in
    for i = #state.results, 1, -1 do
      if line > (8 + (i - 1) * 15) then
        open_result(i)
        return
      end
    end
    open_result(1)
  end, opts)
end

-- Perform semantic search
function M.search(query)
  if not query or query == "" then
    vim.ui.input({ prompt = "Search codebase: " }, function(input)
      if input and input ~= "" then
        M.search(input)
      end
    end)
    return
  end

  vim.notify("MarunochiAI: Searching...", vim.log.levels.INFO)

  local url = api.config.api_url .. "/v1/codebase/search"
  local payload = vim.fn.json_encode({
    query = query,
    limit = 5,
  })

  -- Use temp file for payload (handles escaping)
  local temp_file = vim.fn.tempname()
  local f = io.open(temp_file, "w")
  if f then
    f:write(payload)
    f:close()
  end

  local cmd = {
    "curl", "-s", "-X", "POST", url,
    "-H", "Content-Type: application/json",
    "-d", "@" .. temp_file,
  }

  vim.fn.jobstart(cmd, {
    stdout_buffered = true,
    on_stdout = function(_, data)
      os.remove(temp_file)
      if data and data[1] ~= "" then
        local raw = table.concat(data, "")
        local ok, result = pcall(vim.fn.json_decode, raw)
        if ok and result and result.results then
          vim.schedule(function()
            if #result.results == 0 then
              vim.notify("MarunochiAI: No results found", vim.log.levels.WARN)
            else
              display_results(query, result.results)
            end
          end)
        else
          vim.schedule(function()
            vim.notify("MarunochiAI: Search failed - " .. raw:sub(1, 100), vim.log.levels.ERROR)
          end)
        end
      end
    end,
    on_exit = function(_, code)
      if code ~= 0 then
        os.remove(temp_file)
        vim.schedule(function()
          vim.notify("MarunochiAI: Search request failed", vim.log.levels.ERROR)
        end)
      end
    end,
  })
end

-- Search with context from current file
function M.search_context()
  -- Get current word under cursor or visual selection
  local query = vim.fn.expand("<cword>")

  if query == "" then
    M.search()
  else
    M.search(query)
  end
end

-- Setup keymaps and commands
function M.setup()
  -- Commands
  vim.api.nvim_create_user_command("AISearch", function(opts)
    M.search(opts.args)
  end, { nargs = "?" })

  vim.api.nvim_create_user_command("AIIndex", function(opts)
    M.index_project(opts.args ~= "" and opts.args or nil)
  end, { nargs = "?" })

  vim.api.nvim_create_user_command("AIStats", function()
    M.stats()
  end, {})
end

return M
