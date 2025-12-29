-- MarunochiAI Inline Edit (Cursor Cmd+K style)
-- Select code, describe change, AI modifies in place
local M = {}
local api = require("marunochiAI.api")

local ns = vim.api.nvim_create_namespace("marunochiAI_edit")

-- Edit selected code with AI
function M.edit_selection()
  -- Get selection bounds
  local start_line = vim.fn.line("'<")
  local end_line = vim.fn.line("'>")

  if start_line == 0 or end_line == 0 then
    vim.notify("Select code first (visual mode)", vim.log.levels.WARN)
    return
  end

  local bufnr = vim.api.nvim_get_current_buf()
  local lines = vim.api.nvim_buf_get_lines(bufnr, start_line - 1, end_line, false)
  local code = table.concat(lines, "\n")
  local filetype = vim.bo[bufnr].filetype

  -- Highlight selection
  for i = start_line - 1, end_line - 1 do
    vim.api.nvim_buf_add_highlight(bufnr, ns, "Visual", i, 0, -1)
  end

  -- Prompt for instruction
  vim.ui.input({ prompt = "Edit instruction: " }, function(instruction)
    -- Clear highlight
    vim.api.nvim_buf_clear_namespace(bufnr, ns, 0, -1)

    if not instruction or instruction == "" then
      return
    end

    vim.notify("Generating edit...", vim.log.levels.INFO)

    -- Build prompt
    local messages = {
      {
        role = "system",
        content = "You are a code editor. Modify code according to instructions. "
          .. "Output ONLY the modified code. No explanations. No markdown. No backticks.",
      },
      {
        role = "user",
        content = "Language: " .. filetype .. "\n\n"
          .. "Code:\n" .. code .. "\n\n"
          .. "Instruction: " .. instruction .. "\n\n"
          .. "Output only the modified code:",
      },
    }

    api.chat(messages, function(success, response)
      vim.schedule(function()
        if not success then
          vim.notify("Edit failed: " .. tostring(response), vim.log.levels.ERROR)
          return
        end

        local result = response.choices[1].message.content

        -- Clean markdown artifacts
        result = result:gsub("^```%w*\n?", ""):gsub("\n?```$", "")

        -- Preview changes
        local new_lines = vim.split(result, "\n")

        vim.ui.select({ "Apply", "Cancel" }, {
          prompt = "Apply changes? (" .. #lines .. " → " .. #new_lines .. " lines)",
        }, function(choice)
          if choice == "Apply" then
            vim.api.nvim_buf_set_lines(bufnr, start_line - 1, end_line, false, new_lines)
            vim.notify("Edit applied", vim.log.levels.INFO)
          end
        end)
      end)
    end)
  end)
end

-- Generate code at cursor
function M.generate_at_cursor()
  local bufnr = vim.api.nvim_get_current_buf()
  local cursor = vim.api.nvim_win_get_cursor(0)
  local line = cursor[1]
  local filetype = vim.bo[bufnr].filetype

  -- Get context
  local all_lines = vim.api.nvim_buf_get_lines(bufnr, 0, -1, false)
  local before = table.concat(vim.list_slice(all_lines, 1, line), "\n")
  local after = table.concat(vim.list_slice(all_lines, line + 1), "\n")

  vim.ui.input({ prompt = "Generate: " }, function(instruction)
    if not instruction or instruction == "" then
      return
    end

    vim.notify("Generating...", vim.log.levels.INFO)

    local messages = {
      {
        role = "system",
        content = "You are a code generator. Generate code based on instructions. "
          .. "Output ONLY code. No explanations. No markdown. No backticks.",
      },
      {
        role = "user",
        content = "Language: " .. filetype .. "\n\n"
          .. "Context before cursor:\n" .. before:sub(-500) .. "\n\n"
          .. "Context after cursor:\n" .. after:sub(1, 300) .. "\n\n"
          .. "Generate: " .. instruction .. "\n\n"
          .. "Output only the code:",
      },
    }

    api.chat(messages, function(success, response)
      vim.schedule(function()
        if not success then
          vim.notify("Generation failed", vim.log.levels.ERROR)
          return
        end

        local result = response.choices[1].message.content
        result = result:gsub("^```%w*\n?", ""):gsub("\n?```$", "")

        local new_lines = vim.split(result, "\n")

        vim.ui.select({ "Insert", "Cancel" }, {
          prompt = "Insert " .. #new_lines .. " lines?",
        }, function(choice)
          if choice == "Insert" then
            vim.api.nvim_buf_set_lines(bufnr, line, line, false, new_lines)
            vim.notify("Code inserted", vim.log.levels.INFO)
          end
        end)
      end)
    end)
  end)
end

return M
