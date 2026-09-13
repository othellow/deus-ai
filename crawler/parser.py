"""
DEUS AI - Blog Ingestion Pipeline
---------------------------------

Parser module responsible for converting Blogger HTML
into structured BlogPost objects.

Sprint 3.5 Scope:

- Parse individual HTML files
- Parse all downloaded HTML files
- Extract blog post metadata
- Create BlogPost objects
"""

import re
from datetime import date
from pathlib import Path

from bs4 import BeautifulSoup

from crawler.models import BlogContent, BlogMetadata, BlogPost


class BlogParser:
    """
    Parses Blogger HTML pages into BlogPost objects.
    """

    def load_html(self, html_file: Path) -> BeautifulSoup:
        """
        Load an HTML file into BeautifulSoup.
        """

        html = html_file.read_text(
            encoding="utf-8",
        )

        return BeautifulSoup(html, "lxml")

    def generate_slug(self, title: str) -> str:
        """
        Generate a filesystem-safe slug from a title.
        """

        slug = title.lower()

        # Replace anything that's not a-z or 0-9 with "-"
        slug = re.sub(
            r"[^a-z0-9]+",
            "-",
            slug,
        )

        # Remove duplicate hyphens
        slug = re.sub(
            r"-+",
            "-",
            slug,
        )

        # Remove leading/trailing hyphens
        slug = slug.strip("-")

        # Fallback in case title becomes empty
        if not slug:
            slug = "untitled-post"

        return slug

    def parse(self, html_file: Path) -> list[BlogPost]:
        """
        Parse a Blogger HTML page and extract all visible posts.

        Args:
            html_file:
                HTML file downloaded by crawler.py

        Returns:
            List of BlogPost objects.
        """

        soup = self.load_html(html_file)

        posts: list[BlogPost] = []

        article_titles = soup.select("h3.post-title.entry-title")
        article_bodies = soup.select("div.post-body.entry-content")
        article_authors = soup.select("span.post-author.vcard")
        article_dates = soup.select("span.post-timestamp")
        article_labels = soup.select("span.post-labels")

        total_posts = len(article_titles)

        for index in range(total_posts):

            # -------------------------------------------------
            # Title
            # -------------------------------------------------

            title = article_titles[index].get_text(
                strip=True
            )

            # -------------------------------------------------
            # Body
            # -------------------------------------------------

            body = ""

            images: list[str] = []

            if index < len(article_bodies):

                body = article_bodies[index].get_text(
                    separator="\n",
                    strip=True,
                )

                images = [
                    img.get("src")
                    for img in article_bodies[index].find_all("img")
                    if img.get("src")
                ]

            # -------------------------------------------------
            # Author
            # -------------------------------------------------

            author = "Unknown"

            if index < len(article_authors):

                author = article_authors[index].get_text(
                    strip=True
                )

            # -------------------------------------------------
            # Publish Date
            # -------------------------------------------------

            publish_date = date.today()

            if index < len(article_dates):
                # Future enhancement:
                # Parse Blogger date text.
                pass

            # -------------------------------------------------
            # Labels
            # -------------------------------------------------

            labels: list[str] = []

            if index < len(article_labels):

                labels = [
                    label.get_text(strip=True)
                    for label in article_labels[index].find_all("a")
                ]

            # -------------------------------------------------
            # Slug
            # -------------------------------------------------

            slug = self.generate_slug(title)

            # -------------------------------------------------
            # URL
            # -------------------------------------------------

            article_link = ""

            link = article_titles[index].find("a")

            if link:

                article_link = link.get("href", "")

            # -------------------------------------------------
            # Build BlogPost
            # -------------------------------------------------

            metadata = BlogMetadata(
                title=title,
                slug=slug,
                author=author,
                publish_date=publish_date,
                categories=labels,
                tags=labels,
                source_url=article_link
                or "https://blog.billymacdeus.com/",
            )

            content = BlogContent(
                body=body,
                images=images,
                cleaned_html="",
                markdown="",
            )

            posts.append(
                BlogPost(
                    metadata=metadata,
                    content=content,
                )
            )

        return posts

    def parse_all(self, raw_dir: Path) -> list[BlogPost]:
        """
        Parse every HTML file inside the raw directory.

        Args:
            raw_dir:
                Directory containing downloaded HTML files.

        Returns:
            Combined list of BlogPost objects.
        """

        all_posts: list[BlogPost] = []

        html_files = sorted(raw_dir.glob("*.html"))

        print("=" * 60)
        print("DEUS AI Parser")
        print("=" * 60)
        print(f"HTML files found: {len(html_files)}")
        print()

        for html_file in html_files:

            try:

                posts = self.parse(html_file)

                all_posts.extend(posts)

                print(
                    f"✓ {html_file.name:<45}"
                    f"{len(posts)} post(s)"
                )

            except Exception as exc:

                print(
                    f"✗ Failed: {html_file.name}"
                )

                print(exc)

        print()
        print("=" * 60)
        print("Parsing Complete")
        print("=" * 60)
        print(f"Total BlogPosts: {len(all_posts)}")

        return all_posts


def main() -> None:
    """
    Manual parser test.
    """

    parser = BlogParser()

    posts = parser.parse_all(
        Path("data/raw")
    )

    print()
    print("=" * 60)
    print("Preview")
    print("=" * 60)

    for index, post in enumerate(posts[:5], start=1):

        print(f"{index}. {post.metadata.title}")

    print()
    print(f"Total parsed BlogPosts: {len(posts)}")


if __name__ == "__main__":
    main()

    