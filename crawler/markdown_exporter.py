"""
DEUS AI - Blog Ingestion Pipeline
---------------------------------

Markdown exporter responsible for converting BlogPost
objects into Markdown and JSON metadata files.

Sprint 1 Scope:
- Export one Markdown file per BlogPost
- Export one metadata JSON per BlogPost
"""

import json
from pathlib import Path

from crawler.config import MARKDOWN_DIR, METADATA_DIR
from crawler.models import BlogPost


class MarkdownExporter:
    """
    Exports BlogPost objects into Markdown and metadata files.
    """

    def generate_markdown(self, post: BlogPost) -> str:
        """
        Convert a BlogPost into Markdown.
        """

        return f"""# {post.metadata.title}

**Author:** {post.metadata.author}

**Published:** {post.metadata.publish_date}

**Categories:** {", ".join(post.metadata.categories)}

**Tags:** {", ".join(post.metadata.tags)}

**Source:** {post.metadata.source_url}

---

{post.content.body}
"""

    def export_metadata(self, post: BlogPost) -> Path:
        """
        Export BlogPost metadata as JSON.
        """

        metadata = {
            "title": post.metadata.title,
            "slug": post.metadata.slug,
            "author": post.metadata.author,
            "publish_date": str(post.metadata.publish_date),
            "categories": post.metadata.categories,
            "tags": post.metadata.tags,
            "source_url": str(post.metadata.source_url),
        }

        output_file = METADATA_DIR / f"{post.metadata.slug}.json"

        output_file.write_text(
            json.dumps(metadata, indent=4, ensure_ascii=False),
            encoding="utf-8",
        )

        return output_file

    def export_post(self, post: BlogPost) -> tuple[Path, Path]:
        """
        Export one BlogPost as Markdown and JSON metadata.

        Returns:
            Tuple containing:
            - Markdown file path
            - Metadata JSON path
        """

        markdown_file = MARKDOWN_DIR / f"{post.metadata.slug}.md"

        markdown_file.write_text(
            self.generate_markdown(post),
            encoding="utf-8",
        )

        metadata_file = self.export_metadata(post)

        return markdown_file, metadata_file

    def export_posts(
        self,
        posts: list[BlogPost],
    ) -> list[tuple[Path, Path]]:
        """
        Export multiple BlogPosts.
        """

        return [
            self.export_post(post)
            for post in posts
        ]


def main() -> None:
    """
    Manual exporter test.
    """

    from datetime import date

    from crawler.models import (
        BlogContent,
        BlogMetadata,
    )

    metadata = BlogMetadata(
        title="DEUS AI Test",
        slug="deus-ai-test",
        author="Billy",
        publish_date=date.today(),
        categories=["AI"],
        tags=["Python"],
        source_url="https://blog.billymacdeus.com/",
    )

    content = BlogContent(
        body="Hello Markdown!",
        images=[],
    )

    post = BlogPost(
        metadata=metadata,
        content=content,
    )

    exporter = MarkdownExporter()

    markdown_file, metadata_file = exporter.export_post(post)

    print("Markdown File:")
    print(markdown_file)

    print("\nMetadata File:")
    print(metadata_file)


if __name__ == "__main__":
    main()

    