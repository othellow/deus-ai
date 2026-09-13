
"""
Unit tests for crawler.config
"""

from crawler.config import BLOG_URL


def test_blog_url_exists():
    """
    Ensure BLOG_URL is configured.
    """

    assert BLOG_URL.startswith("https://")

    