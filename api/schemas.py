"""
DEUS AI API Schemas
-------------------
"""

from pydantic import BaseModel


class ChatRequest(BaseModel):
    """
    Incoming chat request.
    """

    message: str


class ChatResponse(BaseModel):
    """
    Chat response.
    """

    answer: str

    sources: list[str]

    