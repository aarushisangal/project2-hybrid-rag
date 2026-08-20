from app.chunking.pipeline import create_chunks
from app.embeddings.embedder import Embedder
from app.vectorstore.chroma_store import ChromaStore


text = """
Machine learning is a branch of artificial intelligence that allows computers to learn from data.

Supervised learning uses labeled examples to train predictive models.

Classification and regression are common supervised learning tasks.

Relational databases organize information into tables.

Database indexing improves the speed of data retrieval.

B-tree indexes are commonly used in relational databases.
"""


# Step 1: Create chunks
chunks = create_chunks(
    text,
    source="test_document.txt",
    method="semantic"
)

print(f"Created {len(chunks)} chunks")


# Step 2: Create embeddings
embedder = Embedder()

texts = [chunk.text for chunk in chunks]

embeddings = embedder.encode(texts)

print(f"Created {len(embeddings)} embeddings")


# Step 3: Store in Chroma
store = ChromaStore(
    persist_directory="data/chroma",
    collection_name="test_documents"
)

store.add_chunks(
    chunks,
    embeddings
)

print("Chunks stored in ChromaDB")


# Step 4: Search
query = "What is machine learning?"

query_embedding = embedder.encode([query])[0]

results = store.search(
    query_embedding,
    n_results=3
)


print("\n===== SEARCH RESULTS =====")

for i, document in enumerate(
    results["documents"][0],
    start=1
):

    print(f"\nResult {i}")
    print("-" * 50)
    print(document)