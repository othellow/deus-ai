"""
DEUS AI API Routes
------------------

API endpoints for DEUS AI.
"""

from fastapi import APIRouter

from api.schemas import ChatRequest, ChatResponse
from api.services import ChatService

router = APIRouter(
    prefix="/api/v1",
    tags=["DEUS AI"],
)


@router.get("/health")
def health():
    """
    Health check endpoint.
    """

    return {
        "status": "healthy",
        "service": "DEUS AI",
        "version": "1.0.0",
    }


@router.post(
    "/chat",
    response_model=ChatResponse,
)
def chat(request: ChatRequest):
    """
    Process a chat request.
    """

    # Lazy initialization prevents GitHub Actions
    # from loading the RAG engine during module import.
    service = ChatService()

    return service.ask(request.message)

