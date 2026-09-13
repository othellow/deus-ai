
# Sprint 2 – RAG Knowledge Engine

## DEUS AI
**Quantic MSSE Capstone Project**

---

# Sprint Goal

Build the Retrieval-Augmented Generation (RAG) Knowledge Engine that enables DEUS AI to semantically search BillyMacDeus' blog content and prepare relevant context for Large Language Models (LLMs).

Sprint 2 transforms raw blog content into a searchable knowledge base using modern AI techniques including text chunking, sentence embeddings, vector databases, and semantic retrieval.

---

# Sprint Objectives

- Implement document chunking
- Generate semantic embeddings
- Store vectors in ChromaDB
- Build semantic retrieval
- Construct LLM-ready prompts
- Prepare the foundation for the DEUS AI Chat backend

---

# Completed Components

## 1. Chunker (`rag/chunker.py`)

Implemented an automated chunking engine that:

- Reads Markdown articles
- Splits documents into overlapping chunks
- Preserves source metadata
- Exports chunk data as JSON

Purpose:

Prepare blog content for semantic embedding.

---

## 2. Embedding Generator (`rag/embedding.py`)

Implemented sentence embedding generation using:

- Sentence Transformers
- all-MiniLM-L6-v2

Each chunk is converted into a high-dimensional semantic vector representing its meaning rather than simple keywords.

Purpose:

Enable semantic similarity search.

---

## 3. Vector Database (`rag/vectordb.py`)

Implemented persistent storage using ChromaDB.

Features include:

- Persistent vector storage
- Metadata preservation
- Efficient semantic indexing

Purpose:

Create the searchable knowledge base powering DEUS AI.

---

## 4. Semantic Retriever (`rag/retriever.py`)

Implemented semantic search capable of:

- Embedding user questions
- Searching ChromaDB
- Returning the most relevant knowledge chunks

Purpose:

Retrieve relevant context for AI responses.

---

## 5. RAG Engine (`rag/rag_engine.py`)

Implemented prompt construction for future LLM integration.

Responsibilities:

- Retrieve relevant blog passages
- Assemble contextual prompts
- Prepare inputs for OpenAI or other LLM providers

Purpose:

Bridge the knowledge base and conversational AI.

---

# Technologies Used

- Python 3.14
- BeautifulSoup
- Pydantic
- Sentence Transformers
- ChromaDB
- Pytest
- Git & GitHub

---

# Current Architecture

```
BillyMacDeus Blog
        │
        ▼
Crawler
        │
        ▼
Parser
        │
        ▼
Cleaner
        │
        ▼
Markdown Exporter
        │
        ▼
Chunker
        │
        ▼
Embedding Generator
        │
        ▼
ChromaDB
        │
        ▼
Retriever
        │
        ▼
RAG Engine
```

---

# Sprint Deliverables

- Semantic document chunking
- AI embedding generation
- Persistent vector database
- Semantic retrieval engine
- Prompt construction for LLMs

---

# Testing

All existing automated tests successfully passed.

```
=============================
6 passed
=============================
```

Manual validation confirmed:

- Markdown generation
- Chunk creation
- Embedding generation
- ChromaDB persistence
- Semantic retrieval
- Prompt generation

---

# Lessons Learned

This sprint introduced the core concepts behind Retrieval-Augmented Generation (RAG), including semantic embeddings, vector databases, and retrieval pipelines. Separating each stage into independent modules resulted in a cleaner, more maintainable architecture and simplified debugging throughout development.

The project evolved from a traditional web crawler into an AI knowledge engine capable of retrieving information based on semantic meaning rather than keyword matching.

---

# Sprint Review

At the conclusion of Sprint 2, DEUS AI can:

- Crawl blog content
- Parse HTML
- Clean extracted content
- Export Markdown
- Split documents into semantic chunks
- Generate sentence embeddings
- Store vectors in ChromaDB
- Retrieve relevant passages through semantic similarity
- Construct prompts ready for LLM consumption

Sprint 2 successfully established the complete Retrieval-Augmented Generation (RAG) foundation that will power the conversational capabilities of DEUS AI.

---

# Next Sprint

## Sprint 3 – DEUS AI Backend API

Sprint 3 will focus on exposing the RAG engine through a FastAPI backend.

Planned features include:

- REST API endpoints
- OpenAI integration
- Chat request handling
- Source citation support
- JSON responses
- Backend services for the DEUS AI web interface

---

# Sprint Status

| Sprint | Status |
|---------|--------|
| Sprint 1 – Blog Ingestion Pipeline | ✅ Complete |
| Sprint 2 – RAG Knowledge Engine | ✅ Complete |
| Sprint 3 – Backend API | ⏳ Planned |
| Sprint 4 – Web Chat Interface | ⏳ Planned |
| Sprint 5 – Production Deployment | ⏳ Planned |

---

**Sprint Outcome**

Sprint 2 successfully transformed DEUS AI from a content ingestion system into a functional AI knowledge engine. The project now supports semantic search over blog content using Retrieval-Augmented Generation principles and is fully prepared for conversational AI integration in Sprint 3.

