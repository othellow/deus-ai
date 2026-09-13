"""
DEUS AI - Blog Ingestion Pipeline
---------------------------------

Cleaner module responsible for removing unnecessary HTML
from parsed blog posts.

Sprint 3.5 Scope:

- Clean individual BlogPost objects
- Clean multiple BlogPost objects
- Remove unnecessary HTML
- Prepare content for Markdown export
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

        # Remove unwanted HTML elements
        for tag in soup(["script", "style", "noscript"]):
            tag.decompose()

        # Remove Blogger layout elements
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

    def clean(self, post: BlogPost) -> BlogPost:
        """
        Clean a single BlogPost.
        """

        cleaned_html = self.clean_html(
            post.content.body
        )

        post.content.cleaned_html = cleaned_html

        return post

    def clean_all(
        self,
        posts: list[BlogPost],
    ) -> list[BlogPost]:
        """
        Clean every BlogPost in the collection.
        """

        cleaned_posts: list[BlogPost] = []

        total = len(posts)

        print()
        print("=" * 60)
        print("DEUS AI Cleaner")
        print("=" * 60)

        for index, post in enumerate(posts, start=1):

            cleaned_posts.append(
                self.clean(post)
            )

            if (
                index <= 5
                or index == total
                or index % 100 == 0
            ):
                print(
                    f"✓ [{index}/{total}] "
                    f"{post.metadata.title}"
                )

        print()
        print("=" * 60)
        print("Cleaning Complete")
        print("=" * 60)
        print(f"Total cleaned posts: {len(cleaned_posts)}")

        return cleaned_posts


def main() -> None:
    """
    Manual cleaner smoke test.
    """

    sample_html = """
    <html>
        <body>
            <script>alert("hello")</script>
            <style>body {color:red;}</style>

            <h1>Hello DEUS AI</h1>

            <p>Cleaner Test</p>

            <noscript>No JavaScript</noscript>
        </body>
    </html>
    """

    cleaner = BlogCleaner()

    cleaned = cleaner.clean_html(sample_html)

    print(cleaned)


if __name__ == "__main__":
    main()

    