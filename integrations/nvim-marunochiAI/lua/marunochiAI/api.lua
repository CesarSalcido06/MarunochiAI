---MarunochiAI API client
---@class MarunochiAPI
local M = {}

M.config = nil

---Setup API client
---@param config MarunochiConfig
function M.setup(config)
  M.config = config
end

---Make HTTP request to MarunochiAI API
---@param method string HTTP method
---@param endpoint string API endpoint
---@param body table|nil Request body
---@param callback function Callback with (success, result)
function M.request(method, endpoint, body, callback)
  local url = M.config.api_url .. endpoint
  local curl_cmd = { "curl", "-s", "-X", method, url }

  -- Add headers
  table.insert(curl_cmd, "-H")
  table.insert(curl_cmd, "Content-Type: application/json")

  if M.config.api_key then
    table.insert(curl_cmd, "-H")
    table.insert(curl_cmd, "Authorization: Bearer " .. M.config.api_key)
  end

  -- Add body for POST/PUT
  if body and (method == "POST" or method == "PUT") then
    table.insert(curl_cmd, "-d")
    table.insert(curl_cmd, vim.fn.json_encode(body))
  end

  vim.fn.jobstart(curl_cmd, {
    stdout_buffered = true,
    on_stdout = function(_, data)
      if not data or #data == 0 then
        callback(false, "No response from server")
        return
      end

      local response = table.concat(data, "\n")
      if response == "" then
        callback(false, "Empty response")
        return
      end

      local ok, result = pcall(vim.fn.json_decode, response)
      if not ok then
        callback(false, "Failed to parse JSON: " .. response)
        return
      end

      callback(true, result)
    end,
    on_stderr = function(_, data)
      if data and #data > 0 then
        local err = table.concat(data, "\n")
        if err ~= "" then
          vim.notify("API Error: " .. err, vim.log.levels.ERROR)
        end
      end
    end,
    on_exit = function(_, code)
      if code ~= 0 then
        callback(false, "Request failed with exit code " .. code)
      end
    end,
  })
end

---Search codebase
---@param query string Search query
---@param limit number|nil Result limit
---@param callback function Callback with (success, results)
function M.search_codebase(query, limit, callback)
  M.request("POST", "/v1/codebase/search", {
    query = query,
    limit = limit or M.config.search_limit,
  }, callback)
end

---Index codebase
---@param path string Codebase path
---@param watch boolean Enable file watching
---@param callback function Callback with (success, stats)
function M.index_codebase(path, watch, callback)
  local params = "?codebase_path=" .. vim.fn.shellescape(path)
  if watch then
    params = params .. "&watch=true"
  end

  M.request("POST", "/v1/codebase/index" .. params, nil, callback)
end

---Get codebase stats
---@param callback function Callback with (success, stats)
function M.get_stats(callback)
  M.request("GET", "/v1/codebase/stats", nil, callback)
end

---Chat completion
---@param messages table List of chat messages
---@param callback function Callback with (success, response)
function M.chat_completion(messages, callback)
  M.request("POST", "/v1/chat/completions", {
    model = M.config.model,
    messages = messages,
    stream = false,
  }, callback)
end

---Streaming chat completion
---@param messages table List of chat messages
---@param on_token function Callback for each token
---@param on_done function Callback when done
function M.chat_completion_stream(messages, on_token, on_done)
  local url = M.config.api_url .. "/v1/chat/completions"
  local curl_cmd = {
    "curl",
    "-s",
    "-N",
    "-X",
    "POST",
    url,
    "-H",
    "Content-Type: application/json",
    "-d",
    vim.fn.json_encode({
      model = M.config.model,
      messages = messages,
      stream = true,
    }),
  }

  local buffer = ""

  vim.fn.jobstart(curl_cmd, {
    on_stdout = function(_, data)
      for _, line in ipairs(data) do
        if line:match("^data: ") then
          local json_str = line:sub(7) -- Remove "data: " prefix

          if json_str == "[DONE]" then
            if on_done then
              on_done()
            end
            return
          end

          local ok, chunk = pcall(vim.fn.json_decode, json_str)
          if ok and chunk.choices and chunk.choices[1].delta.content then
            local token = chunk.choices[1].delta.content
            buffer = buffer .. token
            on_token(token)
          end
        end
      end
    end,
    on_exit = function()
      if on_done then
        on_done()
      end
    end,
  })
end

---Health check
---@param callback function Callback with (success, health)
function M.health_check(callback)
  M.request("GET", "/health", nil, callback)
end

return M
