from sentence_transformers import SentenceTransformer


class Embedder:

    def __init__(
        self,
        model_name: str = "BAAI/bge-small-en-v1.5"
    ):
        self.model = SentenceTransformer(model_name)

    def encode(self, texts: list[str]):
        """
        Convert text into vector embeddings.
        """

        return self.model.encode(
            texts,
            normalize_embeddings=True
        )