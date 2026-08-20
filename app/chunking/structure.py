import re


def structure_chunking(
    text: str,
    max_chunk_size: int = 1000
) -> list[str]:
    """
    Split a document while trying to preserve paragraph and section structure.

    Args:
        text: Extracted document text.
        max_chunk_size: Maximum preferred size of a chunk.

    Returns:
        List of structure-aware chunks.
    """

    if not text or not text.strip():
        return []

    # Normalize excessive whitespace
    text = re.sub(r"\n{3,}", "\n\n", text.strip())

    # Split document into paragraphs
    paragraphs = [
        paragraph.strip()
        for paragraph in re.split(r"\n\s*\n", text)
        if paragraph.strip()
    ]

    chunks = []
    current_chunk = ""

    for paragraph in paragraphs:

        # If adding this paragraph stays within the limit
        if len(current_chunk) + len(paragraph) + 2 <= max_chunk_size:

            if current_chunk:
                current_chunk += "\n\n"

            current_chunk += paragraph

        else:

            if current_chunk:
                chunks.append(current_chunk)

            # If a single paragraph is larger than max_chunk_size,
            # keep it as its own chunk for now.
            current_chunk = paragraph

    if current_chunk:
        chunks.append(current_chunk)

    return chunks