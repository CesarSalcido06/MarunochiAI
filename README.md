# MarunochiAI 🚀

**Fast, Local, Intelligent Coding Assistant**

**Version**: 0.4.0 | **Status**: Production Ready ✅

MarunochiAI is a local-first, AI-powered coding assistant running on your M4 Pro MacBook. Features intelligent dual-model routing, OpenAI-compatible API, and full multi-agent integration with BenchAI.

---

## ⚡ Key Features (v0.4.0)

✅ **Core Features**:
- **🏎️ Blazing Fast**: 27.6 tok/s (7B model), 0.23s first token
- **🧠 Intelligent**: Qwen2.5-Coder beats GPT-4 on HumanEval (88.4% vs 87.1%)
- **🤖 Dual Models**: Auto-routing (7B fast, 14B powerful)
- **🔌 Multi-Agent**: Full A2A Protocol v0.3 integration with BenchAI
- **🔒 Private**: 100% local, no data leaves your machine
- **💰 Cost-Effective**: ~$3/month electricity vs $20+/month cloud APIs

✅ **New in v0.4.0**:
- **📊 Observability**: Correlation IDs, metrics, request callbacks
- **🛡️ Resilience**: Circuit breakers, retry with exponential backoff
- **💾 Local Storage**: SQLite persistence for A2A sync operations
- **⚙️ Centralized Config**: Environment-based configuration management
- **🌐 Multi-Machine**: Network-aware agent discovery (dynamic URLs)

🚧 **Coming Soon** (Optional Enhancements):
- **📚 Learning**: Fine-tuning pipeline (v1.0)
- **🔍 Deep Understanding**: AST parsing + semantic search (v0.5)
- **🤖 Autonomous**: Multi-step agentic execution (v0.6)

---

## 🎯 What Makes It Powerful

**v0.4.0 delivers**:
1. ✅ **Speed** - Local inference (0.2-3s response time)
2. ✅ **Intelligence** - SOTA models (88.4% HumanEval)
3. ✅ **Smart Routing** - Auto-select 7B (fast) or 14B (quality)
4. ✅ **Integration** - OpenAI API + BenchAI multi-agent
5. ✅ **Privacy** - 100% local (no cloud)
6. ✅ **Resilience** - Circuit breakers, retry logic, graceful degradation
7. ✅ **Observability** - Correlation IDs, metrics, structured logging
8. ✅ **Multi-Machine** - Works across network with dynamic URL discovery

**Future versions add**:
- Deep Understanding - AST parsing + semantic search (v0.5)
- Autonomy - Multi-step execution (v0.6)
- Learning - Continuous fine-tuning (v1.0)

---

## 📦 Installation

### Prerequisites

- **M4 Pro MacBook** (or any Apple Silicon with 16GB+ RAM)
- **Python 3.9+**
- **Ollama 0.13.5+**

### Quick Start

```bash
# Clone repository
cd ~/
git clone https://github.com/CesarSalcido06/MarunochiAI.git
cd MarunochiAI

# Install dependencies
pip install -e .

# Download models
ollama pull qwen2.5-coder:7b
ollama pull qwen2.5-coder:14b

# Test installation
marunochithe chat "Write a hello world function"

# Start API server
marunochithe server
```

---

## 🚀 Usage

### Command Line Interface

```bash
# Chat with MarunochiAI
marunochithe chat "Explain this error message"

# Use specific model (7b=fast, 14b=powerful)
marunochithe chat "Refactor this code" --model 14b

# Read file
marunochithe read main.py

# Git status
marunochithe git-status

# Start API server
marunochithe server --port 8765
```

### API Server

```bash
# Start server
marunochithe server

# OpenAI-compatible endpoint
curl -X POST http://localhost:8765/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen2.5-coder:7b",
    "messages": [{"role": "user", "content": "Write hello world in Python"}],
    "stream": false
  }'

# Streaming response
curl -X POST http://localhost:8765/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen2.5-coder:7b",
    "messages": [{"role": "user", "content": "Explain async/await"}],
    "stream": true
  }'
```

### VS Code Integration (Continue.dev)

```json
// ~/.continue/config.json
{
  "models": [
    {
      "title": "MarunochiAI - Fast (7B)",
      "provider": "openai",
      "model": "qwen2.5-coder:7b",
      "apiBase": "http://localhost:8765/v1"
    },
    {
      "title": "MarunochiAI - Best (14B)",
      "provider": "openai",
      "model": "qwen2.5-coder:14b",
      "apiBase": "http://localhost:8765/v1"
    }
  ]
}
```

---

## 🏗️ Architecture (v0.4.0)

```
MarunochiAI v0.4.0 (FastAPI + Python)
├── Inference Layer (Ollama: 7B fast, 14B powerful)
│   ├── Intelligent routing (simple→7B, complex→14B)
│   ├── Streaming support (SSE)
│   └── OpenAI-compatible API
├── A2A Integration (BenchAI multi-agent)
│   ├── Dynamic agent discovery (network-aware URLs)
│   ├── Task delegation with circuit breakers
│   └── Bidirectional sync with local storage
├── Resilience Layer (NEW in v0.4.0)
│   ├── Circuit breakers (per-service)
│   ├── Retry with exponential backoff
│   └── Graceful degradation
├── Observability Layer (NEW in v0.4.0)
│   ├── Correlation IDs for request tracing
│   ├── Metrics collection (latency, throughput)
│   └── Structured logging with Loguru
├── Storage Layer (NEW in v0.4.0)
│   ├── SQLite for experiences/knowledge
│   └── A2A sync persistence
├── CLI Interface (Typer + Rich)
└── Basic Tools (file ops, git, terminal)
```

**Future Architecture** (v0.5+):
```
+ Code Understanding (Tree-sitter AST + ChromaDB semantic search)  [v0.5]
+ Agentic Engine (task planning, self-correction)                  [v0.6]
+ Fine-Tuning Pipeline (QLoRA continuous learning)                  [v1.0]
```

---

## 🤖 Intelligent Model Routing

MarunochiAI automatically selects the optimal model:

- **Simple tasks** (quick questions, simple code) → **7B** (27.6 tok/s, 0.23s TTFT)
- **Complex tasks** (refactoring, architecture) → **14B** (9.5 tok/s, higher quality)

**Keywords for 14B routing**:
- `refactor`, `architecture`, `design pattern`
- `optimize`, `debug`, `async`, `concurrent`
- `test`, `error handling`, `security`

---

## 🔄 Multi-Agent Integration (A2A Protocol v0.3)

**NEW in v1.0.0**: Full BenchAI integration!

### Automatic Task Routing

BenchAI automatically routes coding tasks to MarunochiAI:

```
User Query: "find authentication functions"
     ↓
┌──────────────────────────────────────┐
│  BenchAI (Port 8085)                 │
│  1. Semantic classification: coding  │
│  2. Route to MarunochiAI             │
└─────────┬────────────────────────────┘
          │ POST /v1/a2a/task
          ↓
┌──────────────────────────────────────┐
│  MarunochiAI (Port 8765)             │
│  1. Receive task from BenchAI        │
│  2. Process with Qwen2.5-Coder       │
│  3. Return results                   │
│  4. Auto-report metrics to BenchAI   │
└──────────────────────────────────────┘
```

### Bidirectional Learning

- **MarunochiAI → BenchAI**: Automatic task completion reporting
- **BenchAI → MarunochiAI**: Experience/knowledge sharing
- **Collective Learning**: Both agents improve together

### Quick Start (Multi-Agent)

```bash
# Terminal 1: Start BenchAI (orchestrator)
cd ~/BenchAI/benchai
python3 -m benchai.api.server

# Terminal 2: Start MarunochiAI (code expert)
cd ~/MarunochiAI
marunochithe server

# Terminal 3: Use BenchAI - coding tasks auto-route to MarunochiAI
curl -X POST http://localhost:8085/v1/learning/a2a/route \
  -H "Content-Type: application/json" \
  -d '{"query": "write a binary search function"}'
```

See [A2A Integration Guide](docs/A2A-INTEGRATION.md) for complete documentation.

---

## 📊 Performance (v1.0.0)

### Benchmarks (M4 Pro, Post-GPU Optimization)

| Metric | Result | Status |
|--------|--------|--------|
| **7B Throughput** | 27.6 tok/s | ✅ Excellent |
| **14B Throughput** | 9.5 tok/s | ✅ Good |
| **First Token Latency** | 0.233s | ✅ Excellent (<1s target) |
| **Concurrent Success** | 100% (10/10) | ✅ Perfect |
| **Memory Leaks** | 0 detected | ✅ None |
| **Streaming Stability** | 100% | ✅ Perfect |

### Comparison with Cloud APIs

| Feature | MarunochiAI (Local) | Cloud APIs |
|---------|---------------------|------------|
| **Speed (7B)** | 27.6 tok/s | ~15-25 tok/s |
| **Latency (TTFT)** | 0.233s | 0.5-2s |
| **Privacy** | 100% local | Cloud-based |
| **Cost** | ~$3/month | $20+/month |
| **Offline** | ✅ Yes | ❌ No |

---

## 🧪 Development Status

### ✅ Phase 1: MVP Foundation (v0.3.0) - **COMPLETE**
- [x] Project structure
- [x] Ollama inference engine (7B/14B routing)
- [x] Basic tools (file ops, git, terminal)
- [x] FastAPI server (OpenAI-compatible)
- [x] CLI interface
- [x] A2A Protocol v0.3 integration
- [x] GPU optimization (2.3x speedup)

### ✅ Phase 1.5: Production Hardening (v0.4.0) - **COMPLETE**
- [x] Centralized configuration (config.py)
- [x] Observability middleware (correlation IDs, metrics)
- [x] Resilience layer (circuit breakers, retry logic)
- [x] Local storage for A2A sync (SQLite)
- [x] Dynamic URL discovery for multi-machine deployment
- [x] BenchAI client with circuit breaker integration

### 🚧 Phase 2: Code Understanding (v0.5) - **PLANNED**
- [ ] Tree-sitter AST parsing
- [ ] ChromaDB semantic indexing
- [ ] Hierarchical code chunking
- [ ] Hybrid search (Vector + BM25 + Graph)
- [ ] Incremental file watching

### 🚧 Phase 3: Agentic Capabilities (v0.6) - **PLANNED**
- [ ] Multi-step task planning
- [ ] Self-correction loops
- [ ] Tool orchestration
- [ ] Autonomous debugging

### 🚧 Phase 4: Fine-Tuning (v1.0) - **PLANNED**
- [ ] QLoRA fine-tuning pipeline
- [ ] Continuous learning from user code
- [ ] Domain-specific adaptation

---

## 🛠️ Technology Stack

**Core** (v1.0.0):
- FastAPI, Python 3.9+, asyncio
- Ollama, Qwen2.5-Coder (7B/14B)
- Typer, Rich (CLI)
- pytest, pytest-asyncio (testing)

**Future** (Ready to use):
- Tree-sitter, ChromaDB (Phase 2)
- QLoRA, PEFT (Phase 4)

---

## 📝 Configuration

Create a `.env` file in the project root:

```bash
# Ollama configuration
OLLAMA_HOST=http://localhost:11434

# MarunochiAI server configuration
MARUNOCHITHE_HOST=0.0.0.0        # Bind to all interfaces for network access
MARUNOCHITHE_PORT=8765
MARUNOCHITHE_LOG_LEVEL=INFO

# BenchAI integration (REQUIRED for multi-agent)
BENCHAI_URL=http://192.168.0.213:8085   # BenchAI server address
BENCHAI_AGENT_ID=marunochithe-m4pro     # Unique agent identifier
```

### Multi-Machine Deployment

When running MarunochiAI and BenchAI on different machines:

```bash
# On MarunochiAI machine (e.g., M4 Mac at 192.168.0.182)
MARUNOCHITHE_HOST=0.0.0.0
BENCHAI_URL=http://192.168.0.213:8085  # Points to BenchAI machine

# On BenchAI machine (e.g., 192.168.0.213)
MARUNOCHI_URL=http://192.168.0.182:8765  # Points to MarunochiAI machine
```

**Dynamic URL Discovery**: MarunochiAI automatically returns correct network URLs in agent discovery (`/.well-known/agent.json`) based on the incoming request's host header.

### New v0.4.0 Endpoints

```bash
# Observability
curl http://localhost:8765/v1/observability/health
curl http://localhost:8765/v1/observability/metrics

# Resilience (circuit breaker status)
curl http://localhost:8765/v1/resilience/circuits

# Storage stats
curl http://localhost:8765/v1/storage/stats

# A2A Sync
curl "http://localhost:8765/v1/sync/share?requester=benchai&sync_type=experience"
curl -X POST http://localhost:8765/v1/sync/receive -d '{"from_agent":"benchai",...}'
```

---

## 📖 Documentation

- [A2A Integration Guide](docs/A2A-INTEGRATION.md) - BenchAI multi-agent integration
- [M4 Pro Optimization Guide](docs/M4-PRO-OPTIMIZATION.md) - Performance tuning
- [Validation Report](docs/VALIDATION_REPORT_DEC27.md) - Production readiness
- [Performance Report](docs/PERFORMANCE_OPTIMIZATION_FINAL.md) - GPU optimization results
- [Project Status](docs/PROJECT_STATUS_V1.0.md) - Complete feature status
- [Release Notes](RELEASE_NOTES_V1.0.md) - v1.0.0 release details

---

## 🐛 Known Issues (Non-Critical)

1. **14B Model Throughput** (Low Priority)
   - Current: 9.5 tok/s
   - Expected: 25+ tok/s
   - Cause: M4 Pro memory bandwidth limitation
   - Workaround: Use 7B for most tasks

2. **Health Check Shows "Degraded"** (Cosmetic)
   - Does not affect functionality
   - Inference works perfectly

See [Project Status](docs/PROJECT_STATUS_V1.0.md) for complete details.

---

## 🤝 Contributing

Contributions welcome! MarunochiAI is designed to work with BenchAI and the multi-agent ecosystem.

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

---

## 📜 License

MIT License - see LICENSE file for details

---

## 🙏 Acknowledgments

### Built With
- **Qwen Team** - For the incredible Qwen2.5-Coder models
- **Ollama** - For making local LLM inference accessible
- **FastAPI** - Modern, fast web framework
- **Typer & Rich** - Beautiful CLI framework

### Inspired By
- **Cursor** - Deep refactoring capabilities
- **Aider** - Git-aware code editing
- **Claude Code** - Agentic task execution

### Integrated With
- **BenchAI** - Multi-agent orchestration system

---

## 📞 Support

- **Documentation**: [docs/](./docs/)
- **Issues**: [GitHub Issues](https://github.com/CesarSalcido06/MarunochiAI/issues)
- **Release Notes**: [RELEASE_NOTES_V1.0.md](RELEASE_NOTES_V1.0.md)

---

## 🚀 Quick Reference

```bash
# Installation
pip install -e .

# Start server
marunochithe server

# Chat
marunochithe chat "your question"

# Test API
curl -X POST http://localhost:8765/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "qwen2.5-coder:7b", "messages": [{"role": "user", "content": "hello"}], "stream": false}'

# Health check
curl http://localhost:8765/health
```

---

**MarunochiAI v0.4.0 - Production Ready** ✅

Fast, local, intelligent coding assistant with resilience, observability, and multi-machine support.

**Where the best AI agents sit together on the bench** 🪑

