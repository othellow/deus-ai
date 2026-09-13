"""
DEUS AI - RAG Knowledge Engine
------------------------------

Retriever responsible for semantic search
using ChromaDB.

Sprint 2 Scope:

- Load embedding model
- Embed user query
- Search ChromaDB
- Return best matching chunks
"""

import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

from crawler.config import (
    CHROMA_DIR,
    COLLECTION_NAME,
    EMBEDDING_MODEL,
)


class Retriever:
    """
    Semantic retriever for DEUS AI.
    """

    def __init__(self) -> None:
        """
        Load embedding model and ChromaDB.
        """

        print("Loading embedding model...")

        self.model = SentenceTransformer(
            EMBEDDING_MODEL
        )

        self.client = chromadb.PersistentClient(
            path=str(CHROMA_DIR),
            settings=Settings(
                anonymized_telemetry=False,
            ),
        )

        self.collection = self.client.get_collection(
            COLLECTION_NAME
        )

    def search(
        self,
        question: str,
        top_k: int = 5,
    ) -> dict:
        """
        Search the knowledge base.

        Args:
            question:
                User question.

            top_k:
                Number of results.

        Returns:
            ChromaDB search results.
        """

        embedding = self.model.encode(
            question,
            normalize_embeddings=True,
        ).tolist()

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k,
        )

        return results


def main() -> None:

    retriever = Retriever()

    print()

    question = input("Ask DEUS AI: ")

    print()

    results = retriever.search(question)

    print("=" * 60)

    print("Top Matches")

    print("=" * 60)

    documents = results["documents"][0]
    metadata = results["metadatas"][0]
    distances = results["distances"][0]

    for index, (doc, meta, distance) in enumerate(
        zip(documents, metadata, distances),
        start=1,
    ):

        print(f"\nResult #{index}")

        print(f"Similarity Score : {1-distance:.4f}")

        print(f"Source           : {meta['source']}")

        print()

        print(doc[:350])

        print("-" * 60)


if __name__ == "__main__":
    main()

    