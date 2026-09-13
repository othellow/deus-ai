"""
DEUS AI - RAG Knowledge Engine
------------------------------

Embedding module responsible for converting text chunks
into semantic vectors using Sentence Transformers.

Sprint 3 Scope:

- Load embedding model
- Read chunk JSON files
- Generate semantic embeddings
- Save embedding JSON files
"""

import json
from pathlib import Path

from sentence_transformers import SentenceTransformer

from crawler.config import (
    CHUNKS_DIR,
    EMBEDDING_MODEL,
)


class EmbeddingGenerator:
    """
    Generates embeddings for chunked documents.
    """

    def __init__(self) -> None:
        """
        Load the embedding model once.
        """

        print("=" * 60)
        print("DEUS AI Embedding Generator")
        print("=" * 60)
        print(f"Loading model: {EMBEDDING_MODEL}")
        print()

        self.model = SentenceTransformer(
            EMBEDDING_MODEL
        )

    def embed_text(
        self,
        text: str,
    ) -> list[float]:
        """
        Generate an embedding for a text chunk.
        """

        embedding = self.model.encode(
            text,
            normalize_embeddings=True,
        )

        return embedding.tolist()

    def process_file(
        self,
        chunk_file: Path,
    ) -> int:
        """
        Generate embeddings for one chunk file.
        """

        chunks = json.loads(
            chunk_file.read_text(
                encoding="utf-8"
            )
        )

        for chunk in chunks:

            chunk["embedding"] = self.embed_text(
                chunk["text"]
            )

        output_file = chunk_file.with_name(
            chunk_file.stem + "_embeddings.json"
        )

        output_file.write_text(
            json.dumps(
                chunks,
                indent=4,
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )

        return len(chunks)

    def process_all(self) -> int:
        """
        Process every chunk JSON file.
        """

        chunk_files = sorted(
            [
                file
                for file in CHUNKS_DIR.glob("*.json")
                if not file.name.endswith("_embeddings.json")
            ]
        )

        total_embeddings = 0

        print(f"Chunk files found: {len(chunk_files)}")
        print()

        for index, chunk_file in enumerate(chunk_files, start=1):

            count = self.process_file(
                chunk_file
            )

            total_embeddings += count

            if (
                index <= 5
                or index == len(chunk_files)
                or index % 100 == 0
            ):
                print(
                    f"✓ [{index}/{len(chunk_files)}] "
                    f"{chunk_file.name} "
                    f"({count} embeddings)"
                )

        print()
        print("=" * 60)
        print("Embedding Complete")
        print("=" * 60)
        print(f"Total embeddings generated: {total_embeddings}")

        return total_embeddings


def main() -> None:
    """
    Manual embedding test.
    """

    generator = EmbeddingGenerator()

    total = generator.process_all()

    print()
    print("=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"Embeddings generated: {total}")


if __name__ == "__main__":
    main()

    