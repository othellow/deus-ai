"""
DEUS AI OpenAI Service
----------------------

Handles communication with the OpenAI Responses API.
"""

import os

from dotenv import load_dotenv
from openai import OpenAI, RateLimitError
from openai import OpenAIError

from crawler.config import OPENAI_MODEL

load_dotenv()


class AIService:
    """
    Generates responses using the OpenAI Responses API.
    """

    def __init__(self) -> None:
        """
        Lazily initialize the OpenAI client.

        This prevents GitHub Actions and unit tests from
        failing simply by importing this module.
        """

        api_key = os.getenv("OPENAI_API_KEY")

        self.client = (
            OpenAI(api_key=api_key)
            if api_key
            else None
        )

    def generate(self, prompt: str) -> str:
        """
        Generate a response from OpenAI.
        """

        if self.client is None:

            return (
                "DEUS AI is not configured. "
                "Missing OPENAI_API_KEY."
            )

        try:

            response = self.client.responses.create(
                model=OPENAI_MODEL,
                instructions=(
                    "You are DEUS AI, the conversational companion "
                    "for BillyMacDeus' published writings. "
                    "Answer ONLY using the supplied context. "
                    "If the answer is not present in the context, "
                    "say you don't know."
                ),
                input=prompt,
            )

            return response.output_text

        except RateLimitError:

            return (
                "DEUS AI is temporarily unavailable because "
                "the OpenAI API account has no remaining credits."
            )

        except OpenAIError as exc:

            return f"OpenAI Error: {exc}"

        except Exception as exc:

            return (
                f"DEUS AI encountered an unexpected error: {exc}"
            )
        
        