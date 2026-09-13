"""
DEUS AI Backend API
-------------------
"""

from fastapi import FastAPI

from api.routes import router

app = FastAPI(
    title="DEUS AI API",
    description="Conversational AI for BillyMacDeus' Blog",
    version="1.0.0",
)

app.include_router(router)


@app.get("/")
def root():
    """
    Root endpoint.
    """

    return {
        "message": "Welcome to DEUS AI",
        "docs": "/docs",
    }

