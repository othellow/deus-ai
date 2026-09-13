"""
Unit tests for crawler.models
"""

from datetime import date

from crawler.models import BlogMetadata


def test_blog_metadata_creation():
    """
    Ensure BlogMetadata can be created.
    """

    metadata = BlogMetadata(
        title="Test",
        slug="test",
        author="Billy",
        publish_date=date.today(),
        categories=["AI"],
        tags=["Python"],
        source_url="https://blog.billymacdeus.com/",
    )

    assert metadata.title == "Test"

    