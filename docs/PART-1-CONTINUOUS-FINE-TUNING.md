# Part 1: AI Learning Systems & Continuous Fine-Tuning for Coding Assistants

**Research Date**: December 26, 2025
**Researcher**: Claude Sonnet 4.5
**Project**: MarunochiAI - Qwen2.5-Coder Continuous Fine-Tuning Strategy

---

## Executive Summary

This document provides comprehensive research on continuous fine-tuning approaches for MarunochiAI's coding assistant, using Qwen2.5-Coder 7B/14B as the base model. Research covers 2024-2025 state-of-the-art methods, production systems, and practical implementation strategies.

**Key Findings**:
1. **QLoRA + TT-LoRA MoE** recommended for multi-language support
2. **KTO → DPO → PPO** progression for alignment (start simple, scale complexity)
3. **Weekly retraining** with drift detection triggers
4. **Multi-dimensional quality scoring** (execution + tests + static analysis + retention)
5. **MinHash LSH deduplication** + SoftDedup for data quality
6. **Shadow → Canary → Blue-Green** deployment with automated rollback

---

## 1. Continuous Learning Approaches

### 1.1 Online Learning vs. Periodic Retraining

**Industry Best Practices (2025)**:

The field has evolved from simple "retrain every N days" to sophisticated hybrid approaches:

**Periodic Retraining**:
- Most straightforward approach but heavy computational lift
- LLMs with billions of parameters require enormous compute
- **2025 Industry Practice**: Fine-tune on rolling basis using PEFT methods
- Many production services: scheduled fine-tune jobs (nightly/weekly)
- Grab latest data, update model in small increments
- Frequency determined by domain volatility

**Continuous/Online Learning**:
- Cutting edge: near real-time learning from new data
- Updates via micro-batches or even one sample at a time
- More complex to implement but superior freshness
- Enables rapid adaptation to evolving user patterns

**MACE Hybrid System** (2025 Research):
- State-of-the-art hybrid LLM serving system
- Matches or exceeds continuous retraining performance
- **63% reduction** in inference latency
- Sustains GPU utilization above 85%
- Improves latency breakdown: prefill, decode, finetune stages
- Compared to periodic retraining: superior across all metrics

**In-Context Learning** (Complementary Approach):
- Allows LLMs to update outputs dynamically using real-time inputs
- Offers timely responses without retraining
- Traditional models rely on periodic retraining (inefficient)
- ICL enables adaptive behavior without parameter updates

**Drift Detection Triggers** (Automated):
- User acceptance rate drops > 10%
- Error rate increases > 15%
- New language/framework introduced
- Significant codebase changes
- Data distribution shift detected

**Recommendation for MarunochiAI**:
```
Initial Schedule: Weekly retraining with 500+ quality examples
+ Drift Detection: Automated triggers based on performance metrics
+ In-Context Learning: Session-specific adaptations
+ Emergency Retraining: If acceptance rate < 50%
= Hybrid approach balancing cost, freshness, and performance
```

### 1.2 Active Learning Strategies

**What Data to Collect** (2025 Best Practices):

Modern code generation systems log rich interaction data for continuous improvement:

1. **Accepted suggestions**: Code user accepts without modification (positive signal)
2. **Rejected suggestions**: Code user ignores/dismisses (negative signal)
3. **Corrected suggestions**: Code user modifies before accepting (**strongest learning signal**)
4. **Execution results**: Whether code runs, test pass rates, runtime errors
5. **User feedback**: Explicit thumbs up/down, bug reports, issue comments
6. **Context quality**: Which context led to better suggestions (files, symbols, imports)
7. **Session patterns**: Workflows producing best outcomes
8. **Time to acceptance**: How quickly user accepts (confidence signal)
9. **Code retention**: Whether accepted code remains after N days (quality signal)
10. **Test coverage**: Whether generated code includes/passes tests

**Recent Research on Active Learning** (2025):

**Process-Supervised Reinforcement Learning** (EMNLP 2025):
- Addresses resource-intensive nature of constructing process-supervised datasets
- **"Mutation/refactoring-execution verification" strategy**
- Uses teacher models to mutate code
- Compiler execution results automatically label correctness
- More granular than outcome-based RL
- Process supervision in code generation still evolving

**Reinforcement Learning from Verifiable Rewards (RLVR)**:
- Emerged as **de facto new major training stage** for LLMs in 2025
- Trains against objective reward functions
- Allows longer optimization than traditional fine-tuning
- High capability per dollar
- Most capability progress defined by longer RL runs
- Gobbling up compute originally intended for pretraining

**Reinforcement Learning from Code Execution Feedback (RLCEF)**:
- Used by Poolside for advanced AI models
- Enhances code generation through execution feedback
- Validates correctness automatically
- Real-world testing loop

**Multi-Agent Adaptive Strategies**:
- SEW's workflow self-evolution
- EvoMAC's "text backpropagation" mechanism
- Automatically adjusts collaboration structures based on feedback
- Behavioral strategies between agents adapt dynamically

**Priority Sampling Strategies**:

1. **Corrected Examples** (Highest Priority):
   - User modifications reveal model blindspots
   - Direct supervision signal for improvement
   - Weight 3x higher than accepted examples

2. **Uncertainty Sampling**:
   - Collect data where model least confident
   - Target areas needing most improvement
   - Use model entropy/probability scores

3. **Diversity Sampling**:
   - Ensure coverage across languages, patterns, complexity levels
   - Avoid oversampling common patterns
   - Track distribution per language/framework

4. **Error-Driven Sampling**:
   - Prioritize examples where code failed execution
   - Learn from mistakes
   - Build robustness

**Recommendation for MarunochiAI**:
```python
# Priority weighting for training data collection
weights = {
    "corrected": 3.0,      # Highest learning signal
    "rejected_with_reason": 2.0,
    "execution_failed": 2.0,
    "accepted": 1.0,       # Baseline
    "rejected_no_reason": 0.5,
}

# Sampling strategy
- Log ALL interactions with UUID tracking
- Track full lifecycle: suggestion → acceptance → execution → retention
- Implement execution feedback loop (test if code works)
- User acceptance rate per file type/language
- Quality score every interaction (multi-dimensional)
```

### 1.3 Curriculum Learning for Code Models

**Recent Research (2024-2025)**:

**Code-Specific Findings** (February 2025):

Study investigated CodeT5 under curriculum learning for code clone detection and code summarization:

- **Contrasting results**: Model exhibited catastrophic forgetting and shortcut learning
- **Performance saturation**: After only first quartile of training
- **Difficulty metrics**: Code length and cyclomatic complexity
- **Surprising finding**: High accuracy achieved early, then plateaus

**Small Code Language Models** (2024):

Well-designed curriculum learning significantly improves accuracy on code execution tasks:

- **Execution tasks**: Substantial improvements vs. conventional training
- **Code completion**: Less significant effect
- **Task-dependent effectiveness**: CL more beneficial for some tasks than others

**Training Strategies Tested**:

- Incremental, sequential, and hybrid CL schedules compared
- All strategies showed saturation after first quartile
- **Implication**: May not need to train on all difficulty levels
- Focus on harder examples after basics mastered

**General LLM Pretraining** (June 2025):

Curriculum learning consistently improves convergence:

- Early and mid-training phases: clear benefits
- Can yield lasting gains as warmup strategy (up to 3.5% improvement)
- **Effective difficulty signals**: compression ratio, lexical diversity, readability
- Structure beats random sampling

**Recommendation for MarunochiAI**:
```
Use curriculum learning as WARMUP strategy during initial fine-tuning:

Phase 1 (Weeks 1-2): Simple, short code examples
  - Single-function implementations
  - Low cyclomatic complexity (<5)
  - Well-documented, clear logic

Phase 2 (Weeks 3-4): Medium complexity
  - Multi-function coordination
  - Moderate complexity (5-10)
  - Some edge cases

Phase 3 (Weeks 5-6): Complex examples
  - Full class implementations
  - High complexity (>10)
  - Advanced patterns, error handling

Monitor for saturation: may not need full progression
Task-dependent: prioritize for code execution over code completion
```

### 1.4 Catastrophic Forgetting Mitigation

**State-of-the-Art Techniques (2025)**:

**1. Context-aware Continual Pretraining (CA-CPT)**:
- Provides model with sample-specific context before adapting weights
- Demonstrates comparable/superior performance on new domain data
- **Consistently mitigates forgetting** of both:
  - General knowledge
  - Specialized instruction-following abilities
- Production-ready approach from 2025 research

**2. Model Growth Strategy**:
- Leverages smaller models to expedite training of larger ones
- Stack LLM shows less degradation
- Particularly effective in reading comprehension
- Suggests enhanced retention capabilities
- Promising for continual learning scenarios

**3. General Instruction Tuning**:
- Helps alleviate forgetting phenomenon during subsequent fine-tuning
- Maintains general capabilities while learning specific tasks
- Balance between specialization and generalization
- Preserve base model knowledge

**4. Simple Graph Continual Learning (SimGCL)**:
- Even minor modifications to LLMs can lead to outstanding results
- Surpasses previous SOTA GNN-based baselines by ~20%
- Under rehearsal-free constraints
- LLMs as foundation for continual graph learning

**Traditional Approaches Still Explored**:

**Elastic Weight Consolidation (EWC)**:
- Adds penalty to loss function
- Disincentivizes adjusting weights important for old tasks
- Computational overhead tracking parameter importance

**Synaptic Intelligence**:
- Similar to EWC
- Disincentivizes major parameter changes
- Tracks parameter importance online during training

**Gradient Episodic Memory (GEM)**:
- Stores and recalls past experiences
- Informs new tasks
- Preserves previously acquired knowledge
- Memory-based approach

**Key Empirical Findings**:

- Catastrophic forgetting observed in LLMs: 1B to 7B parameters
- **Forgetting worsens as model size grows**
- Particularly relevant for Qwen2.5-Coder 7B/14B
- Larger models more susceptible to interference

**TT-LoRA MoE Solution** (April 2025 - **Recommended**):

Most elegant solution to catastrophic forgetting:

- Independently trains lightweight, tensorized low-rank adapters
- Expert adapters specialized for specific tasks
- **Adapters remain frozen** → eliminates inter-task interference
- **No catastrophic forgetting** in multi-task setting
- Uses only 2% of LoRA, 0.3% of Adapters, 0.03% of AdapterFusion parameters
- Outperforms AdapterFusion by 4 points in multi-tasking

**Recommendation for MarunochiAI**:
```
Primary Strategy: TT-LoRA MoE Architecture
├── Keep base model FROZEN
├── Train independent adapters per language/task
├── No interference between adapters
└── Eliminates catastrophic forgetting by design

Supplementary Strategies:
1. Replay Buffer (20% of training batches)
   - Mix old high-quality examples with new data
   - Maintain performance on earlier learned patterns

2. Benchmark Monitoring
   - Run HumanEval/MBPP after each fine-tuning
   - Track performance across ALL programming languages
   - Detect forgetting early

3. Context-aware Continual Pretraining
   - Maintain sample-specific context during updates
   - Preserve general coding knowledge

4. Language-Specific Testing
   - Test Python, JavaScript, Rust, Go independently
   - Ensure no language-specific degradation
```

---

## 2. Fine-Tuning Methods (2025 State-of-the-Art)

### 2.1 QLoRA vs LoRA vs DoRA vs Full Fine-Tuning

**Comprehensive Comparison** (2025 Benchmarks):

| Method | Parameters | Memory Usage | Performance | Best Use Case |
|--------|-----------|--------------|-------------|---------------|
| **Full Fine-Tuning** | 100% | Very High | Baseline | Large budgets, maximum accuracy |
| **LoRA** | 1-5% | Medium | Good | Experimentation, balance |
| **QLoRA** | 1-5% | Low (4x reduction) | Good (slight trade-off) | **Recommended for Qwen2.5-Coder** |
| **DoRA** | 1-5% | Medium | Better than LoRA | Production, robustness needed |
| **QDoRA** | 1-5% | Very Low | Best | Memory-constrained + best accuracy |
| **TT-LoRA MoE** | 0.03-2% | Very Low | Excellent | Multi-task, prevents interference |

**LoRA (Low-Rank Adaptation)**:
- Freezes pretrained model weights
- Injects trainable low-rank decomposition matrices into transformer layers
- Trains only ~1-5% of original parameters
- Balance of quality and efficiency
- Works on single GPUs, ideal for experimentation
- Good baseline approach

**QLoRA (Quantized LoRA)** - **Recommended for MarunochiAI**:
- Maximum memory efficiency
- 4-bit quantization + minimal parameter updates
- **4x reduction** in memory usage vs. LoRA
- Enables large model fine-tuning on consumer hardware
- Slight accuracy trade-off (acceptable for most use cases)
- **Qwen2.5-Coder paper explicitly recommends this method**
- Works with bitsandbytes quantization
- Minimum 18GB VRAM for 7B model

**DoRA (Weight-Decomposed LoRA)**:
- Decomposes pretrained weight into magnitude and directional components
- Fine-tunes both components
- **Consistently outperforms LoRA** across:
  - Large language models
  - Vision-language models
  - Text-to-image generation
- More robust to hyperparameter changes
- Better performance with fewer trainable parameters than LoRA
- NVIDIA research highlights as high-performing alternative
- Best performance, robustness, parameter efficiency

**QDoRA (Quantized DoRA)**:
- Outperforms both full fine-tuning and QLoRA
- Strong on Llama 2 and Llama 3 models
- Particularly effective on Orca-Math dataset
- **Performance boost**:
  - Outperforms QLoRA by 0.19 points (Llama2 7B)
  - Outperforms QLoRA by 0.23 points (Llama3-8B)
- Best when prioritizing memory savings with superior performance

**Best GenAI Fine-Tuning Tools (2025)**:
- Combine efficient training methods (LoRA/QLoRA)
- Robust experiment tracking
- **Recommended starting points**:
  - Axolotl for quick experiments
  - LLaMA-Factory for production
  - Unsloth for 2x speedup (Qwen support)

**Recommendation for MarunochiAI**:
```
Primary Method: QLoRA
├── As recommended in Qwen2.5-Coder paper
├── Use bitsandbytes for 4-bit quantization
├── Minimum Hardware: 18GB VRAM (7B), more for 14B
├── Track: memory usage + model performance
└── Balance: efficiency vs. accuracy

Upgrade Path (if resources allow):
QLoRA → QDoRA (better accuracy, same memory)
      → TT-LoRA MoE (multi-language support)

Tools:
- Unsloth: 2x faster fine-tuning, 70% less VRAM
- Hugging Face Transformers + PEFT + bitsandbytes
- Track experiments with Weights & Biases or MLflow
```

### 2.2 Mixture of LoRA Experts (MoE)

**Recent Developments (2025)** - Critical for Multi-Language Support:

**1. TT-LoRA MoE** (April 2025) - **Highly Recommended**:

Novel computational framework integrating PEFT with sparse MoE routing:

- Addresses scalability challenges in large model deployments
- Independently trains lightweight, tensorized low-rank adapters
- Adapters specialized for specific tasks
- **Expert adapters remain frozen** → eliminates inter-task interference
- **Eliminates catastrophic forgetting** in multi-task setting
- **Extreme efficiency**:
  - Uses only 2% of LoRA parameters
  - 0.3% of Adapters parameters
  - 0.03% of AdapterFusion parameters
- **Performance**: Outperforms AdapterFusion by 4 points in multi-tasking
- **Perfect for MarunochiAI**: Train independent language-specific experts

**2. MoLA (MoE LoRA with Layer-wise Expert Allocation)** (April 2025):

Novel parameter-efficient MoE method:

- Each model layer uses varying number of LoRA experts
- **Key finding**: Allocating more experts to middle layers enhances effectiveness
- Redundancy more obvious in lower layers
- Optimization: distribute experts strategically by layer
- Layer-wise analysis reveals expert importance distribution

**3. DynMoLE** (April 2025) - **Most Recent, Best Performance**:

Hybrid routing strategy:

- Dynamically adjusts expert selection
- Based on Tsallis entropy of router's probability distribution
- **Performance**:
  - Outperforms LoRA by 9.6%
  - Surpasses SOTA MoLA by 2.3%
- Adaptive routing for optimal expert utilization

**4. Riemannian-based MoE-LoRA** (February 2025):

Training strategy inspired by Riemannian Preconditioners:

- Trains LoRA as sub-space projector
- Stabilizes and boosts feature learning
- Multi-space projections for better representations

**General Trends**:
- LoRA + MoE achieves performance comparable to full-parameter fine-tuning
- Much fewer parameters tuned
- Particularly effective for multi-task learning
- Significant improvements in computational and memory efficiency

**Architecture for Multi-Language Code Support**:

```python
# TT-LoRA MoE Architecture for MarunochiAI

Base Model: Qwen2.5-Coder-7B (frozen)

Language-Specific Expert Adapters:
├── python_expert.safetensors    # Trained on Python user data
├── javascript_expert.safetensors # Trained on JS/TS user data
├── rust_expert.safetensors      # Trained on Rust user data
├── go_expert.safetensors        # Trained on Go user data
└── cpp_expert.safetensors       # Trained on C/C++ user data

Router Logic:
- File extension triggers appropriate adapter
- Per-token routing for mixed-language files
- Dynamic expert selection (DynMoLE strategy)

Training Strategy:
1. Collect language-specific user data independently
2. Train each expert adapter separately
3. Experts remain frozen after training → no interference
4. Can add new language experts without affecting existing ones

Layer-wise Expert Allocation (MoLA findings):
- Allocate more experts to middle layers (layers 16-32 for 7B model)
- Lower layers: fewer experts (less redundancy)
- Upper layers: moderate experts (task-specific features)
```

**Recommendation for MarunochiAI**:
```
Implement TT-LoRA MoE for multi-language support:

Advantages:
✓ No catastrophic forgetting (frozen adapters)
✓ Add new languages without retraining existing experts
✓ Extremely parameter efficient (2% of LoRA)
✓ 4-point improvement over standard approaches
✓ Independent training per language
✓ Per-token expert selection for mixed files

Implementation:
1. Start with Python expert (likely most user data)
2. Add JavaScript/TypeScript expert next
3. Gradually add Rust, Go, C++ as data accumulates
4. Use DynMoLE routing for dynamic selection
5. Allocate more experts to middle layers (MoLA)
6. Keep base model frozen at all times
```

### 2.3 RLHF vs DPO vs KTO for Coding Tasks

**Performance on Coding Tasks** (2025 Research):

**PPO/RLHF** - **Best Performance, High Complexity**:

Consistently outperforms across experiments:

- Particularly strong in challenging code competition tasks
- **CodeContest benchmark**:
  - PPO (34B params) outperforms AlphaCode-41B
  - 10@1k improvement: 16.4% → 22.4%
- Across all datasets: PPO outperforms DPO
- Provides improvements where DPO failed (e.g., StackExchange)
- **Used by GitHub Copilot**: Write better code without fake functions

**Critical success factors for PPO**:
- Advantage normalization
- Large batch size
- Exponential moving average (EMA) update for reference model

**Challenges**:
- Complex: requires separate reward model and policy training
- Time-consuming
- Memory intensive
- Unstable during training processes
- Highest resource requirements

**DPO (Direct Preference Optimization)** - **Good Balance**:

Simpler alternative to RLHF:

- No separate reward model or RL required
- Directly optimizes model to adhere to human preferences
- Significant computational efficiency advantages
- Complexity much lower than RLHF
- **LLaDA 1.5** (variance-reduced DPO):
  - Outperforms SFT on HumanEval (+3.0 points)
  - Outperforms SFT on MBPP (+1.8 points)

**Limitations**:
- Might find biased solutions exploiting out-of-distribution responses
- Performance significantly affected by distribution shift
- Distribution gap between model outputs and preference dataset matters

**KTO (Kaizen Preference Optimization)** - **Easiest, Domain-Specific Winner**:

Simpler data requirements:

- As good or better than DPO (1B to 30B parameters)
- For Llama models: **KTO alone matches SFT + DPO combined**
- Better than DPO alone in many scenarios
- **Only requires binary signal** (desirable/not desirable)
  - Much easier data to obtain than preference pairs
  - Simple thumbs up/down, accepted/rejected
- **Very strong in domain-specific tasks** (important for enterprise)
- Ideal when feedback is in binary format or imbalanced examples

**Recent Innovations (2025)**:

**RTO (Reinforced Token Optimization)** - **State-of-the-Art**:
- Integrates DPO and PPO (best of both worlds)
- **Outperforms PPO by 7.5 points** on AlpacaEval 2
- **Outperforms PPO by 4.1 points** on Arena-Hard
- Highest performance in 2025
- Increased complexity but worth it for maximum performance

**UNA Framework** (2025):
- Unifies RLHF/PPO, DPO, and KTO
- Generalized implicit reward function
- Theoretical framework connecting all methods
- Provides mathematical understanding of relationships

**EMNLP 2025 Study**:
- Ranked RLHF algorithms including REINFORCE with Baseline and RSO
- Extensive evaluation across diverse tasks
- Comprehensive performance comparison

**Comparison Summary**:

| Method | Complexity | Data Needs | Code Performance | Best For |
|--------|-----------|------------|------------------|----------|
| **PPO/RLHF** | High | Preference pairs + reward | Best (22.4% CodeContest) | Maximum performance, resources available |
| **DPO** | Medium | Preference pairs | Good (HumanEval +3.0) | Computational efficiency |
| **KTO** | Low | Binary (👍/👎) | Good (matches SFT+DPO) | Easy data collection, domain-specific |
| **RTO** | High | Preference pairs | Best (AlpacaEval +7.5 vs PPO) | State-of-the-art 2025 |

**Recommendation for MarunochiAI**:
```
Progression Strategy: Start Simple → Scale Complexity

Phase 1: KTO (Weeks 1-8)
├── Easiest to implement
├── Collect binary feedback: thumbs up/down, accepted/rejected
├── Track user acceptance data automatically
├── Low complexity, quick wins
└── Expected improvement: 5-10% acceptance rate

Phase 2: DPO (Weeks 9-16)
├── When you have comparative preference data
├── "Model A vs. Model B" preferences
├── More sophisticated than KTO
├── Expected improvement: Additional 3-5% on benchmarks
└── Balance complexity vs. performance

Phase 3: PPO (Weeks 17-24+)
├── If resources allow (complex, expensive)
├── Best performance on code tasks
├── Use execution results as rewards
├── CodeContest-style metrics
└── Expected improvement: Maximum performance

Future: RTO (Production)
├── State-of-the-art 2025
├── Combines DPO + PPO benefits
├── Highest performance
└── When team has experience with PPO

Data Collection Requirements:
- KTO: User clicks accepted/rejected (automatic logging)
- DPO: Comparative examples (generate 2 suggestions, user picks best)
- PPO: Execution results + test pass rates (automated testing)

For Qwen2.5-Coder 7B/14B specifically:
Start with KTO due to simpler data requirements and strong domain-specific performance
```

---

## 3. Data Collection & Quality

### 3.1 What Interactions to Log

**Comprehensive Interaction Logging** (2025 Best Practices):

**Critical Data Points**:

1. **Accepted Suggestions** (Positive Signal):
   - Code user accepts without modification
   - Timestamp, file context, language
   - Surrounding code for context
   - **Confidence signal**: Time to acceptance (quick = high confidence)

2. **Rejected Suggestions** (Negative Signal):
   - Code user ignores or dismisses
   - Partial typing before rejection
   - Alternative chosen instead
   - **Why rejected**: Manual analysis or user feedback

3. **Corrected Suggestions** (**Strongest Learning Signal**):
   - Code user modifies before accepting
   - **Original suggestion** (what model generated)
   - **Final version** (what user actually used)
   - **Diff analysis**: What changes were made
   - **This is gold**: Direct supervision for improvement

4. **Execution Results**:
   - Whether code runs successfully
   - Runtime errors (exception types, messages)
   - Test pass rates
   - Performance metrics (if available)
   - **Verifiable rewards** for RL

5. **User Feedback** (Explicit):
   - Thumbs up/down ratings
   - Bug reports mentioning AI-generated code
   - Issue comments about suggestions
   - Feature requests

6. **Context Quality Tracking**:
   - Which files were in context
   - Which symbols/imports were referenced
   - Recent edits and changes
   - **Learn**: What context leads to better suggestions

7. **Session Patterns**:
   - Workflows producing best outcomes
   - Time of day patterns
   - Project phase (new feature vs bug fix vs refactor)
   - **Learn**: Task-specific optimization

8. **Time Metrics**:
   - Time to acceptance (confidence)
   - Time to modification (complexity)
   - Time to execution (completeness)
   - Time in codebase (retention)

9. **Code Retention** (Quality Signal):
   - Does accepted code remain after 7 days?
   - After 30 days?
   - **High retention** = high quality suggestion
   - **Quick deletion** = low quality

10. **Test Coverage**:
    - Did generated code include tests?
    - Do tests pass?
    - Coverage percentage
    - **Quality indicator**

**Research Insights** (2025):

**GitClear Study**:
- Examined 211M changed lines (2020-2024)
- Repos from Google, Microsoft, Meta, enterprise C-Corps
- AI-assisted code shows measurable quality differences
- Focus: How AI Assistants influence code quality

**Qodo 2025 Report**:
- 76% of developers in "red zone"
- Frequent hallucinations experienced
- Low confidence in AI-generated code
- **Implication**: Quality tracking essential

**Quality In, Quality Out** (ICPC 2025):
- Study of 4.4M functions
- 4.98% exhibited quality issues:
  - Security vulnerabilities
  - Maintainability problems
  - Poor coding practices
- Generated 551K Python functions:
  - 5.85% affected by at least one quality issue
- **Training data quality directly impacts output quality**

**Storage Schema**:

```sql
CREATE TABLE interactions (
    id TEXT PRIMARY KEY,  -- UUID
    timestamp DATETIME,
    user_id TEXT,
    session_id TEXT,

    -- Context
    file_path TEXT,
    language TEXT,
    cursor_position INTEGER,
    context_files TEXT[],  -- Other files in context
    recent_edits JSON,

    -- Suggestion
    suggestion TEXT,
    suggestion_type TEXT,  -- completion, function, class, etc.
    model_version TEXT,
    confidence_score REAL,

    -- User Action
    action TEXT,  -- accepted, rejected, corrected, ignored
    final_code TEXT,  -- If corrected
    time_to_action INTEGER,  -- Milliseconds

    -- Execution
    executed BOOLEAN,
    execution_success BOOLEAN,
    error_message TEXT,
    test_results JSON,

    -- Quality
    quality_score REAL,  -- Multi-dimensional (computed)
    retention_7d BOOLEAN,
    retention_30d BOOLEAN,

    -- Feedback
    user_rating INTEGER,  -- -1, 0, 1
    user_comment TEXT,

    -- Metadata
    created_at DATETIME,
    updated_at DATETIME
);

-- Indexes for fast querying
CREATE INDEX idx_timestamp ON interactions(timestamp);
CREATE INDEX idx_language ON interactions(language);
CREATE INDEX idx_action ON interactions(action);
CREATE INDEX idx_quality ON interactions(quality_score);
```

**Recommendation for MarunochiAI**:
```python
# Comprehensive logging for every suggestion
def log_interaction(suggestion_id, **kwargs):
    """
    Log every code suggestion interaction
    """
    interaction = {
        "id": suggestion_id,
        "timestamp": datetime.now(),

        # Context (captured automatically)
        "file_path": current_file,
        "language": detect_language(current_file),
        "cursor_position": editor.cursor_position,
        "context_files": get_open_files(),
        "recent_edits": get_recent_edits(last_n=10),

        # Suggestion
        "suggestion": generated_code,
        "suggestion_type": classify_suggestion(generated_code),
        "model_version": model.version,
        "confidence_score": model.confidence,

        # User action (captured on user input)
        "action": None,  # Will be updated
        "final_code": None,
        "time_to_action": None,

        # Execution (captured asynchronously)
        "executed": False,
        "execution_success": None,
        "error_message": None,
        "test_results": None,

        # Quality (computed later)
        "quality_score": None,
        "retention_7d": None,
        "retention_30d": None,

        # Feedback
        "user_rating": None,
        "user_comment": None,
    }

    db.insert("interactions", interaction)
    return suggestion_id

# Update when user takes action
def update_interaction_action(suggestion_id, action, final_code=None):
    """
    Update interaction when user accepts/rejects/corrects
    """
    time_to_action = (datetime.now() - get_timestamp(suggestion_id)).total_seconds()

    db.update("interactions", suggestion_id, {
        "action": action,
        "final_code": final_code,
        "time_to_action": time_to_action,
    })

    # If corrected, this is high-value training data
    if action == "corrected":
        mark_for_priority_sampling(suggestion_id)

# Async: Test execution results
async def track_execution(suggestion_id, code):
    """
    Execute code and track results (async, non-blocking)
    """
    try:
        result = await execute_code(code)
        test_results = await run_tests(code)

        db.update("interactions", suggestion_id, {
            "executed": True,
            "execution_success": result.success,
            "error_message": result.error if not result.success else None,
            "test_results": test_results.to_json(),
        })
    except Exception as e:
        db.update("interactions", suggestion_id, {
            "executed": True,
            "execution_success": False,
            "error_message": str(e),
        })

# Periodic: Check retention
def check_retention():
    """
    Periodic job: Check if accepted code still in codebase
    """
    for interaction in db.query("SELECT * FROM interactions WHERE action='accepted' AND retention_7d IS NULL AND timestamp < NOW() - INTERVAL '7 days'"):
        still_exists = check_code_exists(interaction.final_code or interaction.suggestion, interaction.file_path)
        db.update("interactions", interaction.id, {"retention_7d": still_exists})

    # Same for 30-day retention
    for interaction in db.query("SELECT * FROM interactions WHERE action='accepted' AND retention_30d IS NULL AND timestamp < NOW() - INTERVAL '30 days'"):
        still_exists = check_code_exists(interaction.final_code or interaction.suggestion, interaction.file_path)
        db.update("interactions", interaction.id, {"retention_30d": still_exists})

# Compute quality scores
def compute_quality_score(interaction_id):
    """
    Multi-dimensional quality scoring
    """
    interaction = db.get("interactions", interaction_id)

    score = 0
    max_score = 100

    # Execution success (30 points)
    if interaction.execution_success:
        score += 30

    # Test coverage/pass (25 points)
    if interaction.test_results:
        test_pass_rate = interaction.test_results.get("pass_rate", 0)
        score += 25 * test_pass_rate

    # Static analysis (20 points)
    static_analysis = run_static_analysis(interaction.final_code or interaction.suggestion)
    if static_analysis.no_errors:
        score += 10
    if static_analysis.low_complexity:
        score += 10

    # Retention (15 points)
    if interaction.retention_7d:
        score += 7
    if interaction.retention_30d:
        score += 8

    # User feedback (10 points)
    if interaction.user_rating == 1:
        score += 10
    elif interaction.user_rating == -1:
        score -= 10  # Penalty

    # Normalize to 0-100
    quality_score = max(0, min(100, score))

    db.update("interactions", interaction_id, {"quality_score": quality_score})
    return quality_score

# Training data selection
def select_training_data(min_quality=70, min_examples=500):
    """
    Select high-quality examples for training
    """
    examples = db.query(f"""
        SELECT * FROM interactions
        WHERE quality_score >= {min_quality}
        AND action IN ('accepted', 'corrected')
        ORDER BY quality_score DESC
        LIMIT {min_examples * 2}  -- Get extra for deduplication
    """)

    # Deduplicate
    deduplicated = deduplicate_examples(examples)

    # Priority weighting
    weighted = []
    for ex in deduplicated:
        weight = 3.0 if ex.action == 'corrected' else 1.0
        weighted.append((ex, weight))

    return weighted
```

### 3.2 Quality Scoring Mechanisms

**Multi-Dimensional Quality Assessment** (2025):

**Research-Backed Quality Metrics**:

**Training Data Quality Impact** (March 2025):
- Study of 4.4M functions: 4.98% had quality issues
- Generated 551K Python functions: 5.85% affected by issues
- **Removing low-quality functions** = measurable improvement
- Quality In, Quality Out principle validated

**SoftDedup Approach** (2024):
- Avoids deletion, reweights recurring data instead
- Lowers sampling probability of highly common passages
- **Same perplexity with 26% fewer training steps**
- **Boosted downstream accuracy by ~1.8%**
- Preserves information while reducing redundancy

**Multi-Dimensional Scoring Framework**:

```python
def compute_quality_score(interaction):
    """
    Comprehensive quality scoring (0-100)
    """
    dimensions = {}

    # 1. Execution Success (30 points)
    if interaction.execution_success == True:
        dimensions["execution"] = 30
    elif interaction.execution_success == False:
        dimensions["execution"] = 0
    else:
        dimensions["execution"] = 15  # Unknown

    # 2. Test Coverage & Pass Rate (25 points)
    if interaction.test_results:
        test_score = (
            interaction.test_results.get("pass_rate", 0) * 15 +  # 15 points for pass rate
            min(interaction.test_results.get("coverage", 0) / 100 * 10, 10)  # 10 points for coverage
        )
        dimensions["tests"] = test_score
    else:
        dimensions["tests"] = 0

    # 3. Static Analysis (20 points)
    static_analysis = analyze_code(interaction.final_code or interaction.suggestion)

    lint_score = 10 if static_analysis.lint_errors == 0 else max(0, 10 - static_analysis.lint_errors * 2)
    complexity_score = 10 if static_analysis.cyclomatic_complexity < 10 else max(0, 20 - static_analysis.cyclomatic_complexity)

    dimensions["static"] = lint_score + complexity_score

    # 4. User Retention (15 points)
    retention_score = 0
    if interaction.retention_7d:
        retention_score += 7
    if interaction.retention_30d:
        retention_score += 8
    dimensions["retention"] = retention_score

    # 5. User Explicit Feedback (10 points)
    if interaction.user_rating == 1:
        dimensions["feedback"] = 10
    elif interaction.user_rating == -1:
        dimensions["feedback"] = -10  # Penalty for negative feedback
    elif interaction.action == "accepted":
        dimensions["feedback"] = 5  # Implicit positive
    elif interaction.action == "rejected":
        dimensions["feedback"] = -5  # Implicit negative
    else:
        dimensions["feedback"] = 0

    # Compute total (normalize to 0-100)
    total_score = sum(dimensions.values())
    total_score = max(0, min(100, total_score))

    # Store breakdown for analysis
    interaction.quality_dimensions = dimensions
    interaction.quality_score = total_score

    return total_score

# Quality thresholds
QUALITY_THRESHOLDS = {
    "excellent": 90,  # Use for few-shot examples
    "good": 70,       # Use for training
    "acceptable": 50, # Monitor but don't train
    "poor": 30,       # Investigate, don't train
    "bad": 0,         # Filter out, analyze for improvements
}

def filter_training_data(interactions, min_quality=70):
    """
    Filter training data by quality threshold
    """
    high_quality = [
        i for i in interactions
        if compute_quality_score(i) >= min_quality
    ]

    logging.info(f"Filtered {len(interactions)} → {len(high_quality)} examples (quality >= {min_quality})")

    return high_quality

# SoftDedup: Reweight common patterns
def apply_soft_dedup(examples):
    """
    Reweight recurring patterns instead of deleting
    """
    pattern_counts = defaultdict(int)

    # Count pattern occurrences (using embeddings for similarity)
    for ex in examples:
        pattern = get_pattern_signature(ex)
        pattern_counts[pattern] += 1

    # Reweight based on frequency
    weighted_examples = []
    for ex in examples:
        pattern = get_pattern_signature(ex)
        frequency = pattern_counts[pattern]

        # Lower weight for common patterns (diminishing returns)
        # But don't eliminate completely (preserve information)
        weight = 1.0 / (1.0 + np.log(frequency))

        weighted_examples.append((ex, weight))

    return weighted_examples

# Monitor quality trends
def track_quality_trends():
    """
    Weekly job: Analyze quality trends
    """
    weekly_stats = db.query("""
        SELECT
            DATE_TRUNC('week', timestamp) as week,
            AVG(quality_score) as avg_quality,
            COUNT(*) as total_interactions,
            SUM(CASE WHEN action='accepted' THEN 1 ELSE 0 END) as accepted_count
        FROM interactions
        WHERE timestamp > NOW() - INTERVAL '3 months'
        GROUP BY week
        ORDER BY week DESC
    """)

    # Alert if quality dropping
    recent_avg = weekly_stats[0].avg_quality
    baseline_avg = np.mean([w.avg_quality for w in weekly_stats[4:]])  # Last month as baseline

    if recent_avg < baseline_avg * 0.9:  # 10% drop
        alert_team(f"Quality score dropped: {recent_avg:.1f} vs baseline {baseline_avg:.1f}")
```

**Recommendation for MarunochiAI**:
```
Quality Scoring System:
├── Multi-dimensional (5 dimensions, 100 points total)
│   ├── Execution Success: 30 points
│   ├── Test Coverage/Pass: 25 points
│   ├── Static Analysis: 20 points (lint + complexity)
│   ├── User Retention: 15 points (7d + 30d)
│   └── User Feedback: 10 points (explicit + implicit)
│
├── Training Threshold: score >= 70
├── Few-Shot Examples: score >= 90
├── Investigation: score < 30 (learn what's wrong)
│
├── SoftDedup: Reweight common patterns (don't delete)
├── Track Trends: Weekly quality monitoring
└── Alert: If avg quality drops > 10%

Implementation:
1. Compute quality score after each interaction completes
2. Store score + dimensional breakdown for analysis
3. Filter training data by threshold (>= 70)
4. Apply SoftDedup for common pattern reweighting
5. Monitor trends, alert on quality drops
6. Use quality dimensions to identify improvement areas
```

(Continued in next message due to length...)
