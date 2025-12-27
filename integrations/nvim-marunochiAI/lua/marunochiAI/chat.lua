---MarunochiAI inline chat and code assistance
---@class MarunochiChat
local M = {}

local api = require("marunochiAI.api")

---Chat history
M.history = {}

---Open interactive chat window
---@param initial_prompt string|nil Initial message
function M.open_chat(initial_prompt)
  -- Create a new buffer for chat
  local bufnr = vim.api.nvim_create_buf(false, true)
  vim.api.nvim_buf_set_option(bufnr, "buftype", "nofile")
  vim.api.nvim_buf_set_option(bufnr, "filetype", "markdown")

  -- Create floating window
  local width = math.floor(vim.o.columns * 0.8)
  local height = math.floor(vim.o.lines * 0.8)
  local row = math.floor((vim.o.lines - height) / 2)
  local col = math.floor((vim.o.columns - width) / 2)

  local win_opts = {
    relative = "editor",
    width = width,
    height = height,
    row = row,
    col = col,
    style = "minimal",
    border = "rounded",
    title = " MarunochiAI Chat ",
    title_pos = "center",
  }

  local winnr = vim.api.nvim_open_win(bufnr, true, win_opts)

  -- Initial content
  local lines = {
    "# MarunochiAI Chat",
    "",
    "Type your message below and press <CR> to send.",
    "Press `q` to close this window.",
    "",
    "---",
    "",
  }

  if initial_prompt and initial_prompt ~= "" then
    table.insert(lines, "**You:** " .. initial_prompt)
    table.insert(lines, "")
    table.insert(lines, "**MarunochiAI:** ")
  end

  vim.api.nvim_buf_set_lines(bufnr, 0, -1, false, lines)

  -- Set up keymaps
  vim.api.nvim_buf_set_keymap(bufnr, "n", "q", ":close<CR>", { noremap = true, silent = true })
  vim.api.nvim_buf_set_keymap(bufnr, "n", "<CR>", "", {
    noremap = true,
    silent = true,
    callback = function()
      M.send_message(bufnr)
    end,
  })

  -- If initial prompt, send it immediately
  if initial_prompt and initial_prompt ~= "" then
    M.send_chat_request(bufnr, initial_prompt)
  end
end

---Send message from chat buffer
---@param bufnr number Buffer number
function M.send_message(bufnr)
  -- Get current line as message
  local line_num = vim.api.nvim_win_get_cursor(0)[1]
  local line = vim.api.nvim_buf_get_lines(bufnr, line_num - 1, line_num, false)[1]

  if not line or line == "" then
    return
  end

  -- Add user message to buffer
  local lines = vim.api.nvim_buf_get_lines(bufnr, 0, -1, false)
  table.insert(lines, "")
  table.insert(lines, "**You:** " .. line)
  table.insert(lines, "")
  table.insert(lines, "**MarunochiAI:** ")

  vim.api.nvim_buf_set_lines(bufnr, 0, -1, false, lines)

  -- Send request
  M.send_chat_request(bufnr, line)
end

---Send chat request and stream response
---@param bufnr number Buffer number
---@param message string User message
function M.send_chat_request(bufnr, message)
  table.insert(M.history, { role = "user", content = message })

  local response_line = vim.api.nvim_buf_line_count(bufnr) - 1
  local response_text = ""

  api.chat_completion_stream(M.history, function(token)
    response_text = response_text .. token

    -- Update buffer with streaming response
    vim.schedule(function()
      local lines = vim.split(response_text, "\n")
      local start_line = response_line
      vim.api.nvim_buf_set_lines(bufnr, start_line, start_line + #lines, false, lines)
    end)
  end, function()
    -- Add assistant response to history
    table.insert(M.history, { role = "assistant", content = response_text })

    vim.schedule(function()
      -- Add separator
      local line_count = vim.api.nvim_buf_line_count(bufnr)
      vim.api.nvim_buf_set_lines(bufnr, line_count, line_count, false, { "", "---", "" })
    end)
  end)
end

---Explain selected code
function M.explain_selection()
  local start_line = vim.fn.line("'<")
  local end_line = vim.fn.line("'>")
  local bufnr = vim.api.nvim_get_current_buf()
  local lines = vim.api.nvim_buf_get_lines(bufnr, start_line - 1, end_line, false)
  local code = table.concat(lines, "\n")

  local prompt = "Explain this code:\n\n```\n" .. code .. "\n```"

  M.open_chat(prompt)
end

---Refactor selected code
function M.refactor_selection()
  local start_line = vim.fn.line("'<")
  local end_line = vim.fn.line("'>")
  local bufnr = vim.api.nvim_get_current_buf()
  local lines = vim.api.nvim_buf_get_lines(bufnr, start_line - 1, end_line, false)
  local code = table.concat(lines, "\n")

  local prompt = "Refactor this code to improve readability and performance:\n\n```\n" .. code .. "\n```"

  M.open_chat(prompt)
end

---Debug selected code
function M.debug_selection()
  local start_line = vim.fn.line("'<")
  local end_line = vim.fn.line("'>")
  local bufnr = vim.api.nvim_get_current_buf()
  local lines = vim.api.nvim_buf_get_lines(bufnr, start_line - 1, end_line, false)
  local code = table.concat(lines, "\n")

  local prompt = "Debug this code and identify potential issues:\n\n```\n" .. code .. "\n```"

  M.open_chat(prompt)
end

---Apply code suggestion inline
---@param suggestion string Code suggestion
function M.apply_suggestion(suggestion)
  -- Extract code blocks from markdown
  local code_blocks = {}
  for block in suggestion:gmatch("```%w*\n(.-)\n```") do
    table.insert(code_blocks, block)
  end

  if #code_blocks == 0 then
    vim.notify("No code blocks found in suggestion", vim.log.levels.WARN)
    return
  end

  -- Replace current selection with first code block
  local lines = vim.split(code_blocks[1], "\n")
  local start_line = vim.fn.line("'<")
  local end_line = vim.fn.line("'>")

  vim.api.nvim_buf_set_lines(0, start_line - 1, end_line, false, lines)
  vim.notify("Applied suggestion", vim.log.levels.INFO)
end

return M
