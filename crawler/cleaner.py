"""
DEUS AI - Blog Ingestion Pipeline
---------------------------------

Cleaner module responsible for removing unnecessary HTML
from parsed blog posts.

Sprint 1 Scope:
- Remove script tags
- Remove style tags
- Remove navigation elements
- Remove footer elements
- Normalize whitespace
"""

from bs4 import BeautifulSoup

from crawler.models import BlogPost


class BlogCleaner:
    """
    Cleans BlogPost content for downstream processing.
    """

    def clean_html(self, html: str) -> str:
        """
        Clean raw HTML and return simplified HTML.
        """

        soup = BeautifulSoup(html, "lxml")

        # Remove unwanted elements
        for tag in soup(["script", "style", "noscript"]):
            tag.decompose()

        # Remove common Blogger layout elements
        for selector in [
            ".sidebar",
            ".header",
            ".footer",
            ".comments",
            ".navigation",
        ]:
            for element in soup.select(selector):
                element.decompose()

        return str(soup)

    def clean_post(self, post: BlogPost) -> BlogPost:
        """
        Clean a single BlogPost.
        """

        cleaned_html = self.clean_html(
            post.content.body
        )

        post.content.cleaned_html = cleaned_html

        return post

    def clean_posts(
        self,
        posts: list[BlogPost],
    ) -> list[BlogPost]:
        """
        Clean multiple BlogPost objects.
        """

        return [
            self.clean_post(post)
            for post in posts
        ]


def main() -> None:
    """
    Manual cleaner smoke test.
    """

    sample_html = """
    <html>
        <body>
            <script>alert("hello")</script>
            <h1>Hello DEUS AI</h1>
            <p>Cleaner Test</p>
        </body>
    </html>
    """

    cleaner = BlogCleaner()

    cleaned = cleaner.clean_html(sample_html)

    print(cleaned)


if __name__ == "__main__":
    main()

    