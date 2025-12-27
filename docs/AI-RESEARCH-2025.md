# MarunochiAI: Deep AI Research & Comparative Analysis
**Research Date**: December 26, 2025
**Researcher**: Claude Sonnet 4.5 (AI Research Mode)
**Project**: MarunochiAI - The Most Powerful Self-Hosted Coding Assistant

---

## Executive Summary

This research document analyzes state-of-the-art approaches in AI learning systems, memory architectures, and agent reasoning - all specifically applied to MarunochiAI's continuous fine-tuning and agentic capabilities.

**Research Scope**:
1. AI Learning Systems & Continuous Fine-Tuning
2. Memory Architectures for AI Agents
3. Agent Architectures & Reasoning Systems

**Methodology**:
- Web research on latest papers (2024-2025)
- Analysis of production systems (Cursor, Claude Code, etc.)
- Benchmark comparison
- Applicability assessment for MarunochiAI

---

## Research Findings

### Part 1: AI Learning Systems & Continuous Fine-Tuning

**Research Completed**: December 26, 2025

This comprehensive section covers state-of-the-art approaches for continuous fine-tuning of coding assistants, specifically tailored for MarunochiAI's use of Qwen2.5-Coder 7B/14B models.

#### 1.1 Continuous Learning Approaches

**Online Learning vs. Periodic Retraining:**

The 2025 consensus favors **hybrid approaches** combining periodic fine-tuning with continuous learning techniques:

- **Periodic Retraining**: Most straightforward but computationally expensive for LLMs. Industry practice in 2025 involves fine-tuning on a rolling basis using PEFT methods (Parameter-Efficient Fine-Tuning) with scheduled jobs (nightly/weekly) that grab latest data and update models in small increments.

- **Continuous/Online Learning**: Cutting edge approach enabling near real-time learning from new data via micro-batches or single samples. More complex but offers superior freshness.

- **MACE Hybrid System** (2025 research): Matches or exceeds continuous retraining while reducing inference latency by up to 63% and sustaining GPU utilization above 85%. Outperforms traditional periodic retraining in latency breakdown across prefill, decode, and finetune stages.

- **In-Context Learning Alternative**: Allows LLMs to update outputs dynamically using real-time inputs without retraining, offering timely responses for temporary adaptations.

**Recommendation for MarunochiAI**: Implement hybrid approach with weekly fine-tuning schedule + active learning data collection + in-context learning for session-specific adaptations. Implement drift detection algorithms to trigger retraining when acceptance rate drops >10% or error rate increases >15%.

### Part 2: Memory Architectures for AI Agents

**Research Completed**: December 26, 2025

#### 2.1 Memory Architecture Taxonomy (2025 State-of-the-Art)

Modern LLM-based agents implement sophisticated memory systems inspired by cognitive science, moving far beyond simple conversation buffers. The field has evolved from monolithic context buffers to modular, multi-component systems.

**Core Memory Categories**:

1. **Episodic Memory**: Captures full interaction context - the situation, thought process, and outcomes. For LLM agents, this means maintaining history of past interactions, conversational turns, and problem-solving steps. Recent systems like A-MEM implement Zettelkasten-inspired note-based structures where each memory unit is enriched with LLM-generated keywords, tags, and contextual descriptions.

2. **Semantic Memory**: Stores essential facts, definitions, concepts, and generalized knowledge distilled from episodic memory. This becomes more compact and efficient for long-term, non-temporal knowledge retention. Often implemented using knowledge graphs or vector databases.

3. **Procedural Memory**: Compiles habitual skills into executable subroutines, enabling unconscious, fluent action. For code agents, this represents learned workflows, common patterns, and compilation of successful problem-solving strategies.

4. **Working Memory**: Current task context and active reasoning state. Systems like HiAgent chunk working memory using subgoals, summarizing fine-grained action-observation pairs once goals are completed.

**Recent Architectural Advances (2024-2025)**:

- **MIRIX Architecture**: Implements Core, Episodic, Semantic, Procedural, Resource, and Knowledge Vault components
- **Episodic-to-Semantic Consolidation**: Transforms successful interaction traces into generalizable skills/rules
- **Intelligent Decay Mechanisms**: Proactively prune or consolidate memories based on composite scores (recency, relevance, utility)
- **Hierarchical Working Memory**: HiAgent-style subgoal chunking for efficient retrieval

#### 2.2 RAG Evolution: From Naive to Agentic (2025)

**RAG Architecture Progression**:

1. **Naive RAG** (2023): Simple retrieve → concatenate → generate pipeline. Limited by static workflows.

2. **Advanced RAG** (2024): Added query rewriting, metadata filtering, hybrid search (vector + keyword), and reranking stages.

3. **Modular RAG** (2024-2025): Complex patterns requiring orchestration and routing. Separable components for different retrieval strategies.

4. **Agentic RAG** (2025 - Current State-of-the-Art):
   - Embedding autonomous AI agents into RAG pipeline
   - Dynamic retrieval strategies with agentic design patterns: reflection, planning, tool use, multi-agent collaboration
   - Query planning and multi-hop reasoning
   - Iterative, targeted queries for comprehensive answers
   - Can retrieve exhaustive datasets and perform structured reasoning

5. **Self-RAG** (2024-2025):
   - Model fine-tuned to make its own retrieval decisions during generation
   - Uses "reflection tokens" to internally decide:
     - If it needs to search for information
     - If retrieved documents are relevant
     - If answers are well-supported by facts
   - Triggers retrieval only when needed (efficiency gains)

6. **Graph RAG** (2025):
   - Microsoft's GraphRAG: Modular graph-based RAG system
   - Combines vector search with knowledge graphs
   - Captures both semantic meaning AND structured relationships
   - Particularly powerful for code understanding (call graphs, dependency graphs, AST relationships)
   - Code-specific implementation: code-graph-rag project uses Tree-sitter parsing + knowledge graphs

**Synergized RAG-Reasoning Frameworks** (2025):
- Agentic LLMs iteratively interleave search and reasoning
- Model identifies knowledge gaps, formulates queries, retrieves via tools (search engines, APIs)
- Integrates retrieved content into evolving solution
- State-of-the-art performance on knowledge-intensive benchmarks

**Key 2025 Research**:
- **INRAExplorer** (July 2025): Multi-tool architecture with comprehensive knowledge graphs
- **Agentic RAG Survey** (Feb 2025): ArXiv 2501.09136
- **Reasoning Agentic RAG** (June 2025): System 1 vs System 2 reasoning patterns

#### 2.3 Code-Specific Embeddings & Models (2025)

**Specialized Code Embedding Models**:

1. **CodeBERT** (Microsoft Research):
   - Bimodal pre-trained model for programming and natural languages
   - Transformer encoder-only architecture
   - Treats code as sequence of tokens
   - Learns bidirectional relationships between code snippets and descriptions
   - Trained on CodeSearchNet dataset

2. **GraphCodeBERT** (Microsoft Research):
   - Based on CodeBERT but incorporates semantic-level structure
   - Leverages data flow in pre-training stage
   - Creates embeddings reflecting program logic, not just text
   - Captures how variables are used throughout code

3. **UniXcoder** (Microsoft Research - Best Overall):
   - Unified cross-modal pre-trained model
   - Incorporates semantic AND syntax information from code comments and AST
   - Supports both encoder and decoder tasks without architecture changes
   - **Performance**: Highest mean F1-score (0.918) with lowest standard deviation (0.041)
   - Most stable performance across benchmarks
   - Further improvements possible with LoRA adapters (rank 32 substantially increases MRR)

**Performance Recommendations for Code Tasks**:
- UniXcoder: Best for stable, high-accuracy code understanding
- GraphCodeBERT: Best when data flow/logic relationships are critical
- CodeBERT: Good baseline for code-NL bidirectional tasks
- OpenAI text-embedding-3-small: Strong general candidate for technical domains

**2025 Enhancement: LoRA Adapters**:
- LoRACode paper (2025) shows LoRA config with rank 32 substantially increases MRR
- One adapter works across all programming languages
- Cost-effective fine-tuning for domain-specific code embedding

#### 2.4 Chunking & Indexing Strategies for Code (2025)

**Optimal Chunk Sizes** (2025 Best Practices):

- **Small chunks** (128-256 tokens): Best for fact-based queries, precise keyword matching
- **Medium chunks** (256-512 tokens): Best for tasks requiring broader context
- **Sweet spot for code**: ~1,800 characters with retrieving more chunks
- **Avoid**: Large chunks (14,400 characters) dilute relevance, drop performance 10-20%

**Advanced Chunking Strategies**:

1. **Hierarchical Chunking** (Recommended for Code):
   - Multi-level chunk hierarchies preserving document structure
   - Top layer: Large chunks summarizing broad sections/themes
   - Next layers: Progressively smaller chunks with finer details
   - For code: File → Class → Method hierarchy
   - Uses hierarchical separators (paragraphs → sentences → words)

2. **Semantic Chunking**:
   - 70% accuracy improvement (best performance)
   - Groups sentences/code blocks by meaning
   - Context-aware boundary detection

3. **Recursive Chunking**:
   - Uses predefined delimiters hierarchically
   - Begins with larger semantic boundaries, recurses into finer splits
   - Good for structured documents/code

4. **LLM-Based Chunking**:
   - Uses language model to analyze structure and decide splits
   - Context-aware decisions about chunk boundaries
   - Most sophisticated but higher cost

5. **Code-Specific Chunking**:
   - Document-based chunking utilizing Python code classes and functions
   - Breaking codebases into meaningful blocks: functions, classes, logical sections
   - Preserves syntactic and semantic boundaries

**Hierarchical Indexing for Code**:
- **Three-tier structure**: File level → Class level → Method level
- Metadata at each level: imports, dependencies, documentation
- Enables both broad codebase queries and specific function lookups
- CocoIndex (2025) demonstrates production-ready infrastructure for real-time semantic codebase indexing

#### 2.5 Context Management: Long Context vs RAG Trade-offs (2025)

**Current Context Window Capabilities**:

- **Claude Sonnet 4**: 200K → recently upgraded to 1M tokens
- **Claude 3.5 Sonnet**: 200K with clear base pricing
- **GPT-4-turbo / GPT-4o**: 128K tokens
- **Gemini 1.5 Pro**: 2M tokens (largest available)

**Performance Reality vs Marketing**:

- Most models break much earlier than advertised
- A model claiming 200K typically becomes unreliable around 130K
- Sudden performance drops at saturation points
- **gpt-4-turbo & claude-3-sonnet**: Performance degrades after ~16K
- **gpt-4o & claude-3.5-sonnet**: Improved long context with little/no deterioration

**Accuracy & Scaling Issues**:

- Accuracy does NOT scale linearly beyond ~64K tokens
- Beyond this point, models lose precision unless combined with RAG
- Structure beats size once sequences get very long
- Vendor docs and independent research prefer retrieval and memory over massive prompts

**Cost Considerations**:

- Unconstrained chat history can reach $1 USD per message (GPT-4 Turbo, Claude 3 Opus)
- Latency and cost scale with context - slower and more expensive on giant prompts
- Before choosing extremely long context, consider if solid RAG is more cost-effective for enterprise/commercial use

**Use Case Guidelines**:

- **Full-document analysis / multi-file reasoning**: 200K-1M range windows
- **Focused tasks (summarization)**: 100K-200K for optimal speed/cost/accuracy balance
- **Heavy-duty enterprise applications**: RAG often better due to cost and performance
- **Best approach**: Hybrid - long context for active reasoning + RAG for knowledge retrieval

#### 2.6 Prompt Caching & Context Optimization (2025)

**Anthropic Claude Prompt Caching** (Generally Available since Dec 17, 2024):

**Performance Benefits**:
- Up to 90% cost reduction for long prompts
- Up to 85% latency reduction
- Game-changing for code agents with large codebases

**2025 Major Updates**:

1. **Cache-Aware Rate Limits** (Early 2025):
   - Prompt cache read tokens no longer count against Input Tokens Per Minute (ITPM) limits
   - For Claude 3.7 Sonnet on Anthropic API
   - Optimize caching to increase throughput and get more from existing rate limits

2. **Simplified Caching**:
   - No manual tracking of cached segments
   - System automatically identifies and uses most relevant cached content
   - AWS Bedrock: Automatically checks for cache hits at previous content block boundaries
   - Looks back ~20 content blocks from specified breakpoint
   - Finds longest matching prefix without predicting optimal checkpoint locations

3. **Token-Efficient Tool Use** (Claude 3.7 Sonnet):
   - Up to 70% reduction in output token consumption
   - Critical for agentic workflows with many tool calls

**Best Practices**:

- Define up to 4 cache breakpoints in prompts
- Default TTL: 5 minutes; Optional: 1-hour cache TTL
- Place cached content at beginning of prompt for optimal performance
- Use cache breakpoints strategically to separate different cacheable sections
- Ideal for: Codebase context, API documentation, style guides

**Integration**: Available in Spring AI, LangChain, and other major frameworks

#### 2.7 Context Compression Techniques (2025)

**LLMLingua Series** (Microsoft Research):

1. **LLMLingua** (EMNLP 2023):
   - Uses well-trained small language model (GPT2-small, LLaMA-7B)
   - Identifies and removes unimportant tokens from prompts
   - Three modules: Budget Controller, Iterative Token-level Compression, Alignment
   - Up to 20x compression with minimal performance loss

2. **LongLLMLingua** (ACL 2024):
   - Specialized for long-context RAG
   - Up to 21.4% performance improvement using only 1/4 of tokens
   - Reduces costs and boosts efficiency

3. **LLMLingua-2** (2024):
   - Small-size prompt compression trained via data distillation from GPT-4
   - BERT-level encoder for token classification
   - Excels in task-agnostic compression
   - Surpasses LLMLingua in handling out-of-domain data
   - 3x-6x faster performance

**State-of-the-Art (2025)**:

- **PISCO**: Achieves very high compression rates without performance loss
- Establishes SOTA for prompt compression in long-context scenarios
- Note: Existing compression techniques can fail to preserve detailed information in long-context scenarios

**Method Categories** (NAACL 2025 Survey):

1. **Hard Prompt Methods**: Remove low-information tokens
2. **Soft Prompt Methods**: Compress text into special tokens

**Framework Integration**: LLMLingua integrated into LangChain and LlamaIndex

#### 2.8 Hybrid Search: Vector + Keyword + Graph (2025)

**Hybrid Search Architecture**:

Combines three retrieval paradigms for optimal accuracy:

1. **Vector Search (Dense Retrieval)**:
   - Semantic understanding via embeddings
   - HNSW (Hierarchical Navigable Small World) or FAISS indexes
   - Captures conceptual similarity

2. **Keyword Search (Sparse Retrieval)**:
   - BM25 algorithm for exact-term precision
   - Inverted indexes (Elasticsearch, OpenSearch)
   - Critical for exact code identifiers, API names

3. **Graph-Based Retrieval**:
   - Knowledge graph relationships
   - Call graphs, dependency graphs for code
   - Captures structural and logical connections

**Technical Implementation**:

- Parallel pipelines: vector index + inverted index
- Combined at query time using Reciprocal Rank Fusion (RRF)
- RRF merges results from different ranking functions (BM25 for text, HNSW/eKNN for vectors)
- Single unified result set

**Performance Gains** (2025 Benchmarks):

- Hybrid search boosts NDCG@10 by 42% over pure vector (Weaviate benchmarks)
- Critical for RAG in LLMs
- 2.3x improvement over pure semantic search in some domains

**Code Retrieval Applications**:

- GitHub Copilot uses hybrid search for code snippets and API documentation
- Combines syntactic matching with semantic understanding
- Voyage AI's code-specific models optimized for this use case

**Advanced Approaches**:

- **All-in-one graph-based index**: Isolated heterogeneous edge storage integrating multiple retrieval paths
- Optimizations: Hybrid distance acceleration, RNG-IP joint pruning, keyword-aware neighbor recycling
- Graph-based analysis for detecting patterns (e.g., fraud detection in finance)

#### 2.9 Embedding Reranking: Voyage AI & Cohere (2025)

**Why Reranking Matters**:

Initial retrieval (embedding search) casts a wide net; reranking intelligently reorders results by deeply analyzing query-result relationships, evaluating code structure and functionality rather than just text similarity.

**Voyage AI** (Code-Optimized):

1. **voyage-code-3**:
   - Optimized specifically for code retrieval tasks
   - Impressive gains over general-purpose embedding models
   - Finds relevant codebase examples instantly, even with different terminology
   - First 200M tokens free per account

2. **rerank-2 and rerank-2-lite**:
   - Multilingual rerankers (next generation)
   - Evaluates code structure and functionality deeply
   - **Performance**: Adding rerank-2 on top of OpenAI v3-large improves accuracy by 13.89%
   - rerank-2-lite: 11.86% improvement
   - **2.3x better** than Cohere reranker (English v3)
   - First 200M tokens free

3. **voyage-3-large** (Latest General Model, Jan 2025):
   - Outperforms OpenAI-v3-large by 9.74% average
   - Outperforms Cohere-v3-English by 20.71% average
   - Ranks first across 8 diverse domains (law, finance, code)
   - Spans 100 datasets

**Cohere Rerank**:

- Ranks multi-aspect and semi-structured documents: emails, tables, JSON, code
- Same precision as long-form text
- Real-time reordering with high accuracy and minimal latency
- Reduces compute costs in RAG systems
- Rerank v3 (English) available

**Cost Comparison**:

- Voyage: $0.06 per 1M tokens (voyage-3.5), $0.02 per 1M tokens (voyage-3.5-lite)
- Free tier: 200M tokens for embeddings + reranking

**Integration**:

- KDB.AI: Cohere, Voyage AI, and Jina AI rerankers
- Zilliz Cloud Pipelines: Seamless Voyage AI integration
- LangChain / LlamaIndex: Both supported

**Recommended Strategy for MarunochiAI**:
Use Voyage AI's voyage-code-3 for embeddings + rerank-2 for code retrieval tasks to maximize accuracy while keeping costs low.

#### 2.10 Incremental Indexing & Performance (ChromaDB 2025)

**ChromaDB Major 2025 Update**:

**Rust-Core Rewrite**:
- 4x faster writes and queries
- Eliminates Python's Global Interpreter Lock (GIL) bottlenecks
- Multithreading support
- Handles billion-scale embeddings with reduced latency

**Real-Time Index Management**:
- Continuous data freshness through incremental updates
- Modify indexes without complete rebuilds
- Delta updates maintain sub-second query times during data drift
- Automated optimization routines adapt index parameters based on evolving query patterns

**Performance Optimization**:

1. **Parallelized Embedding Generation**:
   - Use multithreading/multiprocessing for embedding computation
   - Minimize repeated index update overhead
   - Reduce serialization delays
   - Maximize ingestion throughput

2. **Batch Operations**:
   - Batch inserts significantly faster than individual operations
   - Reduces index update frequency

3. **Incremental Updates**:
   - Only process changed documents
   - Reduces computational overhead
   - Maintains data freshness
   - Critical for code agents watching file changes

**Code-Specific Indexing: CocoIndex** (December 2025):

- Production-ready infrastructure for real-time semantic codebase indexing
- Powered by embeddings + Tree-sitter parsing + vector databases
- Robust semantic code search scaling to massive codebases
- Near-real-time incremental updates
- AST-based understanding of code structure

**Best Practices for MarunochiAI**:

1. Use Tree-sitter for AST parsing
2. Parallelize embedding generation (separate from DB writes)
3. Implement incremental indexing watching file system changes
4. Use ChromaDB's Rust-core for performance
5. Batch operations for initial codebase indexing
6. Delta updates for ongoing file modifications

#### 2.11 SQLite Vector Extensions (2025 State)

**sqlite-vec** (Successor to sqlite-vss):

**Key Features**:
- Written in pure C with zero dependencies
- Runs anywhere SQLite runs: Linux, MacOS, Windows, WASM browsers, Raspberry Pi
- K-Nearest Neighbor (KNN) search
- Multiple distance metrics
- SIMD-accelerated performance (AVX for x86, NEON for ARM)
- Dependency-free and portable

**Technical Implementation**:
- Chunked storage to reduce memory fragmentation
- Bitmaps for validity and metadata filters
- L2/L1 distance calculations with SIMD intrinsics
- Similar API to fts5 Full-Text Search Extension

**sqlite-vss** (Older Extension):
- Based on Faiss library
- Uses vss0 module for virtual tables
- Still maintained but sqlite-vec is preferred

**libSQL/Turso Native Vector Search**:
- No extension needed in Turso or libSQL
- Native vector column type: F32_BLOB(3) for arrays of 32-bit floats
- Built into every libSQL build

**Embedding Storage**:
- Insert vectors as JSON or raw bytes
- Compact binary format supported
- Integration with OpenAI, Nomic, Ollama, Hugging Face embeddings

**Use Cases**:
- Eliminates need for Pinecone, Weaviate, or FAISS
- Ideal for simpler deployments with fewer dependencies
- Perfect for edge deployment or single-binary applications
- MarunochiAI can use for local interaction storage + vector search

**Integration with LangChain**: SQLiteVec officially supported

#### 2.12 Production Framework Comparison: LangChain vs LlamaIndex (2025)

**LangChain**:

**Strengths**:
- Excels in orchestrating multi-step AI workflows
- Modular architecture for chaining operations
- Integrating external tools
- Memory management retains conversation history for chatbots
- Comprehensive framework: chains, agents, memory, tools
- Extensive integrations: models, vector stores, APIs

**Best For**:
- Complex multi-step workflows and agents
- Applications requiring extensive tool integration
- Conversational AI with rich memory
- Workflow orchestration and routing

**LlamaIndex**:

**Strengths**:
- Focuses on optimizing document indexing and retrieval
- Fastest route to high-quality, production-grade RAG
- 35% boost in retrieval accuracy (2025 benchmark)
- Top choice for document-heavy applications
- 40% faster document retrieval than LangChain (2025 comparison)

**Best For**:
- Document-heavy applications
- High-quality RAG pipelines
- Fast, scalable document retrieval
- Knowledge indexing optimization

**Hybrid Approach** (Production Pattern 2025):

Many production applications use BOTH frameworks:

1. **LlamaIndex** for:
   - Document ingestion
   - Building indices
   - Tuning chunking/reranking
   - Exposing high-quality retriever/query engine

2. **LangChain** for:
   - Orchestrating user flow
   - Choosing tools
   - Calling LlamaIndex retriever
   - Post-processing outputs
   - Routing results to downstream systems

**Decision Framework**:
- If app centers on complex multi-step workflows and agents → LangChain
- If app centers on fast, scalable document retrieval and knowledge indexing → LlamaIndex
- For production code agents → Use both (LlamaIndex for codebase RAG, LangChain for agent orchestration)

#### 2.13 Memory Consolidation & Forgetting Strategies (2025)

**Cognitive Science-Inspired Approaches**:

Modern AI agents implement "active forgetting" - memories are not passively lost, but actively removed or modified based on relevance and recency.

**Hybrid Memory Systems**:

Combine episodic and semantic memory with proactive "Intelligent Decay" mechanisms that prune/consolidate memories based on composite scores:

1. **Recency**: How recently was this memory accessed/created?
2. **Relevance**: How relevant to current/future tasks?
3. **Utility**: User-specified importance weights

**Episodic → Semantic Consolidation**:

**Process**:
1. Agent solves novel problem → stored in episodic memory
2. Background process identifies successful pattern
3. Pattern abstracted into generalizable skill/rule
4. Written to semantic memory for reuse

**When to Consolidate**:
- After N successful applications of same pattern
- During idle/low-activity periods
- Based on importance scoring
- User feedback indicating valuable workflow

**Forgetting Strategies**:

1. **Recency-Based**:
   - Older memories decay unless accessed
   - Exponential decay functions common
   - Access resets decay timer

2. **Importance-Based**:
   - Low-utility memories pruned first
   - Composite scoring: recency × relevance × utility
   - Critical memories protected from pruning

3. **Capacity-Based**:
   - When memory full, remove lowest-scoring memories
   - Different strategies per agent type
   - Some agents prioritize recency, others relevance

4. **Semantic Compression**:
   - Multiple similar episodic memories → single semantic concept
   - Reduces storage while preserving knowledge
   - Example: 10 "debug print statement" fixes → rule "use print for debugging"

**Recent Papers (2025)**:

- "Hindsight is 20/20: Building Agent Memory that Retains, Recalls, and Reflects" (Dec 2025)
- "O-Mem: Omni Memory System for Personalized, Long Horizon, Self-Evolving Agents" (Nov 2025)
- Work on continuous consolidation for lifelong learning (Tarale et al., 2025)

**Recommended for MarunochiAI**:

1. **Short-term (working memory)**: Current coding task, active files, recent edits
2. **Episodic memory**: Past coding sessions, bugs fixed, features implemented
3. **Semantic memory**: Code patterns learned, user preferences, project structure
4. **Procedural memory**: Successful debugging workflows, testing patterns, deployment procedures

Implement intelligent decay with higher weights for:
- User-starred interactions
- Successful problem resolutions
- Frequently accessed patterns

#### 2.14 RAG Evaluation Benchmarks (2025)

**LongBench v2** (2024-2025):

- Assesses LLM ability to handle long-context problems requiring deep understanding
- 503 challenging multiple-choice questions
- Contexts: 8K to 2M words
- Six major task categories
- **Human performance**: 53.7% accuracy (15-minute time constraint)
- **Best model**: 50.1% accuracy (direct answering)
- Demonstrates that even humans struggle with extreme long-context

**InfiniteBench**:

- Cutting-edge benchmark for super long contexts (100K+ tokens)
- Tests models against contexts 10x longer than traditional datasets
- 12 unique tasks assessing different aspects of language processing
- Essential for evaluating emerging capabilities of modern LLMs
- Tests from 1K to 10M+ tokens

**CRUD-RAG**:

- Evaluates RAG systems under CRUD paradigm (Create, Read, Update, Delete)
- Emphasizes generation quality over retrieval path validation
- Specifically designed as comprehensive Chinese benchmark
- Useful for multilingual RAG evaluation

**RAG Performance Findings**:

- Advanced RAG methods significantly outperform existing long-context LLMs
- Particularly strong in tasks requiring intensive reasoning
- Excels in extremely long-context comprehension
- Comprehensive assessments using LongBench, InfiniteBench, and RULER benchmarks

**Key Takeaway for MarunochiAI**:

While long context windows are impressive, structured RAG consistently outperforms on:
- Code retrieval tasks
- Multi-file reasoning
- Complex dependency understanding
- Cost-effectiveness at scale

Recommendation: Hybrid approach using Claude Sonnet 4's 1M context for active reasoning + RAG for codebase knowledge retrieval.

### Part 3: Agent Architectures & Reasoning Systems

_Research in progress..._

---

## Comparative Analysis

_Comparison matrix pending research completion..._

---

## Recommendations for MarunochiAI

### Memory Architecture Implementation Plan

Based on the comprehensive research above, here is a concrete architectural plan for MarunochiAI's memory system:

#### 1. Multi-Tier Memory System

**Working Memory (Current Session)**:
- Active file context (currently open files)
- Recent edits and changes
- Current task/instruction context
- Active reasoning state and subgoals
- Implementation: In-memory data structures + Claude's context window
- Use prompt caching for frequently accessed codebase sections (90% cost reduction)

**Episodic Memory (Interaction History)**:
- Past coding sessions with timestamps
- Bug fixes and their resolutions
- Feature implementations and approaches taken
- User feedback and corrections
- Failed attempts (for learning what doesn't work)
- Storage: SQLite with sqlite-vec extension for hybrid storage
- Schema: Timestamp, task description, context, outcome, user rating

**Semantic Memory (Code Knowledge)**:
- Project structure and architecture understanding
- Common patterns in the codebase
- User preferences and coding style
- Library/framework usage patterns
- Dependency relationships
- Storage: ChromaDB with hierarchical indexing (File → Class → Method)
- Embeddings: UniXcoder for code-specific understanding

**Procedural Memory (Learned Workflows)**:
- Successful debugging workflows
- Testing patterns that work
- Deployment procedures
- Code review processes
- Refactoring strategies
- Storage: Structured JSON in SQLite with versioning
- Consolidation: Episodic patterns → Procedural rules after N successful uses

#### 2. RAG Architecture: Hybrid Agentic RAG + Graph RAG

**Recommended Approach**: Modular Agentic RAG with Graph enhancement

**Components**:

1. **Embedding Layer**:
   - Primary: UniXcoder (best for code, F1=0.918)
   - Fallback: OpenAI text-embedding-3-small for general text
   - Consider LoRA fine-tuning (rank 32) for MarunochiAI-specific patterns

2. **Storage Layer**:
   - ChromaDB (Rust-core 2025 version) for vector storage
   - SQLite with sqlite-vec for interaction history
   - Knowledge Graph for code relationships (call graphs, dependencies, AST)

3. **Chunking Strategy**:
   - Hierarchical chunking for code:
     - Level 1: File-level (includes imports, top-level structure)
     - Level 2: Class-level (includes methods, attributes)
     - Level 3: Method/function-level (implementation details)
   - Chunk size: ~1,800 characters per chunk
   - Use Tree-sitter for AST-aware boundary detection
   - Metadata: file path, language, dependencies, last modified

4. **Retrieval Strategy**:
   - **Hybrid Search**: Vector (semantic) + BM25 (keyword) + Graph (structural)
   - **Agentic Query Planning**: LLM decides retrieval strategy based on query type
     - "Find all uses of X" → Graph traversal
     - "Similar implementations to Y" → Vector search
     - "Exact function name Z" → Keyword search
   - **Multi-hop Reasoning**: For complex queries requiring multiple retrieval rounds
   - **Self-RAG**: Model decides when retrieval is needed vs using existing context

5. **Reranking**:
   - Voyage AI's rerank-2 for code-specific reranking
   - 13.89% accuracy improvement over embeddings alone
   - 2.3x better than Cohere for code tasks
   - Free tier: 200M tokens

6. **Indexing Strategy**:
   - Initial indexing: Batch operations for entire codebase
   - Incremental updates: File system watching with delta updates
   - Parallelize embedding generation (separate from DB writes)
   - Use ChromaDB's automated optimization routines

#### 3. Context Management Strategy

**Hybrid Long Context + RAG**:

1. **Use Claude Sonnet 4's 1M context for**:
   - Active reasoning on current task
   - Multi-file edits in current session
   - Understanding complex refactoring across files

2. **Use RAG for**:
   - Codebase knowledge retrieval
   - Finding similar implementations
   - Understanding project architecture
   - Historical context and patterns

3. **Prompt Caching**:
   - Cache common codebase sections (up to 4 cache breakpoints)
   - 90% cost reduction, 85% latency reduction
   - 1-hour TTL for active development sessions
   - Cache: Project structure, common imports, API documentation

4. **Context Compression**:
   - Use LLMLingua-2 for compressing retrieved context before adding to prompt
   - 3x-6x faster, up to 20x compression with minimal performance loss
   - Particularly useful when RAG returns many relevant chunks

#### 4. Memory Consolidation & Forgetting

**Episodic → Semantic Consolidation**:

- **Trigger**: After 3+ successful uses of same pattern
- **Process**: Background job (runs during idle time)
  1. Identify repeated successful patterns in episodic memory
  2. Abstract into generalizable rule/workflow
  3. Store in semantic memory with confidence score
  4. Keep original episodic memories for provenance

**Intelligent Decay**:

- **Composite Score**: (Recency × 0.3) + (Relevance × 0.4) + (User Rating × 0.3)
- **Recency**: Exponential decay, access resets timer
- **Relevance**: Embedding similarity to current project patterns
- **User Rating**: Explicit thumbs up/down, implicit (adopted suggestions)

**Protected Memories** (never forgotten):
- User-starred interactions
- Explicitly saved workflows
- High-rated successful resolutions (score > 0.9)

**Pruning Strategy**:
- When episodic memory > 10,000 interactions, prune bottom 20% by score
- Run weekly consolidation job
- Compress similar episodic memories into semantic summaries

#### 5. Technology Stack Recommendations

**Vector Database**: ChromaDB (Rust-core 2025)
- 4x faster than old version
- Incremental indexing support
- Python-native, easy integration

**Relational Storage**: SQLite with sqlite-vec extension
- Interaction history
- User preferences
- Session management
- Vector search for episodic memory retrieval
- Zero dependencies, portable

**Embedding Models**:
- Primary: UniXcoder (Microsoft Research)
- Reranking: Voyage AI rerank-2
- Fallback: OpenAI text-embedding-3-small

**Graph Database** (for code relationships):
- NetworkX for in-memory graph operations
- Persistent storage in SQLite as edge lists
- Build from Tree-sitter AST parsing

**RAG Framework**:
- LlamaIndex for RAG pipeline (retrieval optimization)
- LangChain for agent orchestration (workflow management)
- Use both: LlamaIndex provides retriever, LangChain orchestrates agent

**Code Parsing**: Tree-sitter
- Multi-language AST parsing
- Fast incremental parsing
- Used by GitHub, Neovim, others

#### 6. Performance Targets

**Indexing**:
- Initial codebase indexing: < 1 minute for 10,000 files
- Incremental update: < 100ms per file change
- Embedding generation: Parallelized, target 1,000 files/minute

**Retrieval**:
- Query latency: < 200ms for hybrid search
- Top-K retrieval: K=20 candidates, rerank to top-5
- Cache hit rate: > 80% for common queries

**Memory Footprint**:
- ChromaDB index: ~1GB per 100,000 code chunks
- SQLite database: ~100MB per 10,000 interactions
- In-memory working state: < 500MB

**Cost Optimization**:
- Prompt caching reduces token costs by 90%
- Voyage AI free tier covers 200M tokens
- ChromaDB self-hosted (no API costs)
- SQLite self-hosted (no API costs)
- Primary cost: LLM inference (Claude API)

#### 7. Implementation Phases

**Phase 1: Basic RAG** (Weeks 1-2)
- ChromaDB integration
- UniXcoder embeddings
- Hierarchical chunking with Tree-sitter
- Simple vector search retrieval
- SQLite for interaction logging

**Phase 2: Hybrid Search** (Weeks 3-4)
- Add BM25 keyword search
- Implement RRF for result fusion
- Add Voyage AI reranking
- Build basic knowledge graph from imports/calls

**Phase 3: Agentic RAG** (Weeks 5-6)
- Query planning (LLM decides retrieval strategy)
- Multi-hop reasoning for complex queries
- Self-RAG (model decides when to retrieve)
- Reflection tokens for quality assessment

**Phase 4: Memory System** (Weeks 7-8)
- Episodic memory storage in SQLite
- Semantic memory in ChromaDB with hierarchical indexing
- Basic consolidation (manual triggers)
- User rating system

**Phase 5: Advanced Features** (Weeks 9-12)
- Automated episodic → semantic consolidation
- Intelligent decay and forgetting
- Procedural memory learning
- Graph RAG for structural queries
- Incremental indexing optimization
- Prompt caching integration
- Context compression with LLMLingua-2

#### 8. Success Metrics

**Retrieval Quality**:
- NDCG@10 > 0.8 (Normalized Discounted Cumulative Gain)
- MRR > 0.7 (Mean Reciprocal Rank)
- Precision@5 > 0.85

**User Experience**:
- Average query latency < 2 seconds (end-to-end)
- User acceptance rate > 70% for suggestions
- Session continuity: Remembers context across sessions

**System Performance**:
- Incremental indexing: < 100ms per file
- Memory footprint: < 2GB for typical project
- Cache hit rate: > 80%

**Learning Effectiveness**:
- Semantic memory grows with usage
- Repeated pattern recognition improves over time
- User corrections reduce repeated mistakes

### Key Differentiators for MarunochiAI

1. **Cognitive-Inspired Memory**: Four-tier memory (working, episodic, semantic, procedural) unlike competitors
2. **Code-Specific Embeddings**: UniXcoder + Voyage AI for best code understanding
3. **Hybrid Agentic RAG**: Combines vector, keyword, and graph search with intelligent query planning
4. **Self-Learning**: Episodic → Semantic consolidation learns user patterns
5. **Cost Optimization**: Prompt caching (90% reduction) + self-hosted storage
6. **Privacy-First**: All memory stored locally (ChromaDB + SQLite)
7. **Cross-Session Intelligence**: Remembers past sessions, learns from mistakes
8. **Hierarchical Code Understanding**: File → Class → Method indexing
9. **Intelligent Forgetting**: Active decay prevents memory bloat while retaining important patterns
10. **Production-Ready Framework**: LlamaIndex + LangChain for reliability

---

## References

### Memory Architectures & Agent Memory Systems

1. [Memory in LLM-based Multi-agent Systems: Mechanisms, Challenges, and Collective](https://www.techrxiv.org/users/1007269/articles/1367390/master/file/data/LLM_MAS_Memory_Survey_preprint_/LLM_MAS_Memory_Survey_preprint_.pdf?inline=true) - TechRxiv Survey
2. [Memory Mechanisms in LLM Agents](https://www.emergentmind.com/topics/memory-mechanisms-in-llm-based-agents) - EmergentMind
3. [A Simple Yet Strong Baseline for Long-Term Conversational Memory of LLM Agents](https://arxiv.org/html/2511.17208v2) - ArXiv 2511.17208
4. [AI Agents with Memory Systems: Cognitive Architectures for LLMs](https://www.bluetickconsultants.com/building-ai-agents-with-memory-systems-cognitive-architectures-for-llms/) - BlueTick Consultants
5. [Long-term Memory in LLM Applications](https://langchain-ai.github.io/langmem/concepts/conceptual_guide/) - LangChain LangMem
6. [Agent-Memory-Paper-List](https://github.com/Shichun-Liu/Agent-Memory-Paper-List) - GitHub Repository
7. [A Survey on the Memory Mechanism of Large Language Model based Agents](https://arxiv.org/abs/2404.13501) - ArXiv 2404.13501
8. [Making Sense of Memory in AI Agents](https://www.leoniemonigatti.com/blog/memory-in-ai-agents.html) - Leonie Monigatti
9. [Exploring Agent Procedural Memory](https://arxiv.org/html/2508.06433v2) - ArXiv 2508.06433
10. [Why Memory Matters in LLM Agents](https://skymod.tech/why-memory-matters-in-llm-agents-short-term-vs-long-term-memory-architectures/) - Skymod Tech
11. ["My agent understands me better": Integrating Dynamic Human-like Memory Recall and Consolidation in LLM-Based Agents](https://arxiv.org/html/2404.00573) - ArXiv 2404.00573
12. [Memory Management and Contextual Consistency for Long-Running Low-Code Agents](https://arxiv.org/html/2509.25250) - ArXiv 2509.25250
13. [Position: Episodic Memory is the Missing Piece for Long-Term LLM Agents](https://arxiv.org/pdf/2502.06975) - ArXiv 2502.06975
14. [Memory for AI Agents: Designing Persistent, Adaptive Memory Systems](https://medium.com/@20011002nimeth/memory-for-ai-agents-designing-persistent-adaptive-memory-systems-0fb3d25adab2) - Medium

### RAG Architectures & Agentic RAG

15. [RAG in 2025: The enterprise guide to retrieval augmented generation, Graph RAG and agentic AI](https://datanucleus.dev/rag-and-agentic-ai/what-is-rag-enterprise-guide-2025) - Data Nucleus
16. [Agentic RAG with Knowledge Graphs for Complex Multi-Hop Reasoning](https://arxiv.org/abs/2507.16507) - ArXiv 2507.16507
17. [Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG](https://arxiv.org/abs/2501.09136) - ArXiv 2501.09136 (Feb 2025)
18. [Reasoning RAG via System 1 or System 2: Survey on Reasoning Agentic RAG](https://arxiv.org/html/2506.10408v1) - ArXiv 2506.10408
19. [The 2025 Guide to Retrieval-Augmented Generation (RAG)](https://www.edenai.co/post/the-2025-guide-to-retrieval-augmented-generation-rag) - Eden AI
20. [AgenticRAG-Survey GitHub Repository](https://github.com/asinghcsu/AgenticRAG-Survey) - GitHub
21. [Agentic RAG: A Guide to Building Autonomous AI Systems](https://blog.n8n.io/agentic-rag/) - n8n Blog
22. [HopRAG: Multi-Hop Reasoning for Logic-Aware RAG](https://www.researchgate.net/publication/394272084_HopRAG_Multi-Hop_Reasoning_for_Logic-Aware_Retrieval-Augmented_Generation) - ResearchGate
23. [MultiHop-RAG: Benchmarking RAG for Multi-Hop Queries](https://openreview.net/forum?id=t4eB3zYWBK) - OpenReview

### Graph RAG & Code Understanding

24. [Microsoft GraphRAG: A modular graph-based RAG system](https://github.com/microsoft/graphrag) - GitHub
25. [Beyond Naive RAG: From Vector Soup to Hindsight Memory & Temporal Reasoning](https://medium.com/@ajayverma23/beyond-naive-rag-from-vector-soup-to-hindsight-memory-temporal-reasoning-ae5e795f6943) - Medium
26. [code-graph-rag: Query and edit multi-language codebases with AI and knowledge graphs](https://github.com/vitali87/code-graph-rag) - GitHub
27. [2025 Ultimate Guide to Open-Source RAG Frameworks](https://www.morphik.ai/blog/guide-to-oss-rag-frameworks-for-developers) - Morphik
28. [Advanced RAG: Architecture, Techniques, Applications](https://www.leewayhertz.com/advanced-rag/) - LeewayHertz
29. [Intro to GraphRAG](https://graphrag.com/concepts/intro-to-graphrag/) - GraphRAG.com
30. [Advanced RAG: LongRAG, Self-RAG and GraphRAG Explained](https://www.glukhov.org/post/2025/11/advanced-rag-variants-longrag-self-rag-graphrag/) - Rost Glukhov
31. [RAG Tutorial: How to Build a RAG System on a Knowledge Graph](https://neo4j.com/blog/developer/rag-tutorial/) - Neo4j

### Code Embeddings: CodeBERT, GraphCodeBERT, UniXcoder

32. [CodeBERT GitHub Repository](https://github.com/microsoft/CodeBERT) - Microsoft Research
33. [What embedding models work best for code and technical content?](https://zilliz.com/ai-faq/what-embedding-models-work-best-for-code-and-technical-content) - Zilliz
34. [A Comprehensive Review of Code Embedding Models](https://mgx.dev/insights/e2514404483f4074b652b8f9396dc21b) - MGX.dev
35. [Code Intelligence - Microsoft Research](https://www.microsoft.com/en-us/research/project/code-intelligence/) - Microsoft
36. [LoRACode: LoRA Adapters for Code Embeddings](https://arxiv.org/pdf/2503.05315) - ArXiv 2503.05315
37. [UniXcoder README](https://github.com/microsoft/CodeBERT/blob/master/UniXcoder/README.md) - Microsoft CodeBERT
38. [One Adapter for All Programming Languages?](https://arxiv.org/pdf/2303.15822) - ArXiv 2303.15822
39. [Unveiling Code Pre-Trained Models: Investigating Syntax and Semantics Capacities](https://dl.acm.org/doi/10.1145/3664606) - ACM TOSEM

### Chunking Strategies for RAG

40. [Mastering Chunking Strategies for RAG: Best Practices & Code Examples](https://community.databricks.com/t5/technical-blog/the-ultimate-guide-to-chunking-strategies-for-rag-applications/ba-p/113089) - Databricks
41. [Chunking strategies for RAG tutorial using Granite](https://www.ibm.com/think/tutorials/chunking-strategies-for-rag-with-langchain-watsonx-ai) - IBM
42. [Evaluating the Ideal Chunk Size for a RAG System using LlamaIndex](https://www.llamaindex.ai/blog/evaluating-the-ideal-chunk-size-for-a-rag-system-using-llamaindex-6207e5d3fec5) - LlamaIndex
43. [Best Chunking Strategies for RAG in 2025](https://www.firecrawl.dev/blog/best-chunking-strategies-rag-2025) - Firecrawl
44. [What is the optimal chunk size for RAG applications?](https://milvus.io/ai-quick-reference/what-is-the-optimal-chunk-size-for-rag-applications) - Milvus
45. [9 Chunking Strategies to Improve RAG Performance](https://www.nb-data.com/p/9-chunking-strategis-to-improve-rag) - NB Data
46. [Document Chunking for RAG: 9 Strategies Tested](https://langcopilot.com/posts/2025-10-11-document-chunking-for-rag-practical-guide) - LangCopilot
47. [5 Advanced Types of Chunking Strategies in RAG](https://www.f22labs.com/blogs/5-advanced-types-of-chunking-strategies-in-rag-for-complex-data/) - F22 Labs
48. [Long-Context Isn't All You Need: Impact of Retrieval & Chunking on Finance RAG](https://www.snowflake.com/en/engineering-blog/impact-retrieval-chunking-finance-rag/) - Snowflake
49. [Chunking Strategies to Improve Your RAG Performance](https://weaviate.io/blog/chunking-strategies-for-rag) - Weaviate

### Long Context Windows vs RAG

50. [Manus 1.5 vs Gemini vs Claude vs GPT-4: Big Project Comparison 2025](https://skywork.ai/blog/ai-agent/manus-1-5-vs-gemini-vs-claude-vs-gpt-4-vs-cohere-vs-mistral-big-project-comparison-2025/) - Skywork AI
51. [Towards infinite LLM context windows](https://towardsdatascience.com/towards-infinite-llm-context-windows-e099225abaaf/) - Towards Data Science
52. [Long Context RAG Performance of LLMs](https://www.databricks.com/blog/long-context-rag-performance-llms) - Databricks
53. [Best LLMs for Extended Context Windows](https://research.aimultiple.com/ai-context-window/) - AIMultiple
54. [Context Windows Explained: The Math, Limits, and Future of AI Memory](https://omarbahgatai.substack.com/p/context-windows-explained-the-math) - Omar Bahgat AI
55. [What Is the Best AI Model in 2025? Deep Dive into Gemini 3, GPT-4, and Claude 2.1](https://dev.to/isabellaking/what-is-the-best-ai-model-in-2025-deep-dive-into-gemini-3-gpt-4-and-claude-21-6bm) - DEV Community
56. [LLMs with largest context windows](https://codingscape.com/blog/llms-with-largest-context-windows) - CodingScape
57. [Overcoming Memory Limitations in Generative AI: Managing Context Windows](https://blog.capitaltg.com/overcoming-memory-limitations-in-generative-ai-managing-context-windows-effectively/) - Capital Technology Group
58. [AI API Pricing Comparison (2025): Grok, Gemini, ChatGPT & Claude](https://intuitionlabs.ai/articles/ai-api-pricing-comparison-grok-gemini-openai-claude) - IntuitionLabs
59. [What is a Context Window for Large Language Models?](https://www.datacamp.com/blog/context-window) - DataCamp

### Prompt Caching & Optimization

60. [Prompt caching with Claude - Anthropic News](https://www.anthropic.com/news/prompt-caching) - Anthropic
61. [Prompt Caching Support in Spring AI with Anthropic Claude](https://spring.io/blog/2025/10/27/spring-ai-anthropic-prompt-caching-blog/) - Spring.io
62. [Prompt caching - Claude Docs](https://docs.claude.com/en/docs/build-with-claude/prompt-caching) - Anthropic Documentation
63. [Prompt caching for faster model inference - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html) - AWS
64. [Token-saving updates on the Anthropic API](https://www.anthropic.com/news/token-saving-updates) - Anthropic
65. [claude-cookbooks/prompt_caching.ipynb](https://github.com/anthropics/anthropic-cookbook/blob/main/misc/prompt_caching.ipynb) - Anthropic Cookbook
66. [Prompt Caching Guide (2025) – Cut AI Costs with OpenAI, Anthropic & Google](https://promptbuilder.cc/blog/prompt-caching-token-economics-2025) - PromptBuilder
67. [Prompt Caching with OpenAI, Anthropic, and Google Models](https://www.prompthub.us/blog/prompt-caching-with-openai-anthropic-and-google-models) - PromptHub
68. [Unlocking Efficiency: A Practical Guide to Claude Prompt Caching](https://medium.com/@mcraddock/unlocking-efficiency-a-practical-guide-to-claude-prompt-caching-3185805c0eef) - Medium
69. [Claude Sonnet 4.5: Context Window Expansion, Caching, and Tool Use](https://www.datastudios.org/post/claude-sonnet-4-5-context-window-expansion-caching-and-tool-use-upgrades) - DataStudios

### Context Compression: LLMLingua

70. [LLMLingua GitHub Repository](https://github.com/microsoft/LLMLingua) - Microsoft Research
71. [LLMLingua: Innovating LLM efficiency with prompt compression](https://www.microsoft.com/en-us/research/blog/llmlingua-innovating-llm-efficiency-with-prompt-compression/) - Microsoft Research
72. [LLMLingua Series Official Website](https://www.llmlingua.com/) - Microsoft
73. [LLMLingua: Compressing Prompts for Accelerated Inference](https://arxiv.org/abs/2310.05736) - ArXiv 2310.05736
74. [Understanding and Improving Information Preservation in Prompt Compression](https://arxiv.org/html/2503.19114) - ArXiv 2503.19114
75. [LLMLingua-2](https://llmlingua.com/llmlingua2.html) - Official Site
76. [Prompt-Compression-Survey GitHub](https://github.com/ZongqianLi/Prompt-Compression-Survey) - NAACL 2025 Oral
77. [LLMLingua ACL Anthology](https://aclanthology.org/2023.emnlp-main.825/) - EMNLP 2023

### Hybrid Search: Vector + Keyword + Graph

78. [Hybrid Search: Vector + Keyword Techniques for better RAG retrieval](https://www.machinelearningplus.com/gen-ai/hybrid-search-vector-keyword-techniques-for-better-rag/) - ML Plus
79. [Hybrid search: Definition, how it works, benefits](https://www.meilisearch.com/blog/hybrid-search) - Meilisearch
80. [Hybrid Retrieval-Augmented Generation Systems](https://medium.com/@adnanmasood/hybrid-retrieval-augmented-generation-systems-for-knowledge-intensive-tasks-10347cbe83ab) - Medium
81. [Hybrid Search - Azure AI Search](https://learn.microsoft.com/en-us/azure/search/hybrid-search-overview) - Microsoft
82. [A Practical Guide to Hybrid Search](https://celerdata.com/glossary/hybrid-search) - CelerData
83. [Understanding hybrid search RAG for better AI answers](https://www.meilisearch.com/blog/hybrid-search-rag) - Meilisearch
84. [Weaviate GraphQL: Python Hybrid Search Implementations 2026](https://www.johal.in/weaviate-graphql-python-hybrid-search-implementations-2026/) - Johal.in
85. [Best Vector Databases in 2025: A Complete Comparison Guide](https://www.firecrawl.dev/blog/best-vector-databases-2025) - Firecrawl
86. [All-in-one Graph-based Indexing for Hybrid Search on GPUs](https://arxiv.org/html/2511.00855) - ArXiv 2511.00855
87. [Optimizing RAG with Hybrid Search & Reranking](https://superlinked.com/vectorhub/articles/optimizing-rag-with-hybrid-search-reranking) - Superlinked VectorHub

### Embedding & Reranking: Voyage AI & Cohere

88. [Transforming Code Search with Voyage AI](https://blog.continue.dev/transforming-code-search-with-voyage-ai-why-your-continue-assistant-needs-better-embeddings-and-reranking/) - Continue.dev
89. [Rerank | Boost Enterprise Search and Retrieval](https://cohere.com/rerank) - Cohere
90. [Embedding Models: OpenAI vs Gemini vs Cohere](https://research.aimultiple.com/embedding-models/) - AIMultiple
91. [voyage-3-large: the new state-of-the-art embedding model](https://blog.voyageai.com/2025/01/07/voyage-3-large/) - Voyage AI Blog
92. [Voyage AI Embeddings and Rerankers for Search and RAG](https://zilliz.com/blog/voyage-ai-embeddings-and-rerankers-for-search-and-rag) - Zilliz
93. [Text Embedding Models Compared: OpenAI, Voyage, Cohere](https://document360.com/blog/text-embedding-model-analysis/) - Document360
94. [9 Best Embedding Models for RAG](https://www.zenml.io/blog/best-embedding-models-for-rag) - ZenML
95. [rerank-2 and rerank-2-lite: next generation Voyage rerankers](https://blog.voyageai.com/2024/09/30/rerank-2/) - Voyage AI
96. [Rerank in KDB.AI - Documentation](https://code.kx.com/kdbai/latest/use/rerank.html) - KDB.AI
97. [Rerankers - Introduction](https://docs.voyageai.com/docs/reranker) - Voyage AI Docs

### ChromaDB & Incremental Indexing

98. [Leveraging ChromaDB for Vector Embeddings](https://airbyte.com/data-engineering-resources/chroma-db-vector-embeddings) - Airbyte
99. [Chroma DB Vs Qdrant - Key Differences](https://airbyte.com/data-engineering-resources/chroma-db-vs-qdrant) - Airbyte
100. [chromadb PyPI Package](https://pypi.org/project/chromadb/) - PyPI
101. [chroma-core/chroma GitHub](https://github.com/chroma-core/chroma) - GitHub
102. [ChromaDB Performance Tuning: Multithreading 10M Record Inserts](https://openillumi.com/en/en-chromadb-insert-speed-multithread-fix/) - CodeArchPedia
103. [Chroma Indexing and RAG Examples](https://haystack.deepset.ai/cookbook/chroma-indexing-and-rag-examples) - Haystack
104. [Building Intelligent Codebase Indexing with CocoIndex](https://medium.com/@cocoindex.io/building-intelligent-codebase-indexing-with-cocoindex-a-deep-dive-into-semantic-code-search-e93ae28519c5) - Medium (Dec 2025)
105. [Chroma DB: Efficient Storage and Retrieval of Vector Embeddings](https://www.analyticsvidhya.com/blog/2023/07/guide-to-chroma-db-a-vector-store-for-your-generative-ai-llms/) - Analytics Vidhya

### SQLite Vector Extensions

106. [sqlite-vss: A SQLite extension for efficient vector search](https://github.com/asg017/sqlite-vss) - GitHub
107. [sqlite-vec: A vector search SQLite extension](https://github.com/asg017/sqlite-vec) - GitHub
108. [How sqlite-vec Works for Storing and Querying Vector Embeddings](https://medium.com/@stephenc211/how-sqlite-vec-works-for-storing-and-querying-vector-embeddings-165adeeeceea) - Medium
109. [Introducing sqlite-vss](https://observablehq.com/@asg017/introducing-sqlite-vss) - Observable
110. [SQLite Vector - Extension for Vector Search](https://www.sqlite.ai/sqlite-vector) - SQLite.ai
111. [SQLiteVec - LangChain Docs](https://docs.langchain.com/oss/python/integrations/vectorstores/sqlitevec) - LangChain
112. [How to use sqlite-vec to store and query vector embeddings](https://dev.to/stephenc222/how-to-use-sqlite-vec-to-store-and-query-vector-embeddings-58mf) - DEV
113. [vectorwrap: Universal vector search wrapper](https://github.com/mihirahuja1/vectorwrap) - GitHub
114. [Turso brings Native Vector Search to SQLite](https://turso.tech/blog/turso-brings-native-vector-search-to-sqlite) - Turso

### LangChain vs LlamaIndex

115. [LangChain vs LlamaIndex 2025: Complete RAG Framework Comparison](https://latenode.com/blog/platform-comparisons-alternatives/automation-platform-comparisons/langchain-vs-llamaindex-2025-complete-rag-framework-comparison) - Latenode
116. [LangChain vs LlamaIndex (2025) – Which One is Better?](https://www.databasemart.com/blog/langchain-vs-llamaindex) - DatabaseMart
117. [LangChain vs LlamaIndex: Which RAG Framework Wins in 2025?](https://sider.ai/blog/ai-tools/langchain-vs-llamaindex-which-rag-framework-wins-in-2025) - Sider AI
118. [langchain-llamaindex-rag-memory GitHub](https://github.com/Seh83/langchain-llamaindex-rag-memory) - GitHub
119. [LlamaIndex vs. LangChain for RAG Pipelines in 2025](https://medium.com/decoded-by-datacast/llamaindex-vs-langchain-which-should-you-use-for-rag-pipelines-in-2025-f5a12a5d32b6) - Medium
120. [LangChain vs. LlamaIndex (2025): Features, Performance & Best Use Cases](https://devtechinsights.com/langchain-vs-llamaindex-2025/) - Dev Tech Insights
121. [LlamaIndex vs LangChain: Which RAG Framework Fits Your 2025 Stack?](https://sider.ai/blog/ai-tools/llamaindex-vs-langchain-which-rag-framework-fits-your-2025-stack) - Sider AI
122. [Best RAG Frameworks 2025: Benchmarks Inside](https://langcopilot.com/posts/2025-09-18-top-rag-frameworks-2024-complete-guide) - LangCopilot
123. [LangChain vs LlamaIndex 2025: Which Should You Use?](https://mernstackdev.com/langchain-vs-llamaindex-2025/) - MERNStackDev
124. [LlamaIndex vs LangChain: RAG framework differences](https://www.statsig.com/perspectives/llamaindex-vs-langchain-rag) - Statsig

### RAG Benchmarks

125. [Add long-context evaluation benchmarks PR](https://github.com/EleutherAI/lm-evaluation-harness/pull/3256) - GitHub
126. [LongBench v2 Official Site](https://longbench2.github.io/) - LongBench
127. [Does RAG Really Perform Bad In Long-Context Processing?](https://arxiv.org/html/2502.11444) - ArXiv 2502.11444
128. [CRUD-RAG: Comprehensive Chinese Benchmark for RAG](https://dl.acm.org/doi/10.1145/3701228) - ACM TOIS
129. [LongBench GitHub Repository](https://github.com/THUDM/LongBench) - THUDM
130. [InfiniteBench GitHub Repository](https://github.com/OpenBMB/InfiniteBench) - OpenBMB
131. [RAG Evaluation: 2025 Metrics and Benchmarks](https://labelyourdata.com/articles/llm-fine-tuning/rag-evaluation) - Label Your Data
132. [LLM Benchmarks 2025 - Complete Evaluation Suite](https://llm-stats.com/benchmarks) - LLM Stats

---

**Total References**: 132 sources
**Research Period**: December 26, 2025
**Primary Focus**: Memory architectures, RAG systems, code-specific embeddings, and production frameworks for AI coding assistants
