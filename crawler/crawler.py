"""
DEUS AI - Blog Ingestion Pipeline
---------------------------------

Blog crawler responsible for downloading BillyMacDeus'
entire Blogger archive.
"""

import logging
import re
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

from crawler.config import (
    BLOG_URL,
    LOG_LEVEL,
    MAX_RETRIES,
    RAW_DIR,
    REQUEST_TIMEOUT,
    RETRY_DELAY,
    USER_AGENT,
)

logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)


class BlogCrawler:

    def __init__(self):

        self.session = requests.Session()

        self.session.headers.update(
            {
                "User-Agent": USER_AGENT,
            }
        )

    # ----------------------------------------------------------

    def generate_filename(self, url: str) -> str:

        parsed = urlparse(url)

        path = parsed.path.strip("/")

        if not path:
            return "homepage.html"

        filename = path.replace("/", "-")

        if not filename.endswith(".html"):
            filename += ".html"

        filename = re.sub(r"[^a-zA-Z0-9._-]", "_", filename)

        return filename

    # ----------------------------------------------------------

    def save_raw_html(
        self,
        html: str,
        filename: str,
    ) -> Path:

        output = RAW_DIR / filename

        output.write_text(
            html,
            encoding="utf-8",
        )

        logger.info("Saved %s", output.name)

        return output

    # ----------------------------------------------------------

    def fetch_page(self, url: str) -> str:

        for attempt in range(
            1,
            MAX_RETRIES + 1,
        ):

            try:

                logger.info("Fetching %s", url)

                response = self.session.get(
                    url,
                    timeout=REQUEST_TIMEOUT,
                )

                response.raise_for_status()

                return response.text

            except requests.RequestException as exc:

                logger.warning(exc)

                if attempt == MAX_RETRIES:
                    raise

                time.sleep(RETRY_DELAY)

    # ----------------------------------------------------------

    def discover_article_links(
        self,
        html: str,
    ) -> list[str]:

        soup = BeautifulSoup(
            html,
            "lxml",
        )

        links = set()

        for a in soup.find_all(
            "a",
            href=True,
        ):

            href = a["href"]

            if (
                href.startswith(BLOG_URL)
                and ".html" in href
            ):
                links.add(href)

        return sorted(links)

    # ----------------------------------------------------------

    def discover_next_page(
        self,
        html: str,
    ) -> str | None:

        soup = BeautifulSoup(
            html,
            "lxml",
        )

        older = soup.find(
            "a",
            class_="blog-pager-older-link",
        )

        if older:

            return urljoin(
                BLOG_URL,
                older["href"],
            )

        return None

    # ----------------------------------------------------------

    def crawl_archive(self) -> list[str]:

        current = BLOG_URL

        all_articles = set()

        page = 1

        while current:

            logger.info(
                "Archive Page %s",
                page,
            )

            html = self.fetch_page(current)

            links = self.discover_article_links(html)

            all_articles.update(links)

            current = self.discover_next_page(html)

            page += 1

            time.sleep(0.5)

        logger.info(
            "Discovered %d unique articles.",
            len(all_articles),
        )

        return sorted(all_articles)

    # ----------------------------------------------------------

    def download_all_articles(
        self,
        urls: list[str],
    ):

        total = len(urls)

        logger.info(
            "Downloading %d articles...",
            total,
        )

        for index, url in enumerate(
            urls,
            start=1,
        ):

            filename = self.generate_filename(url)

            output = RAW_DIR / filename

            if output.exists():

                logger.info(
                    "[%d/%d] Skipping %s",
                    index,
                    total,
                    filename,
                )

                continue

            html = self.fetch_page(url)

            self.save_raw_html(
                html,
                filename,
            )

            time.sleep(0.5)

        logger.info("Download complete.")


def main():

    crawler = BlogCrawler()

    urls = crawler.crawl_archive()

    print()

    print("=" * 60)
    print("BLOG ARCHIVE")
    print("=" * 60)

    print(f"Articles discovered : {len(urls)}")

    print()

    crawler.download_all_articles(urls)

    print()

    print("=" * 60)
    print("CRAWL COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()

    