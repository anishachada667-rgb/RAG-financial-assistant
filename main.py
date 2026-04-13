from src.ingestion.data_loader import load_data

if __name__ == "__main__":
    data = load_data("data/sample_queries.csv")
    print(data.head())