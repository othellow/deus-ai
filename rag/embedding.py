"""
DEUS AI - RAG Knowledge Engine
------------------------------

Embedding module responsible for converting text chunks
into semantic vectors using Sentence Transformers.

Sprint 2 Scope:
- Load embedding model
- Read chunk JSON files
- Generate embeddings
- Save embeddings as JSON
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

        print(f"Loading model: {EMBEDDING_MODEL}")

        self.model = SentenceTransformer(
            EMBEDDING_MODEL
        )

    def embed_text(
        self,
        text: str,
    ) -> list[float]:
        """
        Generate an embedding for one text.
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

        output = chunk_file.with_name(
            chunk_file.stem + "_embeddings.json"
        )

        output.write_text(
            json.dumps(
                chunks,
                indent=4,
            ),
            encoding="utf-8",
        )

        print(
            f"✔ Embedded {chunk_file.name}"
        )

        return len(chunks)

    def process_all(self) -> int:
        """
        Process every chunk JSON.
        """

        total = 0

        for chunk_file in sorted(
            CHUNKS_DIR.glob("*.json")
        ):

            total += self.process_file(
                chunk_file
            )

        return total


def main() -> None:

    generator = EmbeddingGenerator()

    total = generator.process_all()

    print("\n=========================")

    print(f"Embeddings generated: {total}")

    print("=========================")


if __name__ == "__main__":
    main()

    