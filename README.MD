# DEUS AI

> **Conversations with BillyMacDeus**

DEUS AI is a Retrieval-Augmented Generation (RAG) conversational AI platform built on more than sixteen years of published writings from **BillyMacDeus**. Rather than answering from general internet knowledge, DEUS AI retrieves relevant content from the author's personal knowledge base and uses GPT-5 to generate grounded, context-aware responses.

This project was developed as part of the Quantic School of Business and Technology Capstone Project using Agile Scrum methodology.

# Overview

DEUS AI is a Retrieval-Augmented Generation (RAG) application that transforms the BillyMacDeus Blog into an intelligent conversational knowledge base.

Instead of manually searching through hundreds of blog articles, readers can ask questions in natural language and receive AI-generated answers grounded exclusively in BillyMacDeus' published writings.

The system combines semantic search, vector embeddings, ChromaDB, GPT-5, and FastAPI to deliver accurate, context-aware responses.

---


# Live Production

## BillyMacDeus Blog

https://blog.billymacdeus.com

DEUS AI is available through the website navigation as a dedicated page.

---
## Backend API

https://deus-ai-production.up.railway.app

Swagger Documentation:

https://deus-ai-production.up.railway.app/docs

---

## Frontend

https://deus-ai.bd40.workers.dev


## Features

- AI-powered semantic search
- Retrieval-Augmented Generation (RAG)
- GPT-5 integration
- ChromaDB vector database
- SentenceTransformer embeddings
- Automatic blog crawler
- Markdown knowledge processing
- FastAPI REST API
- Responsive web interface
- GitHub Actions CI/CD
- Railway deployment
- Cloudflare deployment
- Automatic ChromaDB rebuilding
- Embedded Blogger integration

---

# Technology Stack

## Backend

- Python
- FastAPI
- OpenAI Responses API
- SentenceTransformers
- ChromaDB

---

## Frontend

- HTML5
- CSS3
- Vanilla JavaScript

---

## AI

- GPT-5
- all-MiniLM-L6-v2
- Retrieval-Augmented Generation (RAG)

---

## Deployment

- Railway
- Cloudflare Workers
- GitHub Actions


---
# Project Structure

```
deus-ai/

├── api/
│   ├── app.py
│   ├── routes.py
│   ├── services.py
│   ├── ai_service.py
│   └── schemas.py
│
├── crawler/
│
├── rag/
│   ├── retriever.py
│   ├── rag_engine.py
│   └── vectordb.py
│
├── frontend/
│   ├── index.html
│   ├── styles.css
│   ├── app.js
│   └── assets/
│
├── data/
│
├── tests/
│
├── docs/
│
└── requirements.txt
```



---

# System Architecture

```
BillyMacDeus Blog
        │
        ▼
Cloudflare Frontend
        │
        ▼
Railway FastAPI
        │
        ▼
Chat Service
        │
        ▼
RAG Engine
        │
        ▼
Retriever
        │
        ▼
ChromaDB
        │
        ▼
GPT-5
        │
        ▼
Response
```

---

# Technology Stack Summary

| Layer | Technology |
|--------|------------|
| Language | Python 3.14 |
| Backend | FastAPI |
| AI Model | GPT-5 |
| Vector Database | ChromaDB |
| Embeddings | Sentence Transformers |
| HTML Parser | BeautifulSoup |
| Frontend | HTML5 / CSS3 / JavaScript |
| Testing | Pytest |
| CI | GitHub Actions |

---

# Project Structure

```text
deus-ai/

├── api/
│   ├── app.py
│   ├── routes.py
│   ├── services.py
│   └── ai_service.py
│
├── crawler/
│   ├── crawler.py
│   ├── parser.py
│   ├── cleaner.py
│   ├── markdown_exporter.py
│   ├── chunker.py
│   ├── embeddings.py
│   └── vectordb.py
│
├── rag/
│   ├── retriever.py
│   └── rag_engine.py
│
├── pipeline/
│   └── ingest.py
│
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── app.js
│
├── tests/
├── docs/
├── data/
├── requirements.txt
└── README.md
```

---

# Knowledge Base Statistics

Current knowledge base:

| Metric | Count |
|---------|------:|
| HTML Pages Crawled | 1008 |
| Blog Articles Parsed | 1014 |
| Markdown Documents | 1014 |
| Semantic Chunks | 4521 |
| Embeddings | 4521 |
| ChromaDB Vectors | 4521 |

---

# Automatic Knowledge Base Initialization

Fresh cloud deployments do not contain an existing ChromaDB vector database.

DEUS AI automatically detects when the knowledge base is unavailable and rebuilds the vector collection from the embedding JSON files.

This allows deployments to remain reproducible without storing generated database files in source control.

Workflow:

```
Application Startup

        │

        ▼

Collection Exists?

        │

   Yes ─────────► Continue

        │

       No

        │

        ▼

Load Embedding JSON Files

        │

        ▼

Rebuild ChromaDB

        │

        ▼

Serve Requests
```

---

# Continuous Integration

GitHub Actions automatically performs:

- Dependency installation
- Unit testing
- FastAPI validation
- RAG engine validation

Every commit to the main branch is automatically verified before deployment.

---

# Production Deployment

Backend

- Railway

Frontend

- Cloudflare

Website

- BillyMacDeus Blog

Deployment is fully automated through GitHub.

---



---

# Running the Project

## Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/deus-ai.git

cd deus-ai
```

---

## Create a virtual environment

```bash
python -m venv .venv
```

Activate it.

macOS / Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configure OpenAI

Create a `.env` file.

```text
OPENAI_API_KEY=your_api_key_here
```

---

## Build the knowledge base

```bash
python -m pipeline.ingest
```

---

## Start the backend

```bash
uvicorn api.app:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## Start the frontend

```bash
cd frontend

python -m http.server 5500
```

Open:

```
http://localhost:5500
```

---

# API

## Health Check

```
GET /api/v1/health
```

---

## Chat

```
POST /api/v1/chat
```

Request

```json
{
    "message":"What have you written about compassion?"
}
```

Response

```json
{
    "answer":"...",
    "sources":[
        "BillyMacDeus Knowledge Base"
    ]
}
```

---

# Development Journey

The project was delivered using four Agile Scrum sprints.

## Sprint 1

- Blog crawler
- HTML parser
- Cleaner
- Markdown exporter

---

## Sprint 2

- Semantic chunking
- Embedding generation
- ChromaDB integration
- Knowledge pipeline

---

## Sprint 3

- FastAPI backend
- OpenAI GPT-5 integration
- Retrieval-Augmented Generation
- Semantic retrieval

---

## Sprint 4

- Responsive frontend
- Conversational interface
- Backend integration
- User experience improvements
- Deployment preparation

---
## Sprint 5

### Production Deployment

Completed

Deliverables

- Railway backend deployment
- Cloudflare frontend deployment
- GitHub automated deployment
- Automatic ChromaDB initialization
- Production API
- Blogger integration
- Live production release

---

# Future Roadmap

Planned enhancements include:

- Clickable article citations
- Conversation history
- Streaming AI responses
- Authentication
- Mobile application
- Analytics dashboard
- Multi-model AI support
- Deployment to production
- Integration with BillyMacDeus.com

---

# Author

** Billy Mac Deus **

Writer • Technologist • AI Enthusiast
owner of BillyMacDeus Blog
https://blog.billymacdeus.com

---

*"Every answer is grounded in BillyMacDeus' published writings."*

BADGES:

![Python](https://img.shields.io/badge/Python-3.14-blue)

![FastAPI](https://img.shields.io/badge/FastAPI-0.141-green)

![GPT-5](https://img.shields.io/badge/GPT-5-OpenAI-black)

![ChromaDB](https://img.shields.io/badge/Vector%20DB-ChromaDB-purple)

![License](https://img.shields.io/badge/License-Educational-orange)


# Academic Information

Capstone Project

Master of Science in Software Engineering

Quantic School of Business and Technology

2026

# License

This project is intended for educational and research purposes as part of the Quantic MSSE Capstone Project.