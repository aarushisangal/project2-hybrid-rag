from dataclasses import dataclass
from typing import Optional


@dataclass
class Chunk:
    chunk_id: int
    text: str
    source: str
    chunking_method: str
    page_number: Optional[int] = None