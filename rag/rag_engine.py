
"""
DEUS AI - RAG Knowledge Engine
------------------------------

Builds an LLM-ready prompt from retrieved blog content.

Sprint 2 Scope:

- Retrieve relevant blog chunks
- Assemble prompt
- Return complete context for an LLM
"""

from rag.retriever import Retriever


class RAGEngine:
    """
    Builds prompts for the language model.
    """

    def __init__(self) -> None:
        self.retriever = Retriever()

    def build_prompt(
        self,
        question: str,
        top_k: int = 5,
    ) -> str:
        """
        Build an LLM prompt using retrieved context.
        """

        results = self.retriever.search(
            question,
            top_k=top_k,
        )

        documents = results["documents"][0]
        metadata = results["metadatas"][0]

        context = []

        for doc, meta in zip(documents, metadata):

            context.append(
                f"""
Source:
{meta['source']}

Content:
{doc}
"""
            )

        prompt = f"""
You are DEUS AI.

You answer questions ONLY using BillyMacDeus'
published writings.

If the answer cannot be found in the supplied
context, politely say you don't know.

=========================
QUESTION
=========================

{question}

=========================
CONTEXT
=========================

{"".join(context)}

=========================
ANSWER
=========================
"""

        return prompt.strip()


def main():

    engine = RAGEngine()

    question = input("Ask DEUS AI: ")

    print()

    prompt = engine.build_prompt(question)

    print("=" * 70)

    print("LLM PROMPT")

    print("=" * 70)

    print(prompt)


if __name__ == "__main__":
    main()

    