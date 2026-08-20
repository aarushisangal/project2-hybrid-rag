from pathlib import Path

from app.chunking.character import character_chunking
from app.chunking.structure import structure_chunking
from app.chunking.semantic import SemanticChunker
from app.models.chunk import Chunk


def create_chunks(
    text: str,
    source: str,
    method: str = "character",
) -> list[Chunk]:
    """
    Create standardized Chunk objects using the selected strategy.
    """

    if method == "character":

        raw_chunks = character_chunking(text)

    elif method == "structure":

        raw_chunks = structure_chunking(text)

    elif method == "semantic":

        semantic_chunker = SemanticChunker()
        raw_chunks = semantic_chunker.chunk(text)

    else:
        raise ValueError(
            f"Unsupported chunking method: {method}"
        )

    chunks = []

    for index, chunk_text in enumerate(raw_chunks):

        chunks.append(
            Chunk(
                chunk_id=index,
                text=chunk_text,
                source=source,
                chunking_method=method,
            )
        )

    return chunks