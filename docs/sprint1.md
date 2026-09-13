
# DEUS AI – Sprint 1 Report

**Project:** DEUS AI

**Sprint:** Sprint 1

**Sprint Title:** Blog Ingestion Pipeline

**Duration:** Sprint 1

**Author:** Billy Mac Deuz

---

# Sprint Goal

Develop the initial blog ingestion pipeline for DEUS AI. The pipeline automatically retrieves content from the BillyMacDeus blog, extracts structured information, cleans the content, converts it into AI-ready Markdown documents, exports metadata, and prepares the data for future Retrieval-Augmented Generation (RAG) processing.

---

# Sprint Objectives

- Establish the project repository.
- Configure the Python development environment.
- Implement a modular ingestion pipeline.
- Extract blog metadata and article content.
- Clean unnecessary HTML elements.
- Export Markdown documents.
- Export metadata as JSON.
- Automate ingestion using a scheduler.
- Create automated unit tests.
- Configure Continuous Integration using GitHub Actions.

---

# Sprint Deliverables

| Deliverable | Status |
|--------------|----------|
| Project Repository | ✅ |
| Python Virtual Environment | ✅ |
| requirements.txt | ✅ |
| config.py | ✅ |
| models.py | ✅ |
| crawler.py | ✅ |
| parser.py | ✅ |
| cleaner.py | ✅ |
| markdown_exporter.py | ✅ |
| scheduler.py | ✅ |
| metadata.json Export | ✅ |
| Automated Tests | ✅ |
| GitHub Actions CI | ✅ |

---

# Product Backlog

| ID | User Story | Priority | Status |
|----|------------|----------|--------|
| PB-01 | Crawl BillyMacDeus blog | High | ✅ |
| PB-02 | Parse article metadata | High | ✅ |
| PB-03 | Extract article content | High | ✅ |
| PB-04 | Clean HTML | High | ✅ |
| PB-05 | Export Markdown | High | ✅ |
| PB-06 | Export Metadata JSON | High | ✅ |
| PB-07 | Schedule automatic crawling | Medium | ✅ |
| PB-08 | Automated Testing | High | ✅ |
| PB-09 | Continuous Integration | Medium | ✅ |

---

# Repository Structure

```text
deus-ai/

├── crawler/
│   ├── __init__.py
│   ├── cleaner.py
│   ├── config.py
│   ├── crawler.py
│   ├── markdown_exporter.py
│   ├── models.py
│   ├── parser.py
│   └── scheduler.py
│
├── data/
│   ├── raw/
│   ├── cleaned/
│   ├── markdown/
│   ├── metadata/
│   └── chunks/
│
├── docs/
│   └── sprint1.md
│
├── logs/
│
├── tests/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── requirements.txt
└── pytest.ini
```

---

# System Architecture

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
BlogPost Objects
        │
        ▼
Cleaner
        │
        ▼
Markdown Exporter
        ├──────────────┐
        ▼              ▼
Markdown Files    Metadata JSON
        │
        ▼
Scheduler
        │
        ▼
Future RAG Pipeline
```

---

# Technical Decisions

During Sprint 1, two architectural improvements were introduced beyond the original implementation plan.

The first improvement was introducing dedicated Pydantic data models (`BlogMetadata`, `BlogContent`, and `BlogPost`) to establish a consistent data contract between pipeline stages.

The second improvement was separating HTML parsing into a dedicated `parser.py` module. This follows the Single Responsibility Principle by isolating content extraction from HTTP retrieval, making the system easier to maintain and test.

These refinements improve modularity and provide a stronger foundation for future AI processing.

---

# Testing

The project includes automated smoke tests covering the primary modules:

- Configuration
- Data models
- Crawler
- Parser
- Cleaner
- Markdown exporter

**Result**

```
6 passed in 0.16s
```

---

# Continuous Integration

GitHub Actions was configured to automatically:

1. Check out the repository.
2. Install Python dependencies.
3. Execute the automated pytest suite.
4. Report build status.

This ensures that future commits are automatically validated.

---

# Sprint Outcomes

Sprint 1 successfully established the ingestion layer of DEUS AI.

The completed solution is capable of:

- Downloading blog pages.
- Discovering articles.
- Parsing blog content.
- Cleaning extracted HTML.
- Exporting Markdown documents.
- Exporting metadata as JSON.
- Running scheduled ingestion jobs.
- Automatically validating functionality through unit tests.

This sprint provides the data acquisition foundation required for future AI features.

---

# Challenges Encountered

Several implementation challenges were addressed during Sprint 1.

- Python package import configuration for pytest.
- Blogger HTML structure differences.
- Scheduler dependency management.
- URL validation using Pydantic.
- GitHub Actions workflow configuration.

Each issue was resolved through iterative development and testing.

---

# Lessons Learned

Sprint 1 reinforced several software engineering principles:

- Modular architectures simplify testing.
- Configuration should be centralized.
- Automated testing reduces regression risk.
- Continuous Integration improves software quality.
- Small iterative improvements align well with Agile Scrum practices.

---

# Sprint Metrics

| Metric | Value |
|----------|---------|
| Python Modules | 7 |
| Automated Tests | 6 |
| GitHub Actions Workflows | 1 |
| Sprint Deliverables Completed | 100% |
| CI Status | Passing |
| Test Status | 6 / 6 Passed |

---

# Sprint Review

Sprint 1 achieved its primary objective of building a functional blog ingestion pipeline for DEUS AI.

The resulting architecture provides a clean separation between data acquisition, parsing, cleaning, serialization, and scheduling. Automated testing and continuous integration were incorporated to improve software quality and maintainability.

The project is now prepared for Sprint 2, which will focus on text chunking, embeddings, vector storage, and Retrieval-Augmented Generation (RAG).

---

# Sprint Retrospective

## What Went Well

- Repository structure established successfully.
- Modular architecture implemented.
- Automated testing introduced early.
- Continuous Integration configured successfully.
- All planned Sprint 1 deliverables completed.

## What Could Be Improved

- Improve metadata extraction accuracy.
- Parse publication dates directly from Blogger.
- Improve label extraction.
- Expand automated test coverage.

## Action Items for Sprint 2

- Implement text chunking.
- Generate embeddings.
- Integrate ChromaDB.
- Build semantic search.
- Connect an LLM using RAG.

---

# Appendix

## Screenshots

Include:

- GitHub Repository
- GitHub Actions (Passing)
- pytest Results
- Scheduler Execution
- Markdown Output
- Metadata JSON Output