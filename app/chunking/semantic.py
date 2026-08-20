import re

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class SemanticChunker:

    def __init__(
        self,
        model_name: str = "BAAI/bge-small-en-v1.5",
        similarity_threshold: float = 0.70,
    ):
        self.model = SentenceTransformer(model_name)
        self.similarity_threshold = similarity_threshold

    def _split_paragraphs(self, text: str) -> list[str]:
        """Split document text into paragraphs."""

        text = re.sub(r"\n{3,}", "\n\n", text.strip())

        paragraphs = [
            paragraph.strip()
            for paragraph in re.split(r"\n\s*\n", text)
            if paragraph.strip()
        ]

        return paragraphs

    def chunk(self, text: str) -> list[str]:
        """Create chunks based on semantic similarity."""

        paragraphs = self._split_paragraphs(text)

        if not paragraphs:
            return []

        if len(paragraphs) == 1:
            return paragraphs

        embeddings = self.model.encode(
            paragraphs,
            normalize_embeddings=True
        )

        chunks = []
        current_chunk = [paragraphs[0]]

        for i in range(1, len(paragraphs)):

            similarity = cosine_similarity(
                [embeddings[i - 1]],
                [embeddings[i]]
            )[0][0]

            if similarity >= self.similarity_threshold:
                current_chunk.append(paragraphs[i])
            else:
                chunks.append("\n\n".join(current_chunk))
                current_chunk = [paragraphs[i]]

        if current_chunk:
            chunks.append("\n\n".join(current_chunk))

        return chunks