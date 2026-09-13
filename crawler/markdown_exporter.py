"""
DEUS AI - Blog Ingestion Pipeline
---------------------------------

Markdown exporter responsible for converting BlogPost
objects into Markdown and JSON metadata files.

Sprint 3.5 Scope:

- Export individual BlogPosts
- Export multiple BlogPosts
- Generate Markdown
- Generate JSON metadata
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

        output_file = (
            METADATA_DIR /
            f"{post.metadata.slug}.json"
        )

        output_file.write_text(
            json.dumps(
                metadata,
                indent=4,
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )

        return output_file

    def export(self, post: BlogPost) -> tuple[Path, Path]:
        """
        Export a single BlogPost.

        Returns:
            Markdown file path and metadata file path.
        """

        markdown_file = (
            MARKDOWN_DIR /
            f"{post.metadata.slug}.md"
        )

        markdown_file.write_text(
            self.generate_markdown(post),
            encoding="utf-8",
        )

        metadata_file = self.export_metadata(post)

        return markdown_file, metadata_file

    def export_all(
        self,
        posts: list[BlogPost],
    ) -> list[tuple[Path, Path]]:
        """
        Export every BlogPost in the collection.
        """

        exported: list[tuple[Path, Path]] = []

        total = len(posts)

        print()
        print("=" * 60)
        print("DEUS AI Markdown Exporter")
        print("=" * 60)

        for index, post in enumerate(posts, start=1):

            exported.append(
                self.export(post)
            )

            if (
                index <= 5
                or index == total
                or index % 100 == 0
            ):
                print(
                    f"✓ [{index}/{total}] "
                    f"{post.metadata.slug}"
                )

        print()
        print("=" * 60)
        print("Markdown Export Complete")
        print("=" * 60)

        print(f"Markdown files : {len(exported)}")
        print(f"Metadata files : {len(exported)}")

        return exported


def main() -> None:
    """
    Manual exporter smoke test.
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
        cleaned_html="",
        markdown="",
    )

    post = BlogPost(
        metadata=metadata,
        content=content,
    )

    exporter = MarkdownExporter()

    markdown_file, metadata_file = exporter.export(post)

    print("Markdown File:")
    print(markdown_file)

    print()

    print("Metadata File:")
    print(metadata_file)


if __name__ == "__main__":
    main()

    