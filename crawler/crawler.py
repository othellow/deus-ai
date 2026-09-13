"""
DEUS AI - Blog Ingestion Pipeline
---------------------------------

Blog crawler responsible for downloading raw HTML from
BillyMacDeus' blog.

Responsibilities:
- Download HTML pages
- Handle retries
- Configure request headers
- Validate HTTP responses
- Generate output filenames
- Save raw HTML
- Return raw HTML

Parsing and content extraction are intentionally handled
by parser.py to keep responsibilities separate.
"""

import logging
import re
import time
from pathlib import Path
from urllib.parse import urlparse

import requests

from crawler.config import (
    BLOG_URL,
    LOG_LEVEL,
    MAX_RETRIES,
    RAW_DIR,
    REQUEST_TIMEOUT,
    RETRY_DELAY,
    USER_AGENT,
)

# ============================================================================
# Logging Configuration
# ============================================================================

logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)


class BlogCrawler:
    """
    Downloads HTML pages from BillyMacDeus' blog.
    """

    def __init__(self) -> None:
        """
        Initialize a reusable HTTP session.
        """

        self.session = requests.Session()

        self.session.headers.update(
            {
                "User-Agent": USER_AGENT,
            }
        )

    def generate_filename(self, url: str) -> str:
        """
        Generate a safe filename based on the URL.

        Examples:
            https://blog.billymacdeus.com/
                -> homepage.html

            https://blog.billymacdeus.com/2025/03/my-post.html
                -> my-post.html
        """

        parsed = urlparse(url)

        path = parsed.path.strip("/")

        if not path:
            return "homepage.html"

        filename = path.split("/")[-1]

        if not filename.endswith(".html"):
            filename = f"{filename}.html"

        # Replace unsafe filename characters
        filename = re.sub(r"[^a-zA-Z0-9._-]", "_", filename)

        return filename

    def save_raw_html(self, html: str, filename: str) -> Path:
        """
        Save downloaded HTML into the raw data directory.

        Args:
            html:
                Raw HTML content.

            filename:
                Output filename.

        Returns:
            Path to the saved HTML file.
        """

        output_file = RAW_DIR / filename

        output_file.write_text(
            html,
            encoding="utf-8",
        )

        logger.info("Saved raw HTML to %s", output_file)

        return output_file

    def fetch_page(self, url: str) -> str:
        """
        Download a single web page.

        Args:
            url:
                URL to download.

        Returns:
            Raw HTML.

        Raises:
            requests.RequestException:
                Raised if all retry attempts fail.
        """

        for attempt in range(1, MAX_RETRIES + 1):

            try:
                logger.info(
                    "Fetching %s (Attempt %s/%s)",
                    url,
                    attempt,
                    MAX_RETRIES,
                )

                response = self.session.get(
                    url,
                    timeout=REQUEST_TIMEOUT,
                )

                response.raise_for_status()

                logger.info("Download successful.")

                filename = self.generate_filename(url)

                self.save_raw_html(
                    html=response.text,
                    filename=filename,
                )

                return response.text

            except requests.RequestException as exc:

                logger.warning(
                    "Attempt %s failed: %s",
                    attempt,
                    exc,
                )

                if attempt == MAX_RETRIES:
                    logger.error("Maximum retries exceeded.")
                    raise

                time.sleep(RETRY_DELAY)


def main() -> None:
    """
    Manual test for the crawler.
    """

    crawler = BlogCrawler()

    html = crawler.fetch_page(BLOG_URL)

    print("\nFirst 500 characters of downloaded HTML:\n")
    print(html[:500])


if __name__ == "__main__":
    main()
    