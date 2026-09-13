"""
DEUS AI OpenAI Service
----------------------

Handles communication with the OpenAI Responses API.
"""

import os

from dotenv import load_dotenv
from openai import OpenAI
from openai import APIError
from openai import RateLimitError

from crawler.config import OPENAI_MODEL

# ------------------------------------------------------------------
# Load environment variables
# ------------------------------------------------------------------

load_dotenv()

# ------------------------------------------------------------------
# Initialize OpenAI client
# ------------------------------------------------------------------

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)


class AIService:
    """
    Generates responses using the OpenAI Responses API.
    """

    def generate(self, prompt: str) -> str:
        """
        Send a Retrieval-Augmented Generation (RAG) prompt
        to OpenAI and return the generated answer.
        """

        try:

            response = client.responses.create(
                model=OPENAI_MODEL,
                instructions=(
                    "You are DEUS AI, the conversational companion "
                    "for BillyMacDeus' published writings.\n\n"
                    "Answer ONLY using the supplied context.\n"
                    "Do not invent information.\n"
                    "If the answer cannot be found in the supplied "
                    "context, politely say you don't know."
                ),
                input=prompt,
            )

            return response.output_text

        except RateLimitError:

            return (
                "DEUS AI is temporarily unavailable because "
                "the OpenAI API account has no remaining credits."
            )

        except APIError as exc:

            return (
                "OpenAI API error: "
                f"{exc}"
            )

        except Exception as exc:

            return (
                "DEUS AI encountered an unexpected error: "
                f"{exc}"
            )
        
        