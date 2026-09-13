"""
DEUS AI - RAG Knowledge Engine
------------------------------

Chunker responsible for splitting Markdown documents
into overlapping chunks for semantic search.

Sprint 2 Scope:
- Read Markdown files
- Split into chunks
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

        Args:
            chunk_size:
                Maximum number of characters per chunk.

            overlap:
                Number of overlapping characters.
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

            chunk = text[start:end]

            chunks.append(chunk)

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

        chunks = self.split_text(text)

        output = []

        for index, chunk in enumerate(chunks):

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
        Process every Markdown file.
        """

        markdown_files = sorted(
            MARKDOWN_DIR.glob("*.md")
        )

        total_chunks = 0

        for markdown_file in markdown_files:

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

            print(
                f"✔ {markdown_file.name} → "
                f"{len(chunks)} chunks"
            )

            total_chunks += len(chunks)

        return total_chunks


def main() -> None:
    """
    Manual chunker test.
    """

    chunker = Chunker()

    total = chunker.process_all()

    print("\n===============================")

    print(f"Total chunks created: {total}")

    print("===============================")


if __name__ == "__main__":
    main()