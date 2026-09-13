"""
DEUS AI Knowledge Pipeline
--------------------------

Coordinates the complete DEUS AI knowledge ingestion workflow.

Pipeline Stages

1. Parse downloaded HTML files
2. Clean extracted content
3. Export Markdown and metadata
4. Chunk Markdown documents
5. Generate semantic embeddings
6. Store embeddings in ChromaDB
"""

from pathlib import Path

from crawler.cleaner import BlogCleaner
from crawler.markdown_exporter import MarkdownExporter
from crawler.parser import BlogParser

from rag.chunker import Chunker
from rag.embedding import EmbeddingGenerator
from rag.vectordb import VectorDatabase


def main() -> None:
    """
    Execute the complete DEUS AI knowledge ingestion pipeline.
    """

    print("=" * 60)
    print("DEUS AI Knowledge Pipeline")
    print("=" * 60)
    print()

    # ==========================================================
    # Initialize pipeline components
    # ==========================================================

    parser = BlogParser()
    cleaner = BlogCleaner()
    exporter = MarkdownExporter()
    chunker = Chunker()
    embedding = EmbeddingGenerator()
    vectordb = VectorDatabase()

    # ==========================================================
    # Stage 1 - Parse HTML
    # ==========================================================

    posts = parser.parse_all(
        Path("data/raw")
    )

    # ==========================================================
    # Stage 2 - Clean Content
    # ==========================================================

    cleaned_posts = cleaner.clean_all(
        posts
    )

    # ==========================================================
    # Stage 3 - Export Markdown & Metadata
    # ==========================================================

    exported = exporter.export_all(
        cleaned_posts
    )

    # ==========================================================
    # Stage 4 - Chunk Markdown
    # ==========================================================

    total_chunks = chunker.process_all()

    # ==========================================================
    # Stage 5 - Generate Embeddings
    # ==========================================================

    total_embeddings = embedding.process_all()

    # ==========================================================
    # Stage 6 - Store Embeddings in ChromaDB
    # ==========================================================

    total_vectors = vectordb.load_all()

    # ==========================================================
    # Pipeline Summary
    # ==========================================================

    print()
    print("=" * 60)
    print("Pipeline Summary")
    print("=" * 60)

    print(f"Parsed Posts      : {len(posts)}")
    print(f"Cleaned Posts     : {len(cleaned_posts)}")
    print(f"Exported Articles : {len(exported)}")
    print(f"Total Chunks      : {total_chunks}")
    print(f"Embeddings        : {total_embeddings}")
    print(f"Vectors Stored    : {total_vectors}")
    print(f"Database Count    : {vectordb.count()}")

    print()
    print("Pipeline completed successfully.")
    print("=" * 60)


if __name__ == "__main__":
    main()

    