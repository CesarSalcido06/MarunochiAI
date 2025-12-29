---MarunochiAI Inline Edit - Cursor/Copilot style inline editing (Cmd+I)
---@class MarunochiInline
local M = {}

local api = require("marunochiAI.api")

-- State
M.is_active = false
M.input_bufnr = nil
M.input_winnr = nil
M.preview_ns = vim.api.nvim_create_namespace("marunochiAI_preview")
M.highlight_ns = vim.api.nvim_create_namespace("marunochiAI_highlight")

-- Configuration
local config = {
  input_height = 1,
  input_width = 60,
}

---Highlight the target range being edited
---@param bufnr number Buffer number
---@param start_line number Start line (0-indexed)
---@param end_line number End line (0-indexed)
local function highlight_range(bufnr, start_line, end_line)
  vim.api.nvim_buf_clear_namespace(bufnr, M.highlight_ns, 0, -1)
  for i = start_line, end_line do
    vim.api.nvim_buf_add_highlight(bufnr, M.highlight_ns, "Visual", i, 0, -1)
  end
end

---Clear highlights
---@param bufnr number Buffer number
local function clear_highlights(bufnr)
  vim.api.nvim_buf_clear_namespace(bufnr, M.highlight_ns, 0, -1)
  vim.api.nvim_buf_clear_namespace(bufnr, M.preview_ns, 0, -1)
end

---Create floating input window
---@param target_bufnr number Target buffer
---@param row number Row position
---@return number, number Buffer and window numbers
local function create_input_window(target_bufnr, row)
  local buf = vim.api.nvim_create_buf(false, true)
  vim.api.nvim_buf_set_option(buf, "buftype", "nofile")
  vim.api.nvim_buf_set_option(buf, "filetype", "markdown")

  local width = math.min(config.input_width, vim.o.columns - 4)
  local col = math.floor((vim.o.columns - width) / 2)

  local win = vim.api.nvim_open_win(buf, true, {
    relative = "editor",
    row = row,
    col = col,
    width = width,
    height = config.input_height,
    style = "minimal",
    border = "rounded",
    title = " MarunochiAI: Edit ",
    title_pos = "center",
  })

  -- Set placeholder
  vim.api.nvim_buf_set_lines(buf, 0, -1, false, { "" })

  -- Window options
  vim.wo[win].wrap = true
  vim.wo[win].cursorline = false

  return buf, win
end

---Close input window
local function close_input()
  if M.input_winnr and vim.api.nvim_win_is_valid(M.input_winnr) then
    vim.api.nvim_win_close(M.input_winnr, true)
  end
  if M.input_bufnr and vim.api.nvim_buf_is_valid(M.input_bufnr) then
    vim.api.nvim_buf_delete(M.input_bufnr, { force = true })
  end
  M.input_winnr = nil
  M.input_bufnr = nil
  M.is_active = false
end

---Generate edit using AI
---@param context table Context with code, prompt, etc.
---@param callback function Callback with result
local function generate_edit(context, callback)
  local messages

  if context.has_selection then
    -- Edit mode
    messages = {
      {
        role = "system",
        content = string.format(
          [[You are an expert code editor. Modify code according to instructions.
Language: %s

Rules:
- Output ONLY the modified code
- No markdown, no backticks, no explanations
- Preserve indentation style
- Keep changes minimal and focused]],
          context.filetype
        ),
      },
      {
        role = "user",
        content = string.format(
          [[Code to edit:
%s

Instruction: %s

Output only the modified code:]],
          context.code,
          context.prompt
        ),
      },
    }
  else
    -- Generate mode
    messages = {
      {
        role = "system",
        content = string.format(
          [[You are an expert code generator.
Language: %s

Rules:
- Output ONLY code
- No markdown, no backticks, no explanations
- Match surrounding indentation style]],
          context.filetype
        ),
      },
      {
        role = "user",
        content = string.format(
          [[Context:
%s
[INSERT CODE HERE]
%s

Generate code for: %s

Output only the code:]],
          context.before:sub(-300),
          context.after:sub(1, 200),
          context.prompt
        ),
      },
    }
  end

  api.chat_completion(messages, function(success, response)
    if not success then
      callback(nil, "Failed to generate edit")
      return
    end

    local result = response.choices[1].message.content
    -- Clean up markdown artifacts
    result = result:gsub("^```%w*\n?", ""):gsub("\n?```$", "")
    callback(result, nil)
  end)
end

---Show preview of changes with virtual text
---@param bufnr number Buffer number
---@param start_line number Start line (0-indexed)
---@param new_lines table New lines to preview
local function show_preview(bufnr, start_line, new_lines)
  vim.api.nvim_buf_clear_namespace(bufnr, M.preview_ns, 0, -1)

  -- Show new lines as virtual text
  for i, line in ipairs(new_lines) do
    vim.api.nvim_buf_set_extmark(bufnr, M.preview_ns, start_line + i - 1, 0, {
      virt_lines = { { { line, "DiffAdd" } } },
      virt_lines_above = true,
    })
  end
end

---Apply changes to buffer
---@param bufnr number Buffer number
---@param start_line number Start line (1-indexed)
---@param end_line number End line (1-indexed)
---@param new_text string New text
local function apply_changes(bufnr, start_line, end_line, new_text)
  local lines = vim.split(new_text, "\n")
  vim.api.nvim_buf_set_lines(bufnr, start_line - 1, end_line, false, lines)
end

---Start inline edit at current position (Cmd+I style)
function M.start_inline_edit()
  if M.is_active then
    return
  end

  local target_bufnr = vim.api.nvim_get_current_buf()
  local target_winnr = vim.api.nvim_get_current_win()
  local cursor = vim.api.nvim_win_get_cursor(target_winnr)

  -- Get selection info
  local mode = vim.fn.mode()
  local has_selection = mode == "v" or mode == "V" or mode == "\22"

  local start_line, end_line, code

  if has_selection then
    -- Get visual selection
    vim.cmd("normal! ")  -- Exit visual mode to set '< and '> marks
    start_line = vim.fn.line("'<")
    end_line = vim.fn.line("'>")
    local lines = vim.api.nvim_buf_get_lines(target_bufnr, start_line - 1, end_line, false)
    code = table.concat(lines, "\n")
  else
    -- Use current line
    start_line = cursor[1]
    end_line = cursor[1]
    local lines = vim.api.nvim_buf_get_lines(target_bufnr, start_line - 1, end_line, false)
    code = table.concat(lines, "\n")
  end

  -- Highlight the range
  highlight_range(target_bufnr, start_line - 1, end_line - 1)

  -- Get context
  local filetype = vim.api.nvim_buf_get_option(target_bufnr, "filetype")
  local all_lines = vim.api.nvim_buf_get_lines(target_bufnr, 0, -1, false)
  local before = table.concat(vim.list_slice(all_lines, 1, start_line - 1), "\n")
  local after = table.concat(vim.list_slice(all_lines, end_line + 1), "\n")

  M.is_active = true

  -- Create floating input
  local input_row = math.min(cursor[1] + 2, vim.o.lines - 5)
  M.input_bufnr, M.input_winnr = create_input_window(target_bufnr, input_row)

  -- Set up input keymaps
  local opts = { noremap = true, silent = true, buffer = M.input_bufnr }

  -- Enter to submit
  vim.keymap.set({ "n", "i" }, "<CR>", function()
    local prompt_lines = vim.api.nvim_buf_get_lines(M.input_bufnr, 0, -1, false)
    local prompt = table.concat(prompt_lines, " ")

    if prompt == "" then
      close_input()
      clear_highlights(target_bufnr)
      return
    end

    -- Close input window
    close_input()

    -- Show loading
    vim.notify("MarunochiAI: Generating...", vim.log.levels.INFO)

    -- Generate edit
    local context = {
      has_selection = has_selection or code ~= "",
      code = code,
      prompt = prompt,
      filetype = filetype,
      before = before,
      after = after,
    }

    generate_edit(context, function(result, err)
      vim.schedule(function()
        clear_highlights(target_bufnr)

        if err then
          vim.notify("MarunochiAI: " .. err, vim.log.levels.ERROR)
          return
        end

        -- Show confirmation
        vim.ui.select({ "Accept", "Preview Diff", "Cancel" }, {
          prompt = "Apply changes?",
        }, function(choice)
          if choice == "Accept" then
            apply_changes(target_bufnr, start_line, end_line, result)
            vim.notify("MarunochiAI: Changes applied", vim.log.levels.INFO)
          elseif choice == "Preview Diff" then
            -- Show diff in split
            local diff_buf = vim.api.nvim_create_buf(false, true)
            vim.api.nvim_buf_set_option(diff_buf, "filetype", filetype)
            vim.api.nvim_buf_set_lines(diff_buf, 0, -1, false, vim.split(result, "\n"))
            vim.cmd("vsplit")
            vim.api.nvim_win_set_buf(0, diff_buf)
            vim.api.nvim_buf_set_name(diff_buf, "[MarunochiAI Preview]")

            -- Ask again
            vim.ui.select({ "Accept", "Cancel" }, {
              prompt = "Apply these changes?",
            }, function(choice2)
              vim.cmd("close")
              if choice2 == "Accept" then
                apply_changes(target_bufnr, start_line, end_line, result)
                vim.notify("MarunochiAI: Changes applied", vim.log.levels.INFO)
              end
            end)
          end
        end)
      end)
    end)
  end, opts)

  -- Escape to cancel
  vim.keymap.set({ "n", "i" }, "<Esc>", function()
    close_input()
    clear_highlights(target_bufnr)
  end, opts)

  -- Start in insert mode
  vim.cmd("startinsert")
end

---Quick action on selection
---@param action string Action type: "explain", "refactor", "fix", "document", "test"
function M.quick_action(action)
  local bufnr = vim.api.nvim_get_current_buf()
  local start_line = vim.fn.line("'<")
  local end_line = vim.fn.line("'>")

  if start_line == 0 or end_line == 0 then
    vim.notify("Please select code first", vim.log.levels.WARN)
    return
  end

  local lines = vim.api.nvim_buf_get_lines(bufnr, start_line - 1, end_line, false)
  local code = table.concat(lines, "\n")
  local filetype = vim.api.nvim_buf_get_option(bufnr, "filetype")

  local prompts = {
    explain = string.format("Explain this %s code concisely:\n\n%s", filetype, code),
    refactor = string.format(
      "Refactor this %s code to be cleaner and more efficient. Output only code:\n\n%s",
      filetype,
      code
    ),
    fix = string.format("Fix any bugs in this %s code. Output only code:\n\n%s", filetype, code),
    document = string.format("Add documentation to this %s code. Output only code:\n\n%s", filetype, code),
    test = string.format("Generate unit tests for this %s code:\n\n%s", filetype, code),
  }

  local replace_actions = { refactor = true, fix = true, document = true }

  vim.notify("MarunochiAI: " .. action .. "...", vim.log.levels.INFO)

  api.chat_completion({
    { role = "user", content = prompts[action] },
  }, function(success, response)
    vim.schedule(function()
      if not success then
        vim.notify("MarunochiAI: Failed", vim.log.levels.ERROR)
        return
      end

      local result = response.choices[1].message.content
      result = result:gsub("^```%w*\n?", ""):gsub("\n?```$", "")

      if replace_actions[action] then
        -- Replace selection
        apply_changes(bufnr, start_line, end_line, result)
        vim.notify("MarunochiAI: " .. action .. " complete", vim.log.levels.INFO)
      else
        -- Show in floating window (explain, test)
        local float_buf = vim.api.nvim_create_buf(false, true)
        vim.api.nvim_buf_set_option(float_buf, "filetype", "markdown")
        vim.api.nvim_buf_set_lines(float_buf, 0, -1, false, vim.split(result, "\n"))

        local width = math.min(80, vim.o.columns - 10)
        local height = math.min(20, vim.o.lines - 10)

        vim.api.nvim_open_win(float_buf, true, {
          relative = "editor",
          row = math.floor((vim.o.lines - height) / 2),
          col = math.floor((vim.o.columns - width) / 2),
          width = width,
          height = height,
          style = "minimal",
          border = "rounded",
          title = " MarunochiAI: " .. action:gsub("^%l", string.upper) .. " ",
          title_pos = "center",
        })

        -- Close on q or Esc
        vim.keymap.set("n", "q", "<cmd>close<cr>", { buffer = float_buf })
        vim.keymap.set("n", "<Esc>", "<cmd>close<cr>", { buffer = float_buf })
      end
    end)
  end)
end

return M
