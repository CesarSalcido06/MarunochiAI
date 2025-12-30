-- MarunochiAI Chat Panel (Floating Window - LazyVim compatible)
local M = {}
local api = require("marunochiAI.api")

local state = {
  chat_buf = nil,
  chat_win = nil,
  input_buf = nil,
  input_win = nil,
  history = {},
  busy = false,
}

local WIDTH = 60
local INPUT_HEIGHT = 3

-- Create or get chat buffer
local function get_chat_buf()
  if state.chat_buf and vim.api.nvim_buf_is_valid(state.chat_buf) then
    return state.chat_buf
  end
  state.chat_buf = vim.api.nvim_create_buf(false, true)
  vim.bo[state.chat_buf].buftype = "nofile"
  vim.bo[state.chat_buf].bufhidden = "hide"
  vim.bo[state.chat_buf].swapfile = false
  vim.bo[state.chat_buf].filetype = "markdown"
  return state.chat_buf
end

-- Create or get input buffer
local function get_input_buf()
  if state.input_buf and vim.api.nvim_buf_is_valid(state.input_buf) then
    return state.input_buf
  end
  state.input_buf = vim.api.nvim_create_buf(false, true)
  vim.bo[state.input_buf].buftype = "nofile"
  vim.bo[state.input_buf].bufhidden = "hide"
  vim.bo[state.input_buf].swapfile = false
  return state.input_buf
end

-- Render chat content
local function render()
  local buf = state.chat_buf
  if not buf or not vim.api.nvim_buf_is_valid(buf) then return end

  vim.bo[buf].modifiable = true

  local lines = { "╭─ MarunochiAI ─────────────────────────────╮", "" }

  if #state.history == 0 then
    table.insert(lines, "  Type a message below and press Enter.")
    table.insert(lines, "")
    table.insert(lines, "  Keybindings:")
    table.insert(lines, "    Enter  - Send message")
    table.insert(lines, "    q/Esc  - Close panel")
    table.insert(lines, "")
  else
    for _, msg in ipairs(state.history) do
      if msg.role == "user" then
        table.insert(lines, "┌─ You ────────────────────────────────────")
      else
        table.insert(lines, "┌─ AI ─────────────────────────────────────")
      end
      for _, l in ipairs(vim.split(msg.content, "\n")) do
        table.insert(lines, "│ " .. l)
      end
      table.insert(lines, "└──────────────────────────────────────────")
      table.insert(lines, "")
    end
  end

  if state.busy then
    table.insert(lines, "│ ▌ Thinking...")
    table.insert(lines, "")
  end

  vim.api.nvim_buf_set_lines(buf, 0, -1, false, lines)
  vim.bo[buf].modifiable = false

  -- Scroll to bottom
  if state.chat_win and vim.api.nvim_win_is_valid(state.chat_win) then
    vim.api.nvim_win_set_cursor(state.chat_win, { #lines, 0 })
  end
end

-- Calculate window positions
local function get_win_config()
  local editor_height = vim.o.lines - vim.o.cmdheight - 1
  local editor_width = vim.o.columns

  local chat_height = editor_height - INPUT_HEIGHT - 2 -- 2 for borders

  return {
    chat = {
      relative = "editor",
      width = WIDTH,
      height = chat_height,
      row = 0,
      col = editor_width - WIDTH - 1,
      style = "minimal",
      border = "rounded",
      title = " Chat ",
      title_pos = "center",
    },
    input = {
      relative = "editor",
      width = WIDTH,
      height = INPUT_HEIGHT,
      row = chat_height + 2,
      col = editor_width - WIDTH - 1,
      style = "minimal",
      border = "rounded",
      title = " Message (Enter to send) ",
      title_pos = "center",
    },
  }
end

-- Open the chat panel
function M.open()
  if state.chat_win and vim.api.nvim_win_is_valid(state.chat_win) then
    -- Already open, focus input
    if state.input_win and vim.api.nvim_win_is_valid(state.input_win) then
      vim.api.nvim_set_current_win(state.input_win)
      vim.cmd("startinsert")
    end
    return
  end

  local chat_buf = get_chat_buf()
  local input_buf = get_input_buf()
  local config = get_win_config()

  -- Open chat window
  state.chat_win = vim.api.nvim_open_win(chat_buf, false, config.chat)
  vim.wo[state.chat_win].wrap = true
  vim.wo[state.chat_win].linebreak = true
  vim.wo[state.chat_win].cursorline = false

  -- Open input window
  state.input_win = vim.api.nvim_open_win(input_buf, true, config.input)
  vim.wo[state.input_win].wrap = true

  -- Setup keymaps for input buffer
  local opts = { buffer = input_buf, silent = true, nowait = true }
  vim.keymap.set("i", "<CR>", function()
    vim.cmd("stopinsert")
    M.send_input()
  end, opts)
  vim.keymap.set("n", "<CR>", function() M.send_input() end, opts)
  vim.keymap.set({ "n", "i" }, "<Esc>", function()
    vim.cmd("stopinsert")
    M.close()
  end, opts)
  vim.keymap.set("n", "q", function() M.close() end, opts)

  -- Setup keymaps for chat buffer
  local chat_opts = { buffer = chat_buf, silent = true, nowait = true }
  vim.keymap.set("n", "q", function() M.close() end, chat_opts)
  vim.keymap.set("n", "<Esc>", function() M.close() end, chat_opts)
  vim.keymap.set("n", "i", function()
    if state.input_win and vim.api.nvim_win_is_valid(state.input_win) then
      vim.api.nvim_set_current_win(state.input_win)
      vim.cmd("startinsert")
    end
  end, chat_opts)

  render()
  vim.cmd("startinsert")
end

-- Close the chat panel
function M.close()
  if state.input_win and vim.api.nvim_win_is_valid(state.input_win) then
    vim.api.nvim_win_close(state.input_win, true)
  end
  if state.chat_win and vim.api.nvim_win_is_valid(state.chat_win) then
    vim.api.nvim_win_close(state.chat_win, true)
  end
  state.chat_win = nil
  state.input_win = nil
end

-- Toggle the chat panel
function M.toggle()
  if state.chat_win and vim.api.nvim_win_is_valid(state.chat_win) then
    M.close()
  else
    M.open()
  end
end

-- Send message from input buffer
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
  vim.api.nvim_buf_set_lines(state.input_buf, 0, -1, false, { "" })

  M.send(message)
end

-- Send a message to the AI
function M.send(message)
  if state.busy then return end

  state.busy = true
  table.insert(state.history, { role = "user", content = message })
  render()

  local response = ""
  local response_added = false

  api.chat_stream(state.history, function(token)
    response = response .. token
  end, function()
    -- Guard against double callback
    if response_added then return end
    response_added = true

    state.busy = false
    if response ~= "" then
      table.insert(state.history, { role = "assistant", content = response })
    end
    vim.schedule(function()
      render()
      -- Refocus input
      if state.input_win and vim.api.nvim_win_is_valid(state.input_win) then
        vim.api.nvim_set_current_win(state.input_win)
        vim.cmd("startinsert")
      end
    end)
  end)
end

-- Open chat with code context
function M.ask_about_code(prompt, code, filetype)
  local message = prompt .. "\n\n```" .. (filetype or "") .. "\n" .. code .. "\n```"
  M.open()
  M.send(message)
end

-- Clear chat history
function M.clear()
  state.history = {}
  render()
end

return M
