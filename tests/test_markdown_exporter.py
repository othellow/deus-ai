
"""
Unit tests for crawler.markdown_exporter
"""

from datetime import date

from crawler.markdown_exporter import MarkdownExporter
from crawler.models import BlogContent, BlogMetadata, BlogPost


def test_generate_markdown():
    """
    Ensure markdown is generated.
    """

    metadata = BlogMetadata(
        title="Test",
        slug="test",
        author="Billy",
        publish_date=date.today(),
        categories=[],
        tags=[],
        source_url="https://blog.billymacdeus.com/",
    )

    content = BlogContent(
        body="Hello World",
        images=[],
    )

    post = BlogPost(
        metadata=metadata,
        content=content,
    )

    exporter = MarkdownExporter()

    markdown = exporter.generate_markdown(post)

    assert "# Test" in markdown