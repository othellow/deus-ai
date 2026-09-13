"""
DEUS AI - RAG Knowledge Engine
------------------------------

Stores semantic embeddings inside ChromaDB.

Sprint 5 Enhancement

- Load embedding JSON files
- Store embeddings in ChromaDB
- Skip duplicate vectors
- Automatically rebuild knowledge base
"""

import json
from pathlib import Path

import chromadb
from chromadb.config import Settings

from crawler.config import (
    CHROMA_DIR,
    CHUNKS_DIR,
    COLLECTION_NAME,
)


class VectorDatabase:
    """
    Handles storage of embeddings in ChromaDB.
    """

    def __init__(self) -> None:
        """
        Initialize the persistent ChromaDB client.
        """

        self.client = chromadb.PersistentClient(
            path=str(CHROMA_DIR),
            settings=Settings(
                anonymized_telemetry=False,
            ),
        )

        self.collection = self.client.get_or_create_collection(
            name=COLLECTION_NAME,
            metadata={
                "description": "BillyMacDeus Knowledge Base",
            },
        )

    def load_embeddings(
        self,
        embedding_file: Path,
    ) -> int:
        """
        Load one embedding JSON file into ChromaDB.
        """

        chunks = json.loads(
            embedding_file.read_text(
                encoding="utf-8"
            )
        )

        stored = 0

        for chunk in chunks:

            vector_id = (
                f"{chunk['source']}_{chunk['chunk_id']}"
            )

            try:

                self.collection.add(
                    ids=[vector_id],
                    documents=[
                        chunk["text"]
                    ],
                    embeddings=[
                        chunk["embedding"]
                    ],
                    metadatas=[
                        {
                            "source": chunk["source"],
                            "chunk_id": chunk["chunk_id"],
                        }
                    ],
                )

                stored += 1

            except Exception:
                # Vector already exists.
                # Ignore duplicates.
                pass

        return stored

    def load_all(self) -> int:
        """
        Load every embedding JSON file.
        """

        embedding_files = sorted(
            CHUNKS_DIR.glob("*_embeddings.json")
        )

        if not embedding_files:
            raise RuntimeError(
                f"No embedding JSON files were found in: {CHUNKS_DIR}"
            )

        total = 0

        print("=" * 60)
        print("DEUS AI Vector Database")
        print("=" * 60)

        print(
            f"Embedding files: {len(embedding_files)}"
        )

        print()

        for index, file in enumerate(
            embedding_files,
            start=1,
        ):

            stored = self.load_embeddings(file)

            total += stored

            if (
                index <= 5
                or index == len(embedding_files)
                or index % 100 == 0
            ):
                print(
                    f"✓ [{index}/{len(embedding_files)}] "
                    f"{file.name} "
                    f"({stored} vectors)"
                )

        print()

        print("=" * 60)
        print("Vector Database Complete")
        print("=" * 60)

        print(f"Vectors stored : {total}")
        print(f"Database count : {self.count()}")

        return total

    def count(self) -> int:
        """
        Return the number of vectors stored.
        """

        return self.collection.count()


def main() -> None:

    db = VectorDatabase()

    total = db.load_all()

    print()
    print("=" * 60)
    print("Summary")
    print("=" * 60)

    print(f"Vectors stored : {total}")
    print(f"Database count : {db.count()}")


if __name__ == "__main__":
    main()

    