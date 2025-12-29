-- MarunochiAI API Client (minimal)
local M = {}

M.config = {
  api_url = "http://localhost:8765",
}

function M.setup(config)
  M.config = vim.tbl_extend("force", M.config, config or {})
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
        local ok, result = pcall(vim.fn.json_decode, table.concat(data, ""))
        if ok then
          callback(true, result)
        else
          callback(false, "JSON parse error")
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

  vim.fn.jobstart(cmd, {
    on_stdout = function(_, data)
      for _, line in ipairs(data) do
        if line:match("^data: ") then
          local json_str = line:sub(7)
          if json_str == "[DONE]" then
            if on_done then on_done() end
          else
            local ok, chunk = pcall(vim.fn.json_decode, json_str)
            if ok and chunk.choices and chunk.choices[1].delta and chunk.choices[1].delta.content then
              on_token(chunk.choices[1].delta.content)
            end
          end
        end
      end
    end,
    on_exit = function()
      if on_done then on_done() end
    end,
  })
end

return M
