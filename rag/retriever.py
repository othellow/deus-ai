"""
DEUS AI - RAG Knowledge Engine
------------------------------

Retriever responsible for semantic search
using ChromaDB.

Sprint 3 Scope

- Load embedding model
- Embed user query
- Search ChromaDB
- Return top semantic matches
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

        print("=" * 60)
        print("DEUS AI Retriever")
        print("=" * 60)
        print(f"Loading embedding model: {EMBEDDING_MODEL}")
        print()

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

        print(
            f"Knowledge Base Size: "
            f"{self.collection.count()} vectors"
        )

        print()

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
                Number of semantic matches.

        Returns:
            ChromaDB search results.
        """

        embedding = self.model.encode(
            question,
            normalize_embeddings=True,
        ).tolist()

        return self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k,
            include=[
                "documents",
                "metadatas",
                "distances",
            ],
        )


def main() -> None:

    retriever = Retriever()

    while True:

        print()

        question = input(
            "Ask DEUS AI (type 'exit' to quit): "
        )

        if question.lower() == "exit":
            break

        results = retriever.search(question)

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        print()
        print("=" * 60)
        print("Top Semantic Matches")
        print("=" * 60)

        if not documents:

            print("No matching articles found.")
            continue

        for index, (doc, meta, distance) in enumerate(
            zip(documents, metadatas, distances),
            start=1,
        ):

            similarity = max(
                0.0,
                1.0 - distance,
            )

            print(f"\nResult #{index}")
            print(f"Similarity : {similarity:.4f}")
            print(f"Source     : {meta['source']}")
            print(f"Chunk      : {meta['chunk_id']}")
            print()

            preview = doc[:400]

            if len(doc) > 400:
                preview += "..."

            print(preview)

            print("-" * 60)


if __name__ == "__main__":
    main()

    