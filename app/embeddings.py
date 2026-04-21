from sentence_transformers import SentenceTransformer

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_embeddings(chunks):
    embeddings = model.encode(chunks)
    return embeddings


if __name__ == "__main__":
    from chunking import chunk_text
    from loader import load_document

    # Load and chunk data
    data = load_document("data/finance_sample.txt")
    chunks = chunk_text(data)

    # Generate embeddings
    embeddings = generate_embeddings(chunks)

    print("Embeddings Shape:", embeddings.shape)
    print("\nSample Embedding:\n", embeddings[0])

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}: {chunk}")
    print(f"Embedding: {embeddings[i][:5]}...")