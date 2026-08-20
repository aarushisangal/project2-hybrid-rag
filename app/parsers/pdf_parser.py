from pathlib import Path
import fitz


def read_pdf(file_path: Path) -> str:
    """
    Extract text from a PDF file.

    Args:
        file_path: Path to the PDF file.

    Returns:
        Extracted text from all pages.
    """

    text = []

    with fitz.open(file_path) as document:
        for page in document:
            page_text = page.get_text()

            if page_text:
                text.append(page_text)

    return "\n".join(text)