from app.chunking.character import character_chunking


text = """
Machine learning is a field of artificial intelligence.
It allows computers to learn patterns from data.
Deep learning uses neural networks with multiple layers.
Natural language processing deals with human language.
"""


chunks = character_chunking(
    text,
    chunk_size=100,
    overlap=20
)


print(f"Number of chunks: {len(chunks)}")

for i, chunk in enumerate(chunks, start=1):
    print(f"\n--- Chunk {i} ---")
    print(chunk)