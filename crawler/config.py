"""
DEUS AI
-------

Centralized configuration for the DEUS AI project.

This module contains:

- Project paths
- Blog configuration
- Network settings
- Scheduler settings
- Chunking settings
- RAG settings
- ChromaDB settings
- Logging configuration

Keeping configuration in one place makes the application
easier to maintain and extend across future sprints.
"""

from pathlib import Path

# ============================================================================
# Project Paths
# ============================================================================

# Root directory of the project (deus-ai/)
BASE_DIR = Path(__file__).resolve().parent.parent

# Data directories
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
CLEANED_DIR = DATA_DIR / "cleaned"
MARKDOWN_DIR = DATA_DIR / "markdown"
METADATA_DIR = DATA_DIR / "metadata"
CHUNKS_DIR = DATA_DIR / "chunks"
CHROMA_DIR = DATA_DIR / "chroma"

# Logs
LOG_DIR = BASE_DIR / "logs"

# ============================================================================
# OpenAI Configuration
# ============================================================================

OPENAI_MODEL = "gpt-5"

# ============================================================================
# Blog Configuration
# ============================================================================

BLOG_NAME = "BillyMacDeus Blog"

BLOG_URL = "https://blog.billymacdeus.com/"

USER_AGENT = (
    "DEUS-AI-BlogCrawler/1.0 "
    "(Quantic MSSE Capstone Project; "
    "https://github.com/othellow/deus-ai)"
)

# ============================================================================
# Network Configuration
# ============================================================================

REQUEST_TIMEOUT = 30  # seconds

MAX_RETRIES = 3

RETRY_DELAY = 5  # seconds

# ============================================================================
# Scheduler Configuration
# ============================================================================

CRAWL_INTERVAL_DAYS = 7

# ============================================================================
# Chunking Configuration
# ============================================================================

CHUNK_SIZE = 500

CHUNK_OVERLAP = 100

# ============================================================================
# RAG Configuration
# ============================================================================

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

EMBEDDING_BATCH_SIZE = 32

# ============================================================================
# ChromaDB Configuration
# ============================================================================

COLLECTION_NAME = "deus_ai_blog"

# ============================================================================
# Logging Configuration
# ============================================================================

LOG_FILE = LOG_DIR / "crawler.log"

LOG_LEVEL = "INFO"

# ============================================================================
# Create Required Directories
# ============================================================================

DIRECTORIES = [
    DATA_DIR,
    RAW_DIR,
    CLEANED_DIR,
    MARKDOWN_DIR,
    METADATA_DIR,
    CHUNKS_DIR,
    CHROMA_DIR,
    LOG_DIR,
]

for directory in DIRECTORIES:
    directory.mkdir(parents=True, exist_ok=True)

