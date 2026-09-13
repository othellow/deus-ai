
"""
Unit tests for crawler.parser
"""

from pathlib import Path

from crawler.parser import BlogParser


def test_load_html():
    """
    Ensure HTML loads successfully.
    """

    parser = BlogParser()

    soup = parser.load_html(
        Path("data/raw/homepage.html")
    )

    assert soup is not None

    