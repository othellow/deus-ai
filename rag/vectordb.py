
"""
DEUS AI - RAG Knowledge Engine
------------------------------

Stores text embeddings inside ChromaDB.

Sprint 2 Scope:
- Load embedding JSON files
- Create persistent ChromaDB collection
- Store vectors with metadata
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
        Initialize persistent ChromaDB client.
        """

        self.client = chromadb.PersistentClient(
            path=str(CHROMA_DIR),
            settings=Settings(anonymized_telemetry=False),
        )

        self.collection = self.client.get_or_create_collection(
            name=COLLECTION_NAME,
            metadata={
                "description": "BillyMacDeus Knowledge Base"
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

        for chunk in chunks:

            self.collection.add(
                ids=[
                    f"{chunk['source']}_{chunk['chunk_id']}"
                ],
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

        print(
            f"✔ Stored {len(chunks)} embeddings from {embedding_file.name}"
        )

        return len(chunks)

    def load_all(self) -> int:
        """
        Load every embedding JSON file.
        """

        total = 0

        for file in sorted(
            CHUNKS_DIR.glob("*_embeddings.json")
        ):

            total += self.load_embeddings(file)

        return total

    def count(self) -> int:
        """
        Return total vectors stored.
        """

        return self.collection.count()


def main() -> None:

    db = VectorDatabase()

    total = db.load_all()

    print("\n============================")

    print(f"Vectors stored: {total}")

    print(f"Database count: {db.count()}")

    print("============================")


if __name__ == "__main__":
    main()

    