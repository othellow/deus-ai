
"""
Unit tests for crawler.cleaner
"""

from crawler.cleaner import BlogCleaner


def test_clean_html():
    """
    Ensure script tags are removed.
    """

    cleaner = BlogCleaner()

    html = """
    <html>
        <script>alert(1)</script>
        <body>Hello</body>
    </html>
    """

    cleaned = cleaner.clean_html(html)

    assert "<script>" not in cleaned

    