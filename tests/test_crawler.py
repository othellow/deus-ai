"""
Unit tests for crawler.crawler
"""

from crawler.crawler import BlogCrawler


def test_generate_filename():
    """
    Ensure filenames are generated correctly and include
    the year/month prefix for uniqueness.
    """

    crawler = BlogCrawler()

    filename = crawler.generate_filename(
        "https://blog.billymacdeus.com/2026/09/test.html"
    )

    assert filename == "2026-09-test.html"

    