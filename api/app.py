"""
DEUS AI Backend API
-------------------

Main FastAPI application.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes import router

app = FastAPI(
    title="DEUS AI API",
    description="Conversational AI for BillyMacDeus' Blog",
    version="1.0.0",
)

# ---------------------------------------------------------
# Enable CORS
# ---------------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------
# Register API Routes
# ---------------------------------------------------------

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

