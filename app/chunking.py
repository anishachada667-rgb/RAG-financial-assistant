from loader import load_document


def chunk_text(text, chunk_size=100):
    chunks = []
    
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)
    
    return chunks


if __name__ == "__main__":
    # Load document
    data = load_document("data/finance_sample.txt")
    
    # Chunk the text
    chunks = chunk_text(data)
    
    print("Chunks:\n")
    
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i+1}:")
        print(chunk)
        print("-" * 40)