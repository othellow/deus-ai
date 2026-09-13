"""
DEUS AI - Blog Ingestion Pipeline
--------------------------------
Configuration settings for the blog crawler.

This module centralizes all configurable values used throughout
the ingestion pipeline, making the application easier to maintain,
test, and extend.
"""

from pathlib import Path

# ============================================================================
# Project Paths
# ============================================================================

# Base directory of the project (deus-ai/)
BASE_DIR = Path(__file__).resolve().parent.parent

# Data directories
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
CLEANED_DIR = DATA_DIR / "cleaned"
MARKDOWN_DIR = DATA_DIR / "markdown"
METADATA_DIR = DATA_DIR / "metadata"
CHUNKS_DIR = DATA_DIR / "chunks"

# Log directory
LOG_DIR = BASE_DIR / "logs"

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
# Chunking Configuration (Future Sprint)
# ============================================================================

CHUNK_SIZE = 500

CHUNK_OVERLAP = 100

# ============================================================================
# Logging
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
    LOG_DIR,
]

for directory in DIRECTORIES:
    directory.mkdir(parents=True, exist_ok=True)

