---MarunochiAI Chat - Full AI assistant experience for Neovim
---@class MarunochiChat
local M = {}

local api = require("marunochiAI.api")

-- State
M.history = {}
M.chat_bufnr = nil
M.chat_winnr = nil
M.input_bufnr = nil
M.input_winnr = nil
M.is_processing = false

-- Configuration
local config = {
  width = 80,
  split_direction = "right", -- "right", "left", "below", "above"
}

---Initialize chat UI
function M.setup_chat_ui()
  -- Create chat buffer
  M.chat_bufnr = vim.api.nvim_create_buf(false, true)
  vim.api.nvim_buf_set_option(M.chat_bufnr, "buftype", "nofile")
  vim.api.nvim_buf_set_option(M.chat_bufnr, "filetype", "markdown")
  vim.api.nvim_buf_set_option(M.chat_bufnr, "modifiable", true)
  vim.api.nvim_buf_set_name(M.chat_bufnr, "[MarunochiAI Chat]")

  -- Create input buffer
  M.input_bufnr = vim.api.nvim_create_buf(false, true)
  vim.api.nvim_buf_set_option(M.input_bufnr, "buftype", "nofile")
  vim.api.nvim_buf_set_option(M.input_bufnr, "filetype", "markdown")
  vim.api.nvim_buf_set_name(M.input_bufnr, "[MarunochiAI Input]")
end

---Open chat in a split
---@param initial_prompt string|nil Initial message to send
function M.open_chat(initial_prompt)
  -- If chat is already open, focus it
  if M.chat_winnr and vim.api.nvim_win_is_valid(M.chat_winnr) then
    vim.api.nvim_set_current_win(M.chat_winnr)
    if initial_prompt and initial_prompt ~= "" then
      M.send_message(initial_prompt)
    end
    return
  end

  -- Create buffers if needed
  if not M.chat_bufnr or not vim.api.nvim_buf_is_valid(M.chat_bufnr) then
    M.setup_chat_ui()
  end

  -- Open chat split
  local cmd = config.split_direction == "right" and "botright vsplit"
    or config.split_direction == "left" and "topleft vsplit"
    or config.split_direction == "below" and "botright split"
    or "topleft split"

  vim.cmd(cmd)
  M.chat_winnr = vim.api.nvim_get_current_win()
  vim.api.nvim_win_set_buf(M.chat_winnr, M.chat_bufnr)
  vim.api.nvim_win_set_width(M.chat_winnr, config.width)

  -- Set window options
  vim.wo[M.chat_winnr].wrap = true
  vim.wo[M.chat_winnr].linebreak = true
  vim.wo[M.chat_winnr].number = false
  vim.wo[M.chat_winnr].relativenumber = false
  vim.wo[M.chat_winnr].signcolumn = "no"
  vim.wo[M.chat_winnr].cursorline = false

  -- Initial welcome content
  if #M.history == 0 then
    M.render_welcome()
  else
    M.render_chat()
  end

  -- Set up keymaps
  M.setup_keymaps()

  -- Focus input at bottom
  vim.cmd("normal! G")

  -- Send initial prompt if provided
  if initial_prompt and initial_prompt ~= "" then
    vim.schedule(function()
      M.send_message(initial_prompt)
    end)
  end
end

---Close chat
function M.close_chat()
  if M.chat_winnr and vim.api.nvim_win_is_valid(M.chat_winnr) then
    vim.api.nvim_win_close(M.chat_winnr, true)
  end
  M.chat_winnr = nil
end

---Toggle chat
function M.toggle_chat()
  if M.chat_winnr and vim.api.nvim_win_is_valid(M.chat_winnr) then
    M.close_chat()
  else
    M.open_chat()
  end
end

---Set up keymaps for chat buffer
function M.setup_keymaps()
  local opts = { noremap = true, silent = true, buffer = M.chat_bufnr }

  -- Close chat
  vim.keymap.set("n", "q", M.close_chat, opts)
  vim.keymap.set("n", "<Esc>", M.close_chat, opts)

  -- Send message (from input at bottom)
  vim.keymap.set("n", "<CR>", M.prompt_and_send, opts)
  vim.keymap.set("n", "i", M.prompt_and_send, opts)

  -- Clear history
  vim.keymap.set("n", "C", M.clear_history, opts)

  -- Copy code block under cursor
  vim.keymap.set("n", "yc", M.copy_code_block, opts)

  -- Insert code block into previous buffer
  vim.keymap.set("n", "<C-y>", M.insert_code_block, opts)

  -- Scroll
  vim.keymap.set("n", "j", "gj", opts)
  vim.keymap.set("n", "k", "gk", opts)
end

---Render welcome message
function M.render_welcome()
  local lines = {
    "╭─────────────────────────────────────────────╮",
    "│             MarunochiAI Chat                │",
    "│        Your Local AI Coding Assistant       │",
    "╰─────────────────────────────────────────────╯",
    "",
    "Welcome! I'm MarunochiAI, running locally on your machine.",
    "I use Qwen2.5-Coder for fast, private code assistance.",
    "",
    "╭─ Quick Actions ────────────────────────────╮",
    "│  i / <CR>  - Ask a question                │",
    "│  yc        - Copy code block under cursor  │",
    "│  <C-y>     - Insert code into editor       │",
    "│  C         - Clear chat history            │",
    "│  q / <Esc> - Close chat                    │",
    "╰────────────────────────────────────────────╯",
    "",
    "Try asking:",
    "  • 'Explain the selected code'",
    "  • 'How do I implement binary search?'",
    "  • 'Refactor this to be more efficient'",
    "",
    "─────────────────────────────────────────────",
    "",
  }

  vim.api.nvim_buf_set_lines(M.chat_bufnr, 0, -1, false, lines)
end

---Render full chat history
function M.render_chat()
  local lines = {
    "╭─────────────────────────────────────────────╮",
    "│             MarunochiAI Chat                │",
    "╰─────────────────────────────────────────────╯",
    "",
  }

  for _, entry in ipairs(M.history) do
    if entry.role == "user" then
      table.insert(lines, "┌─ You ──────────────────────────────────────")
      for _, line in ipairs(vim.split(entry.content, "\n")) do
        table.insert(lines, "│ " .. line)
      end
      table.insert(lines, "└────────────────────────────────────────────")
      table.insert(lines, "")
    else
      table.insert(lines, "┌─ MarunochiAI ──────────────────────────────")
      for _, line in ipairs(vim.split(entry.content, "\n")) do
        table.insert(lines, "│ " .. line)
      end
      table.insert(lines, "└────────────────────────────────────────────")
      table.insert(lines, "")
    end
  end

  table.insert(lines, "─────────────────────────────────────────────")
  table.insert(lines, "Press 'i' or <CR> to ask a question...")

  vim.api.nvim_buf_set_lines(M.chat_bufnr, 0, -1, false, lines)

  -- Scroll to bottom
  if M.chat_winnr and vim.api.nvim_win_is_valid(M.chat_winnr) then
    local line_count = vim.api.nvim_buf_line_count(M.chat_bufnr)
    vim.api.nvim_win_set_cursor(M.chat_winnr, { line_count, 0 })
  end
end

---Prompt user for input and send
function M.prompt_and_send()
  if M.is_processing then
    vim.notify("MarunochiAI is still thinking...", vim.log.levels.WARN)
    return
  end

  -- Get context from previous window
  local context = M.get_context()

  vim.ui.input({
    prompt = "Ask MarunochiAI: ",
    default = "",
  }, function(input)
    if input and input ~= "" then
      M.send_message(input, context)
    end
  end)
end

---Get context from the editor
---@return table Context information
function M.get_context()
  local context = {}

  -- Find a non-chat window to get context from
  for _, winnr in ipairs(vim.api.nvim_list_wins()) do
    local bufnr = vim.api.nvim_win_get_buf(winnr)
    local name = vim.api.nvim_buf_get_name(bufnr)
    if not name:match("MarunochiAI") then
      context.filename = name
      context.filetype = vim.api.nvim_buf_get_option(bufnr, "filetype")

      -- Get visual selection if any
      local mode = vim.fn.mode()
      if mode == "v" or mode == "V" then
        local start_line = vim.fn.line("'<")
        local end_line = vim.fn.line("'>")
        local lines = vim.api.nvim_buf_get_lines(bufnr, start_line - 1, end_line, false)
        context.selection = table.concat(lines, "\n")
      end
      break
    end
  end

  return context
end

---Send message to MarunochiAI
---@param message string User message
---@param context table|nil Context information
function M.send_message(message, context)
  if M.is_processing then
    return
  end

  M.is_processing = true

  -- Build full message with context
  local full_message = message
  if context and context.selection then
    full_message = string.format(
      "[Selected code from %s]\n```%s\n%s\n```\n\n%s",
      context.filename or "unknown",
      context.filetype or "",
      context.selection,
      message
    )
  elseif context and context.filename then
    full_message = string.format("[Working on: %s]\n\n%s", context.filename, message)
  end

  -- Add to history
  table.insert(M.history, { role = "user", content = full_message })

  -- Update UI to show user message
  M.render_chat()

  -- Add loading indicator
  local loading_lines = {
    "┌─ MarunochiAI ──────────────────────────────",
    "│ Thinking...",
    "└────────────────────────────────────────────",
  }
  local line_count = vim.api.nvim_buf_line_count(M.chat_bufnr)
  vim.api.nvim_buf_set_lines(M.chat_bufnr, line_count - 2, line_count, false, loading_lines)

  -- Send request
  local response_text = ""

  api.chat_completion_stream(M.history, function(token)
    response_text = response_text .. token

    -- Update UI with streaming response
    vim.schedule(function()
      if not M.chat_bufnr or not vim.api.nvim_buf_is_valid(M.chat_bufnr) then
        return
      end

      local response_lines = { "┌─ MarunochiAI ──────────────────────────────" }
      for _, line in ipairs(vim.split(response_text, "\n")) do
        table.insert(response_lines, "│ " .. line)
      end
      table.insert(response_lines, "│ ...")
      table.insert(response_lines, "└────────────────────────────────────────────")

      local buf_lines = vim.api.nvim_buf_get_lines(M.chat_bufnr, 0, -1, false)
      -- Find where to insert (remove old loading/response)
      local insert_pos = #buf_lines - 3
      for i = #buf_lines, 1, -1 do
        if buf_lines[i]:match("^┌─ MarunochiAI") then
          insert_pos = i - 1
          break
        end
      end

      vim.api.nvim_buf_set_lines(M.chat_bufnr, insert_pos, -1, false, response_lines)

      -- Scroll to bottom
      if M.chat_winnr and vim.api.nvim_win_is_valid(M.chat_winnr) then
        local new_count = vim.api.nvim_buf_line_count(M.chat_bufnr)
        vim.api.nvim_win_set_cursor(M.chat_winnr, { new_count, 0 })
      end
    end)
  end, function()
    -- Completion callback
    M.is_processing = false
    table.insert(M.history, { role = "assistant", content = response_text })

    vim.schedule(function()
      M.render_chat()
      vim.notify("MarunochiAI response complete", vim.log.levels.INFO)
    end)
  end)
end

---Clear chat history
function M.clear_history()
  M.history = {}
  vim.notify("Chat history cleared", vim.log.levels.INFO)
  M.render_welcome()
end

---Copy code block under cursor
function M.copy_code_block()
  local cursor = vim.api.nvim_win_get_cursor(M.chat_winnr)
  local lines = vim.api.nvim_buf_get_lines(M.chat_bufnr, 0, -1, false)

  -- Find code block boundaries
  local in_code_block = false
  local code_start = nil
  local code_lines = {}

  for i, line in ipairs(lines) do
    if line:match("^│ ```") then
      if in_code_block then
        -- End of code block
        if cursor[1] >= code_start and cursor[1] <= i then
          -- Cursor is in this block
          vim.fn.setreg("+", table.concat(code_lines, "\n"))
          vim.notify("Code copied to clipboard", vim.log.levels.INFO)
          return
        end
        in_code_block = false
        code_lines = {}
      else
        -- Start of code block
        in_code_block = true
        code_start = i
      end
    elseif in_code_block then
      -- Remove the │ prefix
      local clean_line = line:gsub("^│ ", "")
      table.insert(code_lines, clean_line)
    end
  end

  vim.notify("No code block found at cursor", vim.log.levels.WARN)
end

---Insert code block into previous buffer
function M.insert_code_block()
  local cursor = vim.api.nvim_win_get_cursor(M.chat_winnr)
  local lines = vim.api.nvim_buf_get_lines(M.chat_bufnr, 0, -1, false)

  -- Find code block under cursor (same logic as copy)
  local in_code_block = false
  local code_start = nil
  local code_lines = {}

  for i, line in ipairs(lines) do
    if line:match("^│ ```") then
      if in_code_block then
        if cursor[1] >= code_start and cursor[1] <= i then
          -- Found the block, now insert it
          M.close_chat()

          -- Insert at cursor in current buffer
          local current_line = vim.api.nvim_win_get_cursor(0)[1]
          vim.api.nvim_buf_set_lines(0, current_line, current_line, false, code_lines)
          vim.notify("Code inserted", vim.log.levels.INFO)
          return
        end
        in_code_block = false
        code_lines = {}
      else
        in_code_block = true
        code_start = i
      end
    elseif in_code_block then
      local clean_line = line:gsub("^│ ", "")
      table.insert(code_lines, clean_line)
    end
  end

  vim.notify("No code block found at cursor", vim.log.levels.WARN)
end

---Explain selected code
function M.explain_selection()
  local start_line = vim.fn.line("'<")
  local end_line = vim.fn.line("'>")
  local bufnr = vim.api.nvim_get_current_buf()
  local lines = vim.api.nvim_buf_get_lines(bufnr, start_line - 1, end_line, false)
  local code = table.concat(lines, "\n")
  local filetype = vim.api.nvim_buf_get_option(bufnr, "filetype")

  local prompt = string.format("Explain this %s code in detail:\n\n```%s\n%s\n```", filetype, filetype, code)

  M.open_chat(prompt)
end

---Refactor selected code
function M.refactor_selection()
  local start_line = vim.fn.line("'<")
  local end_line = vim.fn.line("'>")
  local bufnr = vim.api.nvim_get_current_buf()
  local lines = vim.api.nvim_buf_get_lines(bufnr, start_line - 1, end_line, false)
  local code = table.concat(lines, "\n")
  local filetype = vim.api.nvim_buf_get_option(bufnr, "filetype")

  local prompt = string.format(
    "Refactor this %s code to improve readability, performance, and best practices:\n\n```%s\n%s\n```",
    filetype,
    filetype,
    code
  )

  M.open_chat(prompt)
end

---Debug selected code
function M.debug_selection()
  local start_line = vim.fn.line("'<")
  local end_line = vim.fn.line("'>")
  local bufnr = vim.api.nvim_get_current_buf()
  local lines = vim.api.nvim_buf_get_lines(bufnr, start_line - 1, end_line, false)
  local code = table.concat(lines, "\n")
  local filetype = vim.api.nvim_buf_get_option(bufnr, "filetype")

  local prompt = string.format(
    "Debug this %s code. Identify potential issues, bugs, or improvements:\n\n```%s\n%s\n```",
    filetype,
    filetype,
    code
  )

  M.open_chat(prompt)
end

---Generate tests for selected code
function M.generate_tests()
  local start_line = vim.fn.line("'<")
  local end_line = vim.fn.line("'>")
  local bufnr = vim.api.nvim_get_current_buf()
  local lines = vim.api.nvim_buf_get_lines(bufnr, start_line - 1, end_line, false)
  local code = table.concat(lines, "\n")
  local filetype = vim.api.nvim_buf_get_option(bufnr, "filetype")

  local prompt = string.format(
    "Generate comprehensive unit tests for this %s code:\n\n```%s\n%s\n```",
    filetype,
    filetype,
    code
  )

  M.open_chat(prompt)
end

---Apply code suggestion (replace selection)
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
