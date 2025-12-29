---MarunochiAI Chat Panel - Unified chat interface
---@class MarunochiChat
local M = {}

local api = require("marunochiAI.api")

-- State
M.history = {}
M.bufnr = nil
M.winnr = nil
M.is_processing = false

-- Configuration
local config = {
  width = 80,
  height = 30,
  position = "float", -- "float" (default), "right", "left"
}

---Create chat buffer
local function create_buffer()
  local buf = vim.api.nvim_create_buf(false, true)
  vim.api.nvim_buf_set_option(buf, "buftype", "nofile")
  vim.api.nvim_buf_set_option(buf, "filetype", "markdown")
  vim.api.nvim_buf_set_option(buf, "swapfile", false)
  vim.api.nvim_buf_set_name(buf, "MarunochiAI")
  return buf
end

---Render chat content
local function render()
  if not M.bufnr or not vim.api.nvim_buf_is_valid(M.bufnr) then
    return
  end

  vim.api.nvim_buf_set_option(M.bufnr, "modifiable", true)

  local lines = {
    "# MarunochiAI Chat",
    "",
  }

  if #M.history == 0 then
    -- Welcome message
    vim.list_extend(lines, {
      "Local AI coding assistant powered by Qwen2.5-Coder.",
      "",
      "**Keybindings:**",
      "- `i` or `a` — Send message",
      "- `yc` — Copy code block",
      "- `<C-y>` — Insert code to editor",
      "- `C` — Clear history",
      "- `q` — Close",
      "",
      "---",
      "",
    })
  else
    -- Chat history
    for _, entry in ipairs(M.history) do
      if entry.role == "user" then
        table.insert(lines, "**You:**")
      else
        table.insert(lines, "**MarunochiAI:**")
      end
      for _, line in ipairs(vim.split(entry.content, "\n")) do
        table.insert(lines, line)
      end
      table.insert(lines, "")
      table.insert(lines, "---")
      table.insert(lines, "")
    end
  end

  -- Input prompt
  if M.is_processing then
    table.insert(lines, "*Thinking...*")
  else
    table.insert(lines, "_Press `i` to send a message_")
  end

  vim.api.nvim_buf_set_lines(M.bufnr, 0, -1, false, lines)
  vim.api.nvim_buf_set_option(M.bufnr, "modifiable", false)

  -- Scroll to bottom
  if M.winnr and vim.api.nvim_win_is_valid(M.winnr) then
    local count = vim.api.nvim_buf_line_count(M.bufnr)
    vim.api.nvim_win_set_cursor(M.winnr, { count, 0 })
  end
end

---Setup keymaps for chat buffer
local function setup_keymaps()
  local opts = { noremap = true, silent = true, buffer = M.bufnr }

  -- Close
  vim.keymap.set("n", "q", M.close, opts)
  vim.keymap.set("n", "<Esc>", M.close, opts)

  -- Send message
  vim.keymap.set("n", "i", M.prompt_input, opts)
  vim.keymap.set("n", "a", M.prompt_input, opts)
  vim.keymap.set("n", "<CR>", M.prompt_input, opts)

  -- Clear history
  vim.keymap.set("n", "C", M.clear, opts)

  -- Copy code block
  vim.keymap.set("n", "yc", M.copy_code_block, opts)

  -- Insert code to editor
  vim.keymap.set("n", "<C-y>", M.insert_code_block, opts)

  -- Scroll
  vim.keymap.set("n", "j", "gj", opts)
  vim.keymap.set("n", "k", "gk", opts)
end

---Open chat panel
---@param initial_message string|nil Initial message to send
function M.open(initial_message)
  -- Focus if already open
  if M.winnr and vim.api.nvim_win_is_valid(M.winnr) then
    vim.api.nvim_set_current_win(M.winnr)
    if initial_message and initial_message ~= "" then
      M.send(initial_message)
    end
    return
  end

  -- Create buffer
  if not M.bufnr or not vim.api.nvim_buf_is_valid(M.bufnr) then
    M.bufnr = create_buffer()
  end

  -- Open as floating window (default - avoids layout conflicts)
  local width = math.min(config.width, vim.o.columns - 8)
  local height = math.min(config.height, vim.o.lines - 8)

  M.winnr = vim.api.nvim_open_win(M.bufnr, true, {
    relative = "editor",
    row = math.floor((vim.o.lines - height) / 2) - 1,
    col = math.floor((vim.o.columns - width) / 2),
    width = width,
    height = height,
    style = "minimal",
    border = "rounded",
    title = " MarunochiAI ",
    title_pos = "center",
  })

  -- Window options
  vim.wo[M.winnr].wrap = true
  vim.wo[M.winnr].linebreak = true
  vim.wo[M.winnr].number = false
  vim.wo[M.winnr].relativenumber = false
  vim.wo[M.winnr].signcolumn = "no"
  vim.wo[M.winnr].spell = false
  vim.wo[M.winnr].conceallevel = 2

  setup_keymaps()
  render()

  if initial_message and initial_message ~= "" then
    vim.schedule(function()
      M.send(initial_message)
    end)
  end
end

---Alias for open
function M.open_chat(msg)
  M.open(msg)
end

---Close chat panel
function M.close()
  if M.winnr and vim.api.nvim_win_is_valid(M.winnr) then
    vim.api.nvim_win_close(M.winnr, true)
  end
  M.winnr = nil
end

---Toggle chat panel
function M.toggle()
  if M.winnr and vim.api.nvim_win_is_valid(M.winnr) then
    M.close()
  else
    M.open()
  end
end

---Alias for toggle
function M.toggle_chat()
  M.toggle()
end

---Prompt for input
function M.prompt_input()
  if M.is_processing then
    vim.notify("MarunochiAI is thinking...", vim.log.levels.WARN)
    return
  end

  vim.ui.input({ prompt = "Message: " }, function(input)
    if input and input ~= "" then
      M.send(input)
    end
  end)
end

---Send message to AI
---@param message string Message to send
function M.send(message)
  if M.is_processing then
    return
  end

  M.is_processing = true

  -- Get context from editor
  local context = M.get_editor_context()
  local full_message = message

  if context.selection then
    full_message = string.format(
      "[Code from %s]\n```%s\n%s\n```\n\n%s",
      context.filename or "buffer",
      context.filetype or "",
      context.selection,
      message
    )
  end

  -- Add to history
  table.insert(M.history, { role = "user", content = full_message })
  render()

  -- Stream response
  local response = ""

  api.chat_completion_stream(M.history, function(token)
    response = response .. token
    -- Update display periodically
    vim.schedule(function()
      if M.bufnr and vim.api.nvim_buf_is_valid(M.bufnr) then
        vim.api.nvim_buf_set_option(M.bufnr, "modifiable", true)
        local lines = vim.api.nvim_buf_get_lines(M.bufnr, 0, -1, false)
        -- Update last section with streaming response
        local last_sep = #lines
        for i = #lines, 1, -1 do
          if lines[i] == "---" then
            last_sep = i
            break
          end
        end
        -- Replace from last separator
        local new_lines = { "---", "", "**MarunochiAI:**" }
        for _, line in ipairs(vim.split(response, "\n")) do
          table.insert(new_lines, line)
        end
        table.insert(new_lines, "")
        table.insert(new_lines, "_streaming..._")
        vim.api.nvim_buf_set_lines(M.bufnr, last_sep - 1, -1, false, new_lines)
        vim.api.nvim_buf_set_option(M.bufnr, "modifiable", false)

        -- Scroll
        if M.winnr and vim.api.nvim_win_is_valid(M.winnr) then
          local count = vim.api.nvim_buf_line_count(M.bufnr)
          vim.api.nvim_win_set_cursor(M.winnr, { count, 0 })
        end
      end
    end)
  end, function()
    -- Done
    M.is_processing = false
    table.insert(M.history, { role = "assistant", content = response })
    vim.schedule(function()
      render()
    end)
  end)
end

---Get context from the editor
---@return table Context
function M.get_editor_context()
  local ctx = {}

  for _, win in ipairs(vim.api.nvim_list_wins()) do
    local buf = vim.api.nvim_win_get_buf(win)
    local name = vim.api.nvim_buf_get_name(buf)

    if not name:match("MarunochiAI") then
      ctx.filename = vim.fn.fnamemodify(name, ":t")
      ctx.filetype = vim.api.nvim_buf_get_option(buf, "filetype")

      -- Check for visual selection marks
      local start_line = vim.fn.line("'<")
      local end_line = vim.fn.line("'>")

      if start_line > 0 and end_line > 0 and start_line <= end_line then
        local lines = vim.api.nvim_buf_get_lines(buf, start_line - 1, end_line, false)
        if #lines > 0 then
          ctx.selection = table.concat(lines, "\n")
        end
      end
      break
    end
  end

  return ctx
end

---Clear chat history
function M.clear()
  M.history = {}
  render()
  vim.notify("Chat cleared", vim.log.levels.INFO)
end

---Find code block at cursor
---@return string|nil Code block content
local function find_code_block_at_cursor()
  if not M.winnr or not vim.api.nvim_win_is_valid(M.winnr) then
    return nil
  end

  local cursor = vim.api.nvim_win_get_cursor(M.winnr)
  local lines = vim.api.nvim_buf_get_lines(M.bufnr, 0, -1, false)

  local in_block = false
  local block_start = nil
  local block_lines = {}

  for i, line in ipairs(lines) do
    if line:match("^```") then
      if in_block then
        -- End of block
        if cursor[1] >= block_start and cursor[1] <= i then
          return table.concat(block_lines, "\n")
        end
        in_block = false
        block_lines = {}
      else
        -- Start of block
        in_block = true
        block_start = i
      end
    elseif in_block then
      table.insert(block_lines, line)
    end
  end

  return nil
end

---Copy code block under cursor
function M.copy_code_block()
  local code = find_code_block_at_cursor()
  if code then
    vim.fn.setreg("+", code)
    vim.notify("Code copied", vim.log.levels.INFO)
  else
    vim.notify("No code block at cursor", vim.log.levels.WARN)
  end
end

---Insert code block into editor
function M.insert_code_block()
  local code = find_code_block_at_cursor()
  if not code then
    vim.notify("No code block at cursor", vim.log.levels.WARN)
    return
  end

  -- Find editor window
  for _, win in ipairs(vim.api.nvim_list_wins()) do
    local buf = vim.api.nvim_win_get_buf(win)
    local name = vim.api.nvim_buf_get_name(buf)

    if not name:match("MarunochiAI") then
      -- Switch to that window and insert
      vim.api.nvim_set_current_win(win)
      local cursor = vim.api.nvim_win_get_cursor(win)
      local lines = vim.split(code, "\n")
      vim.api.nvim_buf_set_lines(buf, cursor[1], cursor[1], false, lines)
      vim.notify("Code inserted", vim.log.levels.INFO)
      return
    end
  end

  vim.notify("No editor window found", vim.log.levels.WARN)
end

-- Legacy aliases for backwards compatibility
M.explain_selection = function()
  local inline = require("marunochiAI.inline")
  inline.quick_action("explain")
end

M.refactor_selection = function()
  local inline = require("marunochiAI.inline")
  inline.quick_action("refactor")
end

M.debug_selection = function()
  local inline = require("marunochiAI.inline")
  inline.quick_action("fix")
end

M.generate_tests = function()
  local inline = require("marunochiAI.inline")
  inline.quick_action("test")
end

return M
