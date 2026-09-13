"""
DEUS AI Services
----------------

Coordinates Retrieval-Augmented Generation (RAG)
and OpenAI response generation.
"""

from api.ai_service import AIService
from rag.rag_engine import RAGEngine


class ChatService:
    """
    Main chat service.
    """

    def __init__(self) -> None:
        self.rag = RAGEngine()
        self.ai = AIService()

    def ask(self, question: str) -> dict:
        """
        Answer a user question using the DEUS AI
        knowledge base.
        """

        prompt = self.rag.build_prompt(question)

        answer = self.ai.generate(prompt)

        return {
            "answer": answer,
            "sources": [
                "BillyMacDeus Knowledge Base"
            ],
        }
    
    