"""
DEUS AI - RAG Knowledge Engine
------------------------------

Chunker responsible for splitting Markdown documents
into overlapping chunks for semantic search.

Sprint 3 Scope:

- Read all Markdown files
- Split into overlapping chunks
- Save chunk JSON files
"""

import json
from pathlib import Path

from crawler.config import CHUNKS_DIR, MARKDOWN_DIR


class Chunker:
    """
    Splits Markdown documents into AI-friendly chunks.
    """

    def __init__(
        self,
        chunk_size: int = 500,
        overlap: int = 100,
    ) -> None:
        """
        Initialize chunking parameters.
        """

        self.chunk_size = chunk_size
        self.overlap = overlap

    def split_text(
        self,
        text: str,
    ) -> list[str]:
        """
        Split text into overlapping chunks.
        """

        chunks = []

        start = 0

        while start < len(text):

            end = start + self.chunk_size

            chunks.append(text[start:end])

            start += self.chunk_size - self.overlap

        return chunks

    def process_markdown(
        self,
        markdown_file: Path,
    ) -> list[dict]:
        """
        Process one Markdown file.
        """

        text = markdown_file.read_text(
            encoding="utf-8",
        )

        pieces = self.split_text(text)

        output = []

        for index, chunk in enumerate(pieces):

            output.append(
                {
                    "chunk_id": index,
                    "source": markdown_file.name,
                    "text": chunk,
                }
            )

        return output

    def process_all(self) -> int:
        """
        Process every Markdown document.
        """

        markdown_files = sorted(
            MARKDOWN_DIR.glob("*.md")
        )

        total_chunks = 0

        print("=" * 60)
        print("DEUS AI Chunker")
        print("=" * 60)
        print(f"Markdown files: {len(markdown_files)}")
        print()

        for index, markdown_file in enumerate(markdown_files, start=1):

            chunks = self.process_markdown(
                markdown_file
            )

            output_file = (
                CHUNKS_DIR /
                f"{markdown_file.stem}.json"
            )

            output_file.write_text(
                json.dumps(
                    chunks,
                    indent=4,
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )

            total_chunks += len(chunks)

            if (
                index <= 5
                or index == len(markdown_files)
                or index % 100 == 0
            ):
                print(
                    f"✓ [{index}/{len(markdown_files)}] "
                    f"{markdown_file.name} "
                    f"({len(chunks)} chunks)"
                )

        print()
        print("=" * 60)
        print("Chunking Complete")
        print("=" * 60)
        print(f"Total chunks created: {total_chunks}")

        return total_chunks


def main() -> None:
    """
    Manual chunker test.
    """

    chunker = Chunker()

    total = chunker.process_all()

    print()
    print("=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"Chunks created: {total}")


if __name__ == "__main__":
    main()

    