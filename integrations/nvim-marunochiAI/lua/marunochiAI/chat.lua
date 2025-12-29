-- MarunochiAI Chat Sidebar (Cursor-style)
local M = {}
local api = require("marunochiAI.api")

local state = {
  buf = nil,
  win = nil,
  input_buf = nil,
  input_win = nil,
  history = {},
  busy = false,
  width = 60,
}

-- Create chat buffer
local function create_chat_buffer()
  if state.buf and vim.api.nvim_buf_is_valid(state.buf) then
    return state.buf
  end

  state.buf = vim.api.nvim_create_buf(false, true)
  vim.bo[state.buf].buftype = "nofile"
  vim.bo[state.buf].bufhidden = "hide"
  vim.bo[state.buf].swapfile = false
  vim.bo[state.buf].filetype = "markdown"
  vim.api.nvim_buf_set_name(state.buf, "MarunochiAI")

  return state.buf
end

-- Render chat
local function render()
  if not state.buf or not vim.api.nvim_buf_is_valid(state.buf) then return end

  vim.bo[state.buf].modifiable = true

  local lines = {}

  for _, msg in ipairs(state.history) do
    if msg.role == "user" then
      table.insert(lines, "━━━ You ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
      for _, l in ipairs(vim.split(msg.content, "\n")) do
        table.insert(lines, l)
      end
    else
      table.insert(lines, "━━━ AI ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
      for _, l in ipairs(vim.split(msg.content, "\n")) do
        table.insert(lines, l)
      end
    end
    table.insert(lines, "")
  end

  if #lines == 0 then
    lines = {
      "MarunochiAI",
      "",
      "Type in the input box below and press Enter.",
      "",
      "Keybindings:",
      "  <CR>  Send message",
      "  q     Close panel",
      "",
    }
  end

  if state.busy then
    table.insert(lines, "")
    table.insert(lines, "▌ Thinking...")
  end

  vim.api.nvim_buf_set_lines(state.buf, 0, -1, false, lines)
  vim.bo[state.buf].modifiable = false

  -- Scroll to bottom
  if state.win and vim.api.nvim_win_is_valid(state.win) then
    vim.api.nvim_win_set_cursor(state.win, { #lines, 0 })
  end
end

-- Open sidebar on the right
function M.open()
  if state.win and vim.api.nvim_win_is_valid(state.win) then
    vim.api.nvim_set_current_win(state.input_win or state.win)
    return
  end

  -- Save current window
  local current_win = vim.api.nvim_get_current_win()

  -- Create buffer
  create_chat_buffer()

  -- Create input buffer
  state.input_buf = vim.api.nvim_create_buf(false, true)
  vim.bo[state.input_buf].buftype = "nofile"
  vim.bo[state.input_buf].swapfile = false

  -- Open vertical split on the far right
  vim.cmd("botright vnew")
  state.win = vim.api.nvim_get_current_win()
  vim.api.nvim_win_set_buf(state.win, state.buf)
  vim.api.nvim_win_set_width(state.win, state.width)

  -- Window options for chat display
  vim.wo[state.win].wrap = true
  vim.wo[state.win].linebreak = true
  vim.wo[state.win].number = false
  vim.wo[state.win].relativenumber = false
  vim.wo[state.win].signcolumn = "no"
  vim.wo[state.win].winfixwidth = true
  vim.wo[state.win].statusline = " MarunochiAI Chat"

  -- Create input area at bottom (horizontal split within our vertical split)
  vim.cmd("belowright split")
  state.input_win = vim.api.nvim_get_current_win()
  vim.api.nvim_win_set_buf(state.input_win, state.input_buf)
  vim.api.nvim_win_set_height(state.input_win, 3)

  -- Input window options
  vim.wo[state.input_win].wrap = true
  vim.wo[state.input_win].number = false
  vim.wo[state.input_win].relativenumber = false
  vim.wo[state.input_win].signcolumn = "no"
  vim.wo[state.input_win].winfixheight = true
  vim.wo[state.input_win].statusline = " Type message, Enter to send"

  -- Input keymaps
  local opts = { buffer = state.input_buf, silent = true }

  vim.keymap.set("n", "<CR>", function() M.send_input() end, opts)
  vim.keymap.set("i", "<CR>", function()
    vim.cmd("stopinsert")
    M.send_input()
  end, opts)
  vim.keymap.set({"n", "i"}, "q", function()
    vim.cmd("stopinsert")
    M.close()
  end, opts)
  vim.keymap.set("n", "<Esc>", function() M.close() end, opts)

  -- Chat buffer keymaps
  local chat_opts = { buffer = state.buf, silent = true }
  vim.keymap.set("n", "q", function() M.close() end, chat_opts)
  vim.keymap.set("n", "<Esc>", function() M.close() end, chat_opts)
  vim.keymap.set("n", "i", function()
    if state.input_win and vim.api.nvim_win_is_valid(state.input_win) then
      vim.api.nvim_set_current_win(state.input_win)
      vim.cmd("startinsert")
    end
  end, chat_opts)

  render()

  -- Focus input and start insert mode
  vim.api.nvim_set_current_win(state.input_win)
  vim.cmd("startinsert")
end

-- Close sidebar
function M.close()
  if state.input_win and vim.api.nvim_win_is_valid(state.input_win) then
    vim.api.nvim_win_close(state.input_win, true)
  end
  if state.win and vim.api.nvim_win_is_valid(state.win) then
    vim.api.nvim_win_close(state.win, true)
  end
  state.win = nil
  state.input_win = nil
end

-- Toggle sidebar
function M.toggle()
  if state.win and vim.api.nvim_win_is_valid(state.win) then
    M.close()
  else
    M.open()
  end
end

-- Send from input buffer
function M.send_input()
  if state.busy then
    vim.notify("Still processing...", vim.log.levels.WARN)
    return
  end

  if not state.input_buf or not vim.api.nvim_buf_is_valid(state.input_buf) then
    return
  end

  local lines = vim.api.nvim_buf_get_lines(state.input_buf, 0, -1, false)
  local message = table.concat(lines, "\n"):gsub("^%s+", ""):gsub("%s+$", "")

  if message == "" then return end

  -- Clear input
  vim.api.nvim_buf_set_lines(state.input_buf, 0, -1, false, {""})

  M.send(message)
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
  end, function()
    state.busy = false
    table.insert(state.history, { role = "assistant", content = response })
    vim.schedule(render)
  end)
end

-- Send with code context
function M.ask_about_code(prompt, code, filetype)
  local message = prompt .. "\n\n```" .. (filetype or "") .. "\n" .. code .. "\n```"
  M.open()
  M.send(message)
end

-- Clear history
function M.clear()
  state.history = {}
  render()
end

return M
