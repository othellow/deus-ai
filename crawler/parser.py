"""
DEUS AI - Blog Ingestion Pipeline
---------------------------------

Parser module responsible for converting Blogger HTML
into structured BlogPost objects.

Sprint 1 Scope:
- Parse homepage HTML
- Extract visible blog post previews
- Create BlogPost objects
"""

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

    def parse(self, html_file: Path) -> list[BlogPost]:
        """
        Parse the homepage HTML and extract all visible posts.

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

            # -----------------------------
            # Title
            # -----------------------------

            title = article_titles[index].get_text(
                strip=True
            )

            # -----------------------------
            # Body
            # -----------------------------

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

            # -----------------------------
            # Author
            # -----------------------------

            author = "Unknown"

            if index < len(article_authors):

                author = article_authors[index].get_text(
                    strip=True
                )

            # -----------------------------
            # Publish Date
            # -----------------------------

            publish_date = date.today()

            if index < len(article_dates):
                # Sprint 1 placeholder.
                # Blogger stores dates as text.
                pass

            # -----------------------------
            # Labels
            # -----------------------------

            labels: list[str] = []

            if index < len(article_labels):

                labels = [
                    label.get_text(strip=True)
                    for label in article_labels[index].find_all("a")
                ]

            # -----------------------------
            # Slug
            # -----------------------------

            slug = title.lower().replace(" ", "-")

            # -----------------------------
            # URL
            # -----------------------------

            article_link = ""

            link = article_titles[index].find("a")

            if link:

                article_link = link.get("href", "")

            # -----------------------------
            # Build BlogPost
            # -----------------------------

            metadata = BlogMetadata(
                title=title,
                slug=slug,
                author=author,
                publish_date=publish_date,
                categories=labels,
                tags=labels,
                source_url=article_link or "https://blog.billymacdeus.com/",
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


def main() -> None:
    """
    Manual parser test.
    """

    parser = BlogParser()

    posts = parser.parse(
        Path("data/raw/homepage.html")
    )

    print("=" * 60)
    print("DEUS AI - Parser Results")
    print("=" * 60)

    print(f"Posts discovered: {len(posts)}")

    for index, post in enumerate(posts, start=1):

        print("\n--------------------------------------")

        print(f"Post #{index}")

        print(f"Title      : {post.metadata.title}")

        print(f"Author     : {post.metadata.author}")

        print(f"Labels     : {post.metadata.categories}")

        print(f"Images     : {len(post.content.images)}")

        print(f"Body Length: {len(post.content.body)} characters")


if __name__ == "__main__":
    main()

    