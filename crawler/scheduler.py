"""
DEUS AI Scheduler
-----------------

Runs the DEUS AI Knowledge Ingestion Pipeline
on a recurring schedule.
"""

import schedule
import time
from datetime import datetime

# Temporary for Sprint 3.5
# Eventually this will become:
#
# from pipeline.ingest import run_pipeline
#
# For now we continue using the crawler until
# the ingestion pipeline is completed.

from crawler.crawler import main as crawl_blog


def run_pipeline():
    """
    Execute the DEUS AI knowledge update.
    """

    print()
    print("=" * 60)
    print("DEUS AI Knowledge Refresh")
    print("=" * 60)

    print(
        f"Started : {datetime.now():%Y-%m-%d %H:%M:%S}"
    )

    crawl_blog()

    print(
        f"Finished: {datetime.now():%Y-%m-%d %H:%M:%S}"
    )

    print("=" * 60)
    print()


def main():
    """
    Schedule the ingestion pipeline.
    """

    print("=" * 60)
    print("DEUS AI Scheduler")
    print("=" * 60)

    print()

    print("Knowledge refresh scheduled every 7 days.")

    print()

    # Every 7 days
    schedule.every(7).days.do(run_pipeline)

    # Run once immediately
    run_pipeline()

    while True:

        schedule.run_pending()

        time.sleep(30)


if __name__ == "__main__":
    main()

    