from pathlib import Path

import chromadb


class ChromaStore:

    def __init__(
        self,
        persist_directory: str = "data/chroma",
        collection_name: str = "documents"
    ):
        Path(persist_directory).mkdir(
            parents=True,
            exist_ok=True
        )

        self.client = chromadb.PersistentClient(
            path=persist_directory
        )

        self.collection = self.client.get_or_create_collection(
            name=collection_name
        )

    def add_chunks(self, chunks, embeddings):
        """Store chunks and their embeddings in Chroma."""

        ids = [
            f"{chunk.source}_{chunk.chunk_id}"
            for chunk in chunks
        ]

        documents = [
            chunk.text
            for chunk in chunks
        ]

        metadatas = [
            {
                "source": chunk.source,
                "chunk_id": chunk.chunk_id,
                "chunking_method": chunk.chunking_method,
            }
            for chunk in chunks
        ]

        self.collection.upsert(
            ids=ids,
            documents=documents,
            embeddings=embeddings.tolist(),
            metadatas=metadatas
        )

    def search(self, query_embedding, n_results=5):
        """Search for the most similar chunks."""

        results = self.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=n_results
        )

        return results