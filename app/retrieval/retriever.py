from app.embeddings.embedder import Embedder
from app.reranking.reranker import Reranker
from app.vectorstore.chroma_store import ChromaStore


class Retriever:

    def __init__(
        self,
        collection_name: str = "documents"
    ):
        self.embedder = Embedder()

        self.store = ChromaStore(
            collection_name=collection_name
        )

        self.reranker = Reranker()

    def search(
        self,
        query: str,
        retrieve_k: int = 10,
        final_k: int = 3
    ):
        """
        Retrieve candidates from Chroma and rerank them.
        """

        # 1. Convert query into an embedding
        query_embedding = self.embedder.encode(
            [query]
        )[0]

        # 2. Retrieve candidates from Chroma
        results = self.store.search(
            query_embedding,
            n_results=retrieve_k
        )

        documents = results["documents"][0]

        if not documents:
            return []

        # 3. Rerank candidates
        reranked = self.reranker.rerank(
            query=query,
            documents=documents,
            top_k=final_k
        )

        return reranked