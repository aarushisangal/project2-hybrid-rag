from app.embeddings.embedder import Embedder


embedder = Embedder()

texts = [
    "Machine learning is a branch of artificial intelligence.",
    "Artificial intelligence systems can learn from data.",
    "The weather is sunny today."
]

embeddings = embedder.encode(texts)

print("Number of embeddings:", len(embeddings))
print("Embedding dimension:", len(embeddings[0]))

for i, embedding in enumerate(embeddings):
    print(f"Text {i + 1}: vector length = {len(embedding)}")