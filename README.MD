# DEUS AI

> **Conversations with BillyMacDeus**

DEUS AI is a Retrieval-Augmented Generation (RAG) conversational AI platform built on more than sixteen years of published writings from **BillyMacDeus**. Rather than answering from general internet knowledge, DEUS AI retrieves relevant content from the author's personal knowledge base and uses GPT-5 to generate grounded, context-aware responses.

This project was developed as part of the Quantic School of Business and Technology Capstone Project using Agile Scrum methodology.

---

## Features

- AI-powered conversational interface
- Retrieval-Augmented Generation (RAG)
- Semantic search using Sentence Transformers
- ChromaDB vector database
- FastAPI backend
- Responsive web frontend
- Automated blog ingestion pipeline
- GitHub Actions Continuous Integration (CI)

---

## Architecture

```text
BillyMacDeus Blog
        │
        ▼
Crawler
        │
        ▼
Raw HTML
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
        │
        ▼
GPT-5
        │
        ▼
FastAPI
        │
        ▼
Frontend
```

---

# Technology Stack

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

# Screenshots

Suggested repository screenshots:

- Frontend interface
- FastAPI Swagger UI
- Knowledge pipeline execution
- ChromaDB indexing
- GitHub Actions
- Conversation example

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

# License

This project is intended for educational and research purposes as part of the Quantic School of Business and Technology Capstone Project.

---

# Author

**BillyMacDeus**

Writer • Technologist • AI Enthusiast

---

*"Every answer is grounded in BillyMacDeus' published writings."*

BADGES:

![Python](https://img.shields.io/badge/Python-3.14-blue)

![FastAPI](https://img.shields.io/badge/FastAPI-0.141-green)

![GPT-5](https://img.shields.io/badge/GPT-5-OpenAI-black)

![ChromaDB](https://img.shields.io/badge/Vector%20DB-ChromaDB-purple)

![License](https://img.shields.io/badge/License-Educational-orange)