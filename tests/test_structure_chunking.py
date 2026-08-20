from app.chunking.structure import structure_chunking


text = """
INTRODUCTION

Machine learning is a field of artificial intelligence.
It allows computers to learn patterns from data.

METHODOLOGY

The model was trained using a dataset containing thousands of examples.
The data was divided into training and testing sets.

RESULTS

The model achieved strong performance on the test dataset.
"""


chunks = structure_chunking(
    text,
    max_chunk_size=200
)


print(f"Number of chunks: {len(chunks)}")

for i, chunk in enumerate(chunks, start=1):
    print(f"\n--- Chunk {i} ---")
    print(chunk)