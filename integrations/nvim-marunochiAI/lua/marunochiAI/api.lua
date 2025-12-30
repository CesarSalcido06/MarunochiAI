-- MarunochiAI API Client
local M = {}

M.config = {
  api_url = "http://localhost:8765",
}

function M.setup(config)
  M.config = vim.tbl_extend("force", M.config, config or {})
end

-- Convert Python dict string to JSON (handles single quotes and None)
local function python_to_json(str)
  str = str:gsub("'", '"')
  str = str:gsub(": None", ": null")
  str = str:gsub(":None", ":null")
  str = str:gsub(": True", ": true")
  str = str:gsub(":True", ":true")
  str = str:gsub(": False", ": false")
  str = str:gsub(":False", ":false")
  return str
end

-- Simple HTTP request using curl
function M.request(endpoint, body, callback)
  local url = M.config.api_url .. endpoint
  local json_body = vim.fn.json_encode(body)

  local cmd = {
    "curl", "-s", "-X", "POST", url,
    "-H", "Content-Type: application/json",
    "-d", json_body,
  }

  vim.fn.jobstart(cmd, {
    stdout_buffered = true,
    on_stdout = function(_, data)
      if data and data[1] ~= "" then
        local raw = table.concat(data, "")
        local ok, result = pcall(vim.fn.json_decode, raw)
        if ok then
          callback(true, result)
        else
          local converted = python_to_json(raw)
          ok, result = pcall(vim.fn.json_decode, converted)
          if ok then
            callback(true, result)
          else
            callback(false, "JSON parse error: " .. raw:sub(1, 100))
          end
        end
      end
    end,
    on_stderr = function(_, data)
      if data and data[1] ~= "" then
        callback(false, table.concat(data, ""))
      end
    end,
  })
end

-- Chat completion (non-streaming)
function M.chat(messages, callback)
  M.request("/v1/chat/completions", {
    messages = messages,
    stream = false,
  }, callback)
end

-- Streaming chat completion
function M.chat_stream(messages, on_token, on_done)
  local url = M.config.api_url .. "/v1/chat/completions"
  local json_body = vim.fn.json_encode({
    messages = messages,
    stream = true,
  })

  local cmd = {
    "curl", "-s", "-N", "-X", "POST", url,
    "-H", "Content-Type: application/json",
    "-d", json_body,
  }

  -- Use a table to track state (avoids closure issues)
  local state = { done = false }

  vim.fn.jobstart(cmd, {
    on_stdout = function(_, data)
      if state.done then return end
      for _, line in ipairs(data) do
        if line:match("^data: ") then
          local json_str = line:sub(7):gsub("^%s+", ""):gsub("%s+$", "")
          if json_str == "[DONE]" then
            state.done = true
            vim.schedule(function()
              if on_done then on_done() end
            end)
            return
          else
            local ok, chunk = pcall(vim.fn.json_decode, json_str)
            if not ok then
              local converted = python_to_json(json_str)
              ok, chunk = pcall(vim.fn.json_decode, converted)
            end
            if ok and chunk and chunk.choices and chunk.choices[1] then
              local delta = chunk.choices[1].delta
              if delta and delta.content then
                on_token(delta.content)
              end
            end
          end
        end
      end
    end,
    on_exit = function()
      -- Only call on_done if not already called
      if not state.done then
        state.done = true
        vim.schedule(function()
          if on_done then on_done() end
        end)
      end
    end,
  })
end

return M
