from app.retrieval.retriever import Retriever


retriever = Retriever(
    collection_name="test_documents"
)


query = "What is machine learning?"


results = retriever.search(
    query=query,
    retrieve_k=2,
    final_k=2
)


print("\n===== FINAL RETRIEVAL RESULTS =====")


for rank, (document, score) in enumerate(
    results,
    start=1
):

    print(f"\nRank {rank}")
    print(f"Score: {float(score):.4f}")
    print("-" * 50)
    print(document)