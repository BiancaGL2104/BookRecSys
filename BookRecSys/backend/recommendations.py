import pandas as pd
import json

# Load the book dataset
books = pd.read_csv("resources/datasets/popularbooks.csv")

def generate_and_save_books(books):
    try:
        # Verify the dataset structure
        print("Columns in the dataset:", books.columns)

        # Ensure the required columns exist
        required_columns = ['Title', 'Author', 'Published', 'Genres', 'Description', 'Image']
        for col in required_columns:
            if col not in books.columns:
                raise KeyError(f"Missing column '{col}'")

        # Process the dataset
        book_list = []
        for _, row in books.iterrows():
            book = {
                "title": str(row["Title"]),
                "author": str(row["Author"]),
                "published": str(row["Published"]),
                "genres": str(row["Genres"]),
                "description": str(row["Description"]),
                "image": str(row["Image"]),
            }
            book_list.append(book)

        # Save to JSON
        with open("resources/actual_books.json", "w", encoding="utf-8") as json_file:
            json.dump(book_list, json_file, indent=4, ensure_ascii=False)

        print(f"{len(book_list)} books saved to resources/actual_books.json.")
    except KeyError as e:
        print(f"KeyError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_saved_books(file_path="resources/actual_books.json"):
    """Load saved books from the JSON file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File not found: {file_path}. Please run generate_and_save_books first.")
        return []

# Example recommendation functions
from backend.lda_engine import LDAEngine
from backend.bert_engine import BertEngine

# Initialize recommendation engines
lda_engine = LDAEngine()
bert_engine = BertEngine()

def get_recommendations(user_ratings, engine):
    """Get recommendations using the specified engine."""
    try:
        if engine == "lda":
            return lda_engine.retrieval(user_ratings, n=10)
        elif engine == "bert":
            return bert_engine.retrieval(user_ratings, n=10)
        else:
            raise ValueError("Invalid engine type. Choose 'lda' or 'bert'.")
    except ValueError as e:
        print(e)
        return []

# Script to generate the books if needed
if __name__ == "__main__":
    generate_and_save_books(books)
