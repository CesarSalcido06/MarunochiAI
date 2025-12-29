# MarunochiAI 🚀

**Fast, Local, Intelligent Coding Assistant**

**Version**: 1.0.0 | **Status**: Production Ready ✅

MarunochiAI is a local-first, AI-powered coding assistant running on your M4 Pro MacBook. Features intelligent dual-model routing, OpenAI-compatible API, and full multi-agent integration with BenchAI.

---

## ⚡ Key Features (v1.0.0)

✅ **Working Now**:
- **🏎️ Blazing Fast**: 27.6 tok/s (7B model), 0.23s first token
- **🧠 Intelligent**: Qwen2.5-Coder beats GPT-4 on HumanEval (88.4% vs 87.1%)
- **🤖 Dual Models**: Auto-routing (7B fast, 14B powerful)
- **🔌 Multi-Agent**: Full A2A Protocol v0.3 integration with BenchAI
- **🔒 Private**: 100% local, no data leaves your machine
- **💰 Cost-Effective**: ~$3/month electricity vs $20+/month cloud APIs
- **✅ Production Ready**: 100% stability, comprehensive testing

🚧 **Coming Soon** (Optional Enhancements):
- **📚 Learning**: Fine-tuning pipeline (v4.0)
- **🔍 Deep Understanding**: AST parsing + semantic search (v2.0)
- **🤖 Autonomous**: Multi-step agentic execution (v3.0)

---

## 🎯 What Makes It Powerful

**v1.0.0 delivers**:
1. ✅ **Speed** - Local inference (0.2-3s response time)
2. ✅ **Intelligence** - SOTA models (88.4% HumanEval)
3. ✅ **Smart Routing** - Auto-select 7B (fast) or 14B (quality)
4. ✅ **Integration** - OpenAI API + BenchAI multi-agent
5. ✅ **Privacy** - 100% local (no cloud)
6. ✅ **Stability** - Production-grade (100% test pass rate)
7. ✅ **Cost** - Electricity only

**Future versions add**:
- Learning - Continuous fine-tuning (v4.0)
- Understanding - Deep codebase analysis (v2.0)
- Autonomy - Multi-step execution (v3.0)

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

## 🏗️ Architecture (v1.0.0)

```
MarunochiAI v1.0.0 (FastAPI + Python)
├── Inference Layer (Ollama: 7B fast, 14B powerful)
│   ├── Intelligent routing (simple→7B, complex→14B)
│   ├── Streaming support (SSE)
│   └── OpenAI-compatible API
├── A2A Integration (BenchAI multi-agent)
│   ├── Agent discovery
│   ├── Task delegation
│   └── Bidirectional sync
├── CLI Interface (Typer + Rich)
└── Basic Tools (file ops, git, terminal)
```

**Future Architecture** (v2.0+):
```
+ Code Understanding (Tree-sitter AST + ChromaDB semantic search)  [v2.0]
+ Agentic Engine (task planning, self-correction)                  [v3.0]
+ Fine-Tuning Pipeline (QLoRA continuous learning)                  [v4.0]
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

### ✅ Phase 1: MVP Foundation (v1.0.0) - **COMPLETE**
- [x] Project structure
- [x] Ollama inference engine (7B/14B routing)
- [x] Basic tools (file ops, git, terminal)
- [x] FastAPI server (OpenAI-compatible)
- [x] CLI interface
- [x] A2A Protocol v0.3 integration
- [x] GPU optimization (2.3x speedup)
- [x] Comprehensive testing (100% pass rate)
- [x] Production documentation

### 🚧 Phase 2: Code Understanding (v2.0) - **PLANNED** (Optional)
- [ ] Tree-sitter AST parsing
- [ ] ChromaDB semantic indexing
- [ ] Hierarchical code chunking
- [ ] Hybrid search (Vector + BM25 + Graph)
- [ ] Incremental file watching

**Status**: Fully planned (1,350 LOC spec ready), not started
**Timeline**: Optional enhancement (Week 2-3)

### 🚧 Phase 3: Agentic Capabilities (v3.0) - **PLANNED** (Optional)
- [ ] Multi-step task planning
- [ ] Self-correction loops
- [ ] Tool orchestration
- [ ] Autonomous debugging

**Status**: Design phase
**Timeline**: Optional enhancement (Week 4-5)

### 🚧 Phase 4: Fine-Tuning (v4.0) - **PLANNED** (Optional)
- [ ] QLoRA fine-tuning pipeline
- [ ] Continuous learning from user code
- [ ] Domain-specific adaptation

**Status**: Research phase
**Timeline**: Optional enhancement (Month 2+)

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

Optional `.env` file:

```bash
# Ollama configuration
OLLAMA_HOST=http://localhost:11434

# MarunochiAI configuration
MARUNOCHITHE_PORT=8765
MARUNOCHITHE_LOG_LEVEL=INFO

# BenchAI integration (optional)
BENCHAI_URL=http://localhost:8085
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

**MarunochiAI v1.0.0 - Production Ready** ✅

Fast, local, intelligent coding assistant. Ready to use today!

**Where the best AI agents sit together on the bench** 🪑

