def load_document(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


if __name__ == "__main__":
    data = load_document("data/finance_sample.txt")
    print("Loaded Document:\n")
    print(data)