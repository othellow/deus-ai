"""
DEUS AI API Routes
------------------
"""

from fastapi import APIRouter

from api.schemas import ChatRequest, ChatResponse
from api.services import ChatService

router = APIRouter(
    prefix="/api/v1",
    tags=["DEUS AI"],
)

service = ChatService()


@router.get("/health")
def health():

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

    return service.ask(request.message)

