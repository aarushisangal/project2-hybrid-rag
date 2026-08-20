from app.reranking.reranker import Reranker


query = "What is machine learning?"

documents = [
    "Machine learning is a branch of artificial intelligence that allows computers to learn from data.",
    "Relational databases organize information into tables consisting of rows and columns.",
    "Supervised learning is a machine learning technique that uses labeled training data.",
    "B-tree indexes are commonly used to improve database query performance.",
]


reranker = Reranker()

results = reranker.rerank(
    query=query,
    documents=documents,
    top_k=3
)


print("\n===== RERANKED RESULTS =====")

for rank, (document, score) in enumerate(results, start=1):

    print(f"\nRank {rank}")
    print(f"Score: {float(score):.4f}")
    print("-" * 50)
    print(document)