-- MarunochiAI Chat - Simple floating window
local M = {}
local api = require("marunochiAI.api")

-- State
local state = {
  buf = nil,
  win = nil,
  history = {},
  busy = false,
}

-- Create or get chat buffer
local function get_buffer()
  if state.buf and vim.api.nvim_buf_is_valid(state.buf) then
    return state.buf
  end

  state.buf = vim.api.nvim_create_buf(false, true)
  vim.bo[state.buf].buftype = "nofile"
  vim.bo[state.buf].bufhidden = "hide"
  vim.bo[state.buf].swapfile = false
  vim.bo[state.buf].filetype = "markdown"

  return state.buf
end

-- Render chat content
local function render()
  if not state.buf or not vim.api.nvim_buf_is_valid(state.buf) then
    return
  end

  vim.bo[state.buf].modifiable = true

  local lines = { "# MarunochiAI", "" }

  if #state.history == 0 then
    table.insert(lines, "Type your message and press Enter.")
    table.insert(lines, "")
    table.insert(lines, "Keybindings:")
    table.insert(lines, "  i     - Type message")
    table.insert(lines, "  q     - Close")
    table.insert(lines, "  C     - Clear history")
  else
    for _, msg in ipairs(state.history) do
      if msg.role == "user" then
        table.insert(lines, "**You:** " .. msg.content)
      else
        table.insert(lines, "")
        table.insert(lines, "**AI:**")
        for _, line in ipairs(vim.split(msg.content, "\n")) do
          table.insert(lines, line)
        end
      end
      table.insert(lines, "")
      table.insert(lines, "---")
      table.insert(lines, "")
    end
  end

  if state.busy then
    table.insert(lines, "_Thinking..._")
  end

  vim.api.nvim_buf_set_lines(state.buf, 0, -1, false, lines)
  vim.bo[state.buf].modifiable = false

  -- Scroll to bottom
  if state.win and vim.api.nvim_win_is_valid(state.win) then
    vim.api.nvim_win_set_cursor(state.win, { #lines, 0 })
  end
end

-- Open chat window
function M.open()
  -- Already open? Focus it
  if state.win and vim.api.nvim_win_is_valid(state.win) then
    vim.api.nvim_set_current_win(state.win)
    return
  end

  local buf = get_buffer()

  -- Calculate size
  local width = math.min(80, vim.o.columns - 10)
  local height = math.min(25, vim.o.lines - 10)
  local row = math.floor((vim.o.lines - height) / 2)
  local col = math.floor((vim.o.columns - width) / 2)

  -- Open floating window
  state.win = vim.api.nvim_open_win(buf, true, {
    relative = "editor",
    width = width,
    height = height,
    row = row,
    col = col,
    style = "minimal",
    border = "rounded",
    title = " MarunochiAI ",
    title_pos = "center",
  })

  -- Window options
  vim.wo[state.win].wrap = true
  vim.wo[state.win].linebreak = true
  vim.wo[state.win].cursorline = false

  -- Keymaps
  local opts = { buffer = buf, silent = true }
  vim.keymap.set("n", "q", M.close, opts)
  vim.keymap.set("n", "<Esc>", M.close, opts)
  vim.keymap.set("n", "i", M.input, opts)
  vim.keymap.set("n", "a", M.input, opts)
  vim.keymap.set("n", "<CR>", M.input, opts)
  vim.keymap.set("n", "C", M.clear, opts)

  render()
end

-- Close chat window
function M.close()
  if state.win and vim.api.nvim_win_is_valid(state.win) then
    vim.api.nvim_win_close(state.win, true)
  end
  state.win = nil
end

-- Toggle chat
function M.toggle()
  if state.win and vim.api.nvim_win_is_valid(state.win) then
    M.close()
  else
    M.open()
  end
end

-- Get user input and send
function M.input()
  if state.busy then
    vim.notify("Still processing...", vim.log.levels.WARN)
    return
  end

  vim.ui.input({ prompt = "You: " }, function(input)
    if input and input ~= "" then
      M.send(input)
    end
  end)
end

-- Send message
function M.send(message)
  if state.busy then return end

  state.busy = true
  table.insert(state.history, { role = "user", content = message })
  render()

  local response = ""

  api.chat_stream(state.history, function(token)
    response = response .. token
    -- Update display
    vim.schedule(function()
      if state.buf and vim.api.nvim_buf_is_valid(state.buf) then
        vim.bo[state.buf].modifiable = true
        local lines = vim.api.nvim_buf_get_lines(state.buf, 0, -1, false)
        -- Update last line with streaming response
        lines[#lines] = response:gsub("\n", " "):sub(1, 100) .. "..."
        vim.api.nvim_buf_set_lines(state.buf, 0, -1, false, lines)
        vim.bo[state.buf].modifiable = false
      end
    end)
  end, function()
    state.busy = false
    table.insert(state.history, { role = "assistant", content = response })
    vim.schedule(render)
  end)
end

-- Clear history
function M.clear()
  state.history = {}
  render()
  vim.notify("Chat cleared", vim.log.levels.INFO)
end

-- Send with context (for code actions)
function M.send_with_code(prompt, code, filetype)
  local message = string.format("%s\n\n```%s\n%s\n```", prompt, filetype or "", code)
  M.open()
  M.send(message)
end

return M
