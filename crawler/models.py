"""
DEUS AI - Blog Ingestion Pipeline
---------------------------------
Pydantic data models used throughout the ingestion pipeline.

These models provide a consistent data contract between the
crawler, parser, cleaner, markdown exporter, storage layer,
and future RAG components.
"""

from datetime import date
from typing import List

from pydantic import AnyHttpUrl, BaseModel, Field


class BlogMetadata(BaseModel):
    """
    Metadata extracted from a blog article.
    """

    title: str = Field(
        ...,
        description="Article title",
    )

    slug: str = Field(
        ...,
        description="Unique URL slug",
    )

    author: str = Field(
        ...,
        description="Author name",
    )

    publish_date: date = Field(
        ...,
        description="Publication date",
    )

    categories: List[str] = Field(
        default_factory=list,
        description="Article categories",
    )

    tags: List[str] = Field(
        default_factory=list,
        description="Article tags",
    )

    source_url: AnyHttpUrl = Field(
        ...,
        description="Original article URL",
    )


class BlogContent(BaseModel):
    """
    Content extracted from the article.
    """

    body: str = Field(
        ...,
        description="Main article text",
    )

    images: List[str] = Field(
        default_factory=list,
        description="Image URLs",
    )

    cleaned_html: str = Field(
        default="",
        description="Cleaned HTML",
    )

    markdown: str = Field(
        default="",
        description="Markdown version",
    )


class BlogPost(BaseModel):
    """
    Complete blog article.

    Combines metadata and content into a single object
    used throughout the ingestion pipeline.
    """

    metadata: BlogMetadata

    content: BlogContent