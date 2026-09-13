"""
DEUS AI - RAG Knowledge Engine
------------------------------

Builds an LLM-ready prompt from retrieved blog content.

Sprint 3 Scope

- Retrieve relevant semantic chunks
- Assemble LLM prompt
- Return context grounded in BillyMacDeus' writings
"""

from rag.retriever import Retriever


class RAGEngine:
    """
    Builds prompts for the language model.
    """

    def __init__(self) -> None:
        """
        Initialize the semantic retriever.
        """

        self.retriever = Retriever()

    def build_prompt(
        self,
        question: str,
        top_k: int = 5,
    ) -> str:
        """
        Build an LLM prompt from the retrieved context.
        """

        results = self.retriever.search(
            question,
            top_k=top_k,
        )

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        context = []

        for doc, meta, distance in zip(
            documents,
            metadatas,
            distances,
        ):

            similarity = max(
                0.0,
                1.0 - distance,
            )

            context.append(
                f"""
============================================================

Source:
{meta['source']}

Chunk:
{meta['chunk_id']}

Similarity:
{similarity:.4f}

Content:

{doc}
"""
            )

        prompt = f"""
You are DEUS AI.

You are the AI companion for BillyMacDeus' writings.

Use ONLY the supplied context below.

Do not invent facts.

If the answer cannot be found in the supplied context,
reply politely that the information is not available in
BillyMacDeus' published writings.

============================================================
QUESTION
============================================================

{question}

============================================================
CONTEXT
============================================================

{''.join(context)}

============================================================
ANSWER
============================================================
"""

        return prompt.strip()


def main() -> None:
    """
    Manual RAG engine test.
    """

    engine = RAGEngine()

    while True:

        print()

        question = input(
            "Ask DEUS AI (type 'exit' to quit): "
        )

        if question.lower() == "exit":
            break

        prompt = engine.build_prompt(question)

        print()
        print("=" * 70)
        print("LLM PROMPT")
        print("=" * 70)
        print()

        print(prompt)


if __name__ == "__main__":
    main()

    