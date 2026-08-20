from app.chunking.semantic import SemanticChunker


text = """
Machine learning is a branch of artificial intelligence that allows computers to learn from data.

Supervised learning uses labeled examples to train predictive models.

Classification and regression are two common supervised learning tasks.

Relational databases organize information into tables consisting of rows and columns.

Database indexing improves the speed of data retrieval operations.

B-tree indexes are commonly used in relational database systems.
"""


chunker = SemanticChunker(
    similarity_threshold=0.70
)

chunks = chunker.chunk(text)

print(f"Number of chunks: {len(chunks)}")

for i, chunk in enumerate(chunks, start=1):
    print(f"\n--- Chunk {i} ---")
    print(chunk)