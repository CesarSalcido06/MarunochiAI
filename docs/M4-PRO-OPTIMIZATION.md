# MarunochiAI M4 Pro Optimization Guide

**Hardware**: Apple M4 Pro MacBook
**Date**: December 27, 2025
**Status**: Baseline Performance Documented

---

## Current Performance (Baseline)

### Benchmark Results

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| **7B Throughput** | 12.1 tok/s | 40+ tok/s | ⚠️ Low |
| **14B Throughput** | 9.6 tok/s | 25+ tok/s | ⚠️ Low |
| **First Token Latency** | 0.38s | <1s | ✅ Good |
| **7B Code Quality** | 1/3 | N/A | Basic |
| **14B Code Quality** | 2/3 | N/A | Better |

**Analysis**: Throughput is **significantly lower than expected**. This indicates Ollama may not be fully utilizing the M4 Pro's GPU (Metal acceleration).

---

## M4 Pro Hardware Capabilities

| Component | Specification | Optimal Usage |
|-----------|---------------|---------------|
| CPU | Apple M4 Pro (10-14 cores) | Context processing |
| GPU | 14-20 core GPU (Metal) | Model inference |
| **Unified Memory** | 24-48GB | Shared CPU/GPU pool |
| Neural Engine | 16-core | Not used by Ollama |
| SSD | 512GB - 2TB NVMe | Model storage |

**Key Advantage**: Unified memory allows seamless CPU ↔ GPU data transfer without copying.

---

## Issue Diagnosis

### Why is Throughput Low?

Possible causes:

1. **Ollama Not Using GPU** (Most Likely)
   - Ollama 0.13.5 should use Metal on M4 Pro
   - Check: Activity Monitor → GPU History
   - Expected: 80-90% GPU utilization during inference

2. **Model Not Loaded to GPU**
   - Models may be CPU-only
   - Check: `ollama ps` while model is running

3. **Thermal Throttling**
   - M4 Pro throttles at ~100°C
   - Check: Activity Monitor → CPU/GPU temperature

4. **Memory Pressure**
   - If memory is full, system swaps to disk (slow)
   - Check: Activity Monitor → Memory tab

### How to Verify GPU Usage

```bash
# Run inference in one terminal
ollama run qwen2.5-coder:7b "Write hello world"

# In another terminal, check GPU usage
# macOS Activity Monitor:
# 1. Open Activity Monitor
# 2. Window → GPU History
# 3. Look for Ollama process using GPU

# Or use command line (if iStats installed):
# sudo powermetrics --samplers gpu_power -i 1000 -n 1
```

**Expected**: 80-90% GPU utilization, <20% CPU

**If GPU is 0%**: Ollama is running on CPU only (slow!)

---

## Optimization Strategies

### 1. Verify Ollama is Using Metal (GPU)

Ollama should automatically detect and use Metal on Apple Silicon. Verify:

```bash
# Check Ollama version (needs ≥0.1.10 for Metal)
ollama --version

# Expected: 0.13.5 (has Metal support)

# Check running models
ollama ps

# Expected output should show models loaded in memory
```

If not using GPU, try:

```bash
# Restart Ollama service
pkill ollama
ollama serve &

# Pull model again to force recompilation
ollama pull qwen2.5-coder:7b --force
```

### 2. Optimize Model Quantization

M4 Pro has 24-48GB unified memory. Use appropriate quantization:

| Model | Quantization | Memory | Speed | Quality |
|-------|--------------|--------|-------|---------|
| 7B | Q4_K_M (default) | 4.3GB | Good | Good |
| 7B | Q5_K_M | 5.2GB | Slower | Better |
| 7B | Q8_0 | 7.8GB | Slowest | Best |
| 14B | Q4_K_M (default) | 8.4GB | Good | Good |
| 14B | Q5_K_M | 10.2GB | Slower | Better |

**Recommendation for M4 Pro 24GB**:
- 7B: Use Q4_K_M (default) - balanced
- 14B: Use Q4_K_M (default) - fits in memory
- Draft 0.5B: Use Q8_0 - tiny anyway

### 3. Enable Context Caching

Ollama caches KV (key-value) pairs for faster subsequent responses:

```bash
# Configure cache size (set in Modelfile or via API)
# Larger cache = faster multi-turn conversations

# Example: 8K context with cache
ollama run qwen2.5-coder:7b --context 8192
```

### 4. Adjust Concurrent Requests

M4 Pro can handle multiple models simultaneously due to unified memory:

```python
# In MarunochiAI server.py
# Current: Single request at a time
# Optimized: Allow batching (if Ollama supports)

# Note: Ollama 0.13.5 doesn't support batching natively
# Future: Consider vLLM or llama.cpp for batching
```

### 5. Model Loading to RAM Disk (Optional)

For **instant model loading**, create RAM disk:

```bash
# Create 16GB RAM disk (if you have 48GB total)
hdid -nomount ram://33554432  # 16GB in 512-byte blocks
diskutil eraseVolume HFS+ RAMDisk /dev/diskX  # Replace X

# Mount at /Volumes/RAMDisk
# Copy model
cp ~/.ollama/models/blobs/sha256-* /Volumes/RAMDisk/

# Link back
ln -s /Volumes/RAMDisk/sha256-* ~/.ollama/models/blobs/
```

**Benefit**: Model loads in 1-2 seconds vs 10-15 seconds from SSD

**Trade-off**: Uses 16GB RAM, only practical if you have 48GB total

---

## Advanced Optimizations (For Power Users)

### Option A: Use llama.cpp Directly (Speculative Decoding)

Ollama is built on llama.cpp but doesn't expose all features. For max performance:

1. **Download llama.cpp**:
```bash
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp

# Compile with Metal support
make LLAMA_METAL=1
```

2. **Download Draft Model for Speculative Decoding**:
```bash
# Already have qwen2.5:0.5b via Ollama
# Convert to GGUF if needed, or download directly:
huggingface-cli download Qwen/Qwen2.5-0.5B-Instruct-GGUF \
  qwen2.5-0.5b-instruct-q8_0.gguf --local-dir ~/llm-models/
```

3. **Run with Speculative Decoding**:
```bash
# Find Ollama's model files
ls ~/.ollama/models/blobs/

# Run llama.cpp with draft model
./llama-server \
  --model ~/.ollama/models/blobs/sha256-[14B-model-hash] \
  --draft ~/.ollama/models/blobs/sha256-[0.5B-model-hash] \
  --draft-max 8 \
  --draft-min 4 \
  -ngl 99 \
  --port 11434 \
  -c 8192

# Expected: 2x faster token generation
```

**Benefit**: 2x faster generation with speculative decoding

**Trade-off**: Manual setup, no Ollama integration

### Option B: Flash Attention (llama.cpp)

Enable Flash Attention for longer contexts:

```bash
# Compile llama.cpp with Flash Attention (if supported on Metal)
cmake -B build -DGGML_METAL=ON -DGGML_METAL_FLASH_ATTENTION=ON
cmake --build build --config Release

# Run with Flash Attention
./build/bin/llama-server --model model.gguf --flash-attn
```

**Benefit**: 2x longer context in same memory, 1.5x faster attention

**Status**: May not be available on Metal yet (check llama.cpp docs)

### Option C: Use ExLlamaV2 (Not Recommended for Mac)

ExLlamaV2 is CUDA-only (NVIDIA GPUs). Not applicable to M4 Pro.

---

## Comparison with BenchAI (Linux + RTX 3060)

| Metric | BenchAI (RTX 3060) | MarunochiAI (M4 Pro) | Ratio |
|--------|---------------------|----------------------|-------|
| **Hardware** | RTX 3060 12GB VRAM | M4 Pro 24GB Unified | Different arch |
| **7B Throughput** | 30-40 tok/s (GPU) | 12.1 tok/s | 0.3x (slow!) |
| **14B Throughput** | 20-30 tok/s (GPU) | 9.6 tok/s | 0.4x (slow!) |
| **VRAM/Memory** | 12GB dedicated | 24GB unified | 2x memory |
| **Context** | 8K tokens | 8K tokens | Same |
| **Model Quality** | Qwen2.5-Coder-14B | Qwen2.5-Coder-14B | Same |

**Analysis**:
- M4 Pro has **3x slower throughput** than expected
- Likely cause: Ollama not fully utilizing Metal GPU
- RTX 3060 has dedicated VRAM and CUDA optimizations
- M4 Pro has **2x more memory** which is an advantage for longer contexts

**Recommendation**: Investigate Ollama GPU usage before pursuing advanced optimizations.

---

## Optimization Priority

| Priority | Optimization | Effort | Expected Impact | Status |
|----------|--------------|--------|-----------------|--------|
| 🔴 **HIGH** | Fix Ollama GPU usage | 15 min | 3-4x speedup | TODO |
| 🟡 MEDIUM | Model quantization tuning | 30 min | 10-20% | Optional |
| 🟡 MEDIUM | Context caching | 10 min | Faster multi-turn | Optional |
| 🟢 LOW | RAM disk for models | 20 min | Faster loading | Optional |
| 🟢 LOW | llama.cpp w/ spec decoding | 2 hours | 2x speedup | Advanced |
| 🟢 LOW | Flash Attention | 1 hour | Longer context | Advanced |

---

## Quick Start: Verify and Fix GPU Usage

### Step 1: Check Current GPU Usage

```bash
# Start a long-running inference
ollama run qwen2.5-coder:7b "Write a detailed explanation of binary search with examples" &

# Open Activity Monitor (GUI)
open -a "Activity Monitor"
# Navigate to: Window → GPU History
# Look for Ollama process using GPU cores

# Expected: 70-90% GPU utilization
# If 0%: GPU not being used!
```

### Step 2: Force GPU Reinitialization

```bash
# Kill Ollama
pkill ollama

# Clear cache
rm -rf ~/.ollama/tmp/*

# Restart Ollama
ollama serve &

# Re-pull model (forces recompilation for Metal)
ollama pull qwen2.5-coder:7b
```

### Step 3: Re-run Benchmark

```bash
cd ~/MarunochiAI
python3 scripts/benchmark_performance.py
```

**Expected after fix**:
- 7B: 40-50 tok/s (up from 12.1)
- 14B: 25-30 tok/s (up from 9.6)
- First token: <0.5s (same)

---

## MarunochiAI Configuration

Current inference engine is already optimized for intelligent routing:

```python
# marunochithe/core/inference.py
class InferenceEngine:
    """
    Intelligent 7B/14B routing:
    - Simple tasks (autocomplete, inline) → 7B (fast)
    - Complex tasks (refactor, arch) → 14B (powerful)
    """

    COMPLEX_KEYWORDS = {
        "refactor", "architecture", "design pattern",
        "optimize", "debug", "async", "concurrent",
        "test", "error handling", "security"
    }
```

**Optimization**: Routing logic is good, just need to fix underlying GPU usage.

---

## Expected Performance After Optimization

### Target Metrics (M4 Pro with GPU)

| Metric | Target | How to Achieve |
|--------|--------|----------------|
| 7B Throughput | 40-50 tok/s | Fix GPU usage |
| 14B Throughput | 25-30 tok/s | Fix GPU usage |
| First Token | <0.5s | Already good |
| Code Quality 7B | 1-2/3 | Model limitation |
| Code Quality 14B | 2-3/3 | Already good |

### Comparison: M4 Pro vs RTX 3060 (Optimized)

| Feature | M4 Pro (Optimized) | RTX 3060 (BenchAI) | Winner |
|---------|--------------------|--------------------|--------|
| Speed (7B) | 40-50 tok/s | 30-40 tok/s | 🏆 M4 Pro |
| Speed (14B) | 25-30 tok/s | 20-30 tok/s | Tie |
| Memory | 24-48GB unified | 12GB VRAM | 🏆 M4 Pro |
| Power Usage | 20-30W | 170W (GPU) | 🏆 M4 Pro |
| Context Length | 32K+ | 8K | 🏆 M4 Pro |
| Batching | No | Limited | Tie |
| Cost | Laptop | Desktop | 🏆 M4 Pro |

**Conclusion**: M4 Pro should match or exceed RTX 3060 once GPU is properly utilized!

---

## Troubleshooting

### Issue: Low Throughput (<20 tok/s)

**Symptoms**:
- Benchmark shows 10-15 tok/s
- Activity Monitor shows 0% GPU usage
- CPU usage is high (60-80%)

**Solution**:
1. Check Ollama version: `ollama --version` (needs ≥0.1.10)
2. Restart Ollama: `pkill ollama && ollama serve`
3. Re-pull models: `ollama pull qwen2.5-coder:7b`
4. Verify Metal: Check System Settings → General → About → System Report → Graphics/Displays

### Issue: Memory Pressure

**Symptoms**:
- Activity Monitor shows yellow/red memory pressure
- System is swapping to disk
- Very slow responses (>30s)

**Solution**:
1. Close other apps
2. Reduce model size: Use 7B instead of 14B
3. Reduce context: Use `--context 4096` instead of 8192
4. Upgrade RAM if possible (24GB → 48GB)

### Issue: Thermal Throttling

**Symptoms**:
- Performance degrades after 5-10 minutes
- Fans running at max speed
- M4 Pro temperature >95°C

**Solution**:
1. Ensure good ventilation (don't use on soft surfaces)
2. Clean vents/fans
3. Reduce workload: Lower concurrent requests
4. Consider cooling pad

---

## Future Optimizations

### When Available

1. **Ollama Batching Support**
   - Process multiple requests in parallel
   - Better GPU utilization
   - Status: Not yet in Ollama

2. **Apple Neural Engine Integration**
   - M4 Pro has 16-core Neural Engine
   - Could accelerate certain operations
   - Status: Not used by current LLM frameworks

3. **Apple MLX Framework**
   - Apple's ML framework optimized for Apple Silicon
   - Status: Experimental, not production-ready for LLMs

---

## Benchmark Results Storage

All benchmark results are saved to:
```
/tmp/marunochiAI_benchmark_results.json
```

Re-run benchmarks after optimizations to track improvements:

```bash
cd ~/MarunochiAI
python3 scripts/benchmark_performance.py

# Compare with previous results
cat /tmp/marunochiAI_benchmark_results.json
```

---

## Summary

### Current Status
- ⚠️ Throughput is 3x lower than expected (12 tok/s vs 40+ tok/s target)
- ✅ First token latency is good (0.38s)
- ✅ Code quality acceptable (14B better than 7B)

### Next Steps
1. **Verify Ollama is using GPU** (Activity Monitor)
2. **Fix GPU usage** if needed (restart, re-pull models)
3. **Re-run benchmarks** to confirm improvement
4. **Consider advanced optimizations** only if needed

### Expected Outcome
After fixing GPU usage:
- **3-4x faster** throughput (12 → 40+ tok/s)
- Comparable to BenchAI's RTX 3060
- Better power efficiency and portability

---

*Document generated: December 27, 2025*
*MarunochiAI v0.2.0 - M4 Pro Optimization Guide*
