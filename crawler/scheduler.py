"""
DEUS AI - Blog Ingestion Pipeline
---------------------------------

Scheduler responsible for periodically running
the blog ingestion pipeline.

Sprint 1 Scope:
- Schedule weekly ingestion
- Demonstrate scheduled execution
"""

import time

import schedule

from crawler.config import BLOG_URL
from crawler.crawler import BlogCrawler


def run_ingestion() -> None:
    """
    Execute the blog crawler.
    """

    print("=" * 60)
    print("DEUS AI Scheduler")
    print("=" * 60)

    crawler = BlogCrawler()

    crawler.fetch_page(BLOG_URL)

    print("Blog crawl completed.")


def main() -> None:
    """
    Configure the scheduler.
    """

    print("Starting scheduler...")

    # Sprint 1 Demo:
    # Run every 10 seconds instead of weekly.
    schedule.every(10).seconds.do(run_ingestion)

    print("Press CTRL+C to stop.\n")

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()

    