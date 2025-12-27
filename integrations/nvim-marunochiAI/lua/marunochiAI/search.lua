---MarunochiAI semantic search
---@class MarunochiSearch
local M = {}

local api = require("marunochiAI.api")

---Index codebase with progress notification
---@param path string Codebase path
---@param watch boolean Enable file watching
function M.index_codebase(path, watch)
  vim.notify("Indexing codebase: " .. path, vim.log.levels.INFO)

  api.index_codebase(path, watch, function(success, result)
    if success then
      local msg = string.format(
        "✓ Indexed %d files, %d chunks in %dms",
        result.total_files,
        result.total_chunks,
        result.duration_ms
      )
      if result.watcher_started then
        msg = msg .. "\n👁  File watcher started"
      end
      vim.notify(msg, vim.log.levels.INFO)
    else
      vim.notify("Failed to index: " .. tostring(result), vim.log.levels.ERROR)
    end
  end)
end

---Search codebase and display results
---@param query string Search query
function M.search_codebase(query)
  -- Try to use Telescope if available
  local has_telescope, telescope = pcall(require, "telescope")

  if has_telescope then
    M.search_with_telescope(query)
  else
    M.search_with_quickfix(query)
  end
end

---Search with Telescope picker
---@param query string Search query
function M.search_with_telescope(query)
  local pickers = require("telescope.pickers")
  local finders = require("telescope.finders")
  local conf = require("telescope.config").values
  local actions = require("telescope.actions")
  local action_state = require("telescope.actions.state")
  local previewers = require("telescope.previewers")

  vim.notify("Searching: " .. query, vim.log.levels.INFO)

  api.search_codebase(query, 20, function(success, response)
    if not success then
      vim.notify("Search failed: " .. tostring(response), vim.log.levels.ERROR)
      return
    end

    if not response.results or #response.results == 0 then
      vim.notify("No results found", vim.log.levels.WARN)
      return
    end

    -- Convert results to picker entries
    local results = {}
    for _, result in ipairs(response.results) do
      table.insert(results, {
        filepath = result.filepath,
        name = result.metadata.name,
        line_start = result.metadata.line_range[1],
        line_end = result.metadata.line_range[2],
        similarity = result.similarity,
        language = result.metadata.language,
        chunk_type = result.metadata.chunk_type,
        content = result.content,
        display = string.format(
          "%s:%d  [%.3f] %s (%s)",
          vim.fn.fnamemodify(result.filepath, ":t"),
          result.metadata.line_range[1],
          result.similarity,
          result.metadata.name,
          result.metadata.chunk_type
        ),
      })
    end

    pickers
      .new({}, {
        prompt_title = "MarunochiAI: " .. query,
        finder = finders.new_table({
          results = results,
          entry_maker = function(entry)
            return {
              value = entry,
              display = entry.display,
              ordinal = entry.filepath .. " " .. entry.name,
              filename = entry.filepath,
              lnum = entry.line_start,
            }
          end,
        }),
        sorter = conf.generic_sorter({}),
        previewer = previewers.new_buffer_previewer({
          title = "Code Preview",
          define_preview = function(self, entry)
            local lines = vim.split(entry.value.content, "\n")
            vim.api.nvim_buf_set_lines(self.state.bufnr, 0, -1, false, lines)

            -- Set filetype for syntax highlighting
            local ft = entry.value.language
            if ft == "typescript" then
              ft = "typescript"
            elseif ft == "javascript" then
              ft = "javascript"
            elseif ft == "python" then
              ft = "python"
            end
            vim.api.nvim_buf_set_option(self.state.bufnr, "filetype", ft)
          end,
        }),
        attach_mappings = function(prompt_bufnr, map)
          actions.select_default:replace(function()
            actions.close(prompt_bufnr)
            local selection = action_state.get_selected_entry()
            vim.cmd("edit " .. selection.filename)
            vim.api.nvim_win_set_cursor(0, { selection.lnum, 0 })
          end)
          return true
        end,
      })
      :find()
  end)
end

---Search with quickfix list (fallback)
---@param query string Search query
function M.search_with_quickfix(query)
  vim.notify("Searching: " .. query, vim.log.levels.INFO)

  api.search_codebase(query, nil, function(success, response)
    if not success then
      vim.notify("Search failed: " .. tostring(response), vim.log.levels.ERROR)
      return
    end

    if not response.results or #response.results == 0 then
      vim.notify("No results found", vim.log.levels.WARN)
      return
    end

    -- Convert to quickfix entries
    local qf_list = {}
    for _, result in ipairs(response.results) do
      table.insert(qf_list, {
        filename = result.filepath,
        lnum = result.metadata.line_range[1],
        col = 1,
        text = string.format(
          "[%.3f] %s (%s)",
          result.similarity,
          result.metadata.name,
          result.metadata.chunk_type
        ),
      })
    end

    vim.fn.setqflist(qf_list, "r")
    vim.cmd("copen")
    vim.notify(string.format("Found %d results", #qf_list), vim.log.levels.INFO)
  end)
end

---Get codebase statistics
function M.get_stats()
  api.get_stats(function(success, stats)
    if success then
      local msg = string.format(
        "Vector: %d chunks | Keyword: %d chunks | Watcher: %s",
        stats.vector.total_chunks,
        stats.keyword.total_chunks,
        stats.watcher_running and "✓" or "✗"
      )
      vim.notify(msg, vim.log.levels.INFO)
    else
      vim.notify("Failed to get stats: " .. tostring(stats), vim.log.levels.ERROR)
    end
  end)
end

return M
