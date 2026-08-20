from app.chunking.pipeline import create_chunks


text = """
Machine learning is a branch of artificial intelligence.

Supervised learning uses labeled examples.

Classification is a common supervised learning task.

Relational databases organize information into tables.

Database indexing improves query performance.
"""


for method in ["character", "structure", "semantic"]:

    print("\n" + "=" * 60)
    print(f"CHUNKING METHOD: {method}")
    print("=" * 60)

    chunks = create_chunks(
        text,
        source="test_document.txt",
        method=method
    )

    print(f"Number of chunks: {len(chunks)}")

    for chunk in chunks:

        print(f"\nChunk ID: {chunk.chunk_id}")
        print(f"Source: {chunk.source}")
        print(f"Method: {chunk.chunking_method}")
        print(f"Text: {chunk.text}")