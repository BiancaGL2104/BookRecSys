import pandas as pd
import json

# Load the book dataset
books = pd.read_csv("resources/datasets/book_summaries_cleaned.csv")

def generate_and_save_books(books):
    try:

        required_columns = ['ID', 'MID', 'Title', 'Author', 'Date', 'Genres', 'Summary']
        for col in required_columns:
            if col not in books.columns:
                raise KeyError(f"Missing column '{col}'")

        book_list = []
        for _, row in books.iterrows():
            book = {
                "id": str(row["ID"]),
                "mid": str(row["MID"]),
                "title": str(row["Title"]),
                "author": str(row["Author"]),
                "date": str(row["Date"]),
                "genres": str(row["Genres"]),
                "summary": str(row["Summary"]),
            }
            book_list.append(book)

        with open("resources/actual_books.json", "w", encoding="utf-8") as json_file:
            json.dump(book_list, json_file, indent=4, ensure_ascii=False)

        print(f"{len(book_list)} books saved to resources/actual_books.json.")

        save_lda_and_bert_books()
    except KeyError as e:
        print(f"KeyError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def save_lda_and_bert_books():
    try:
        with open("resources/actual_books.json", "r", encoding="utf-8") as f:
            books = json.load(f)

        # Check if there are enough books
        if len(books) < 6:
            raise ValueError("Not enough books in the dataset to extract LDA and BERT books.")

        lda_books = books[:3]
        bert_books = books[3:6]

        # Save LDA books
        with open("resources/lda_books.json", "w", encoding="utf-8") as f:
            json.dump(lda_books, f, indent=4, ensure_ascii=False)
        print("Saved LDA books to resources/lda_books.json")

        # Save BERT books
        with open("resources/bert_books.json", "w", encoding="utf-8") as f:
            json.dump(bert_books, f, indent=4, ensure_ascii=False)
        print("Saved BERT books to resources/bert_books.json")

    except Exception as e:
        print(f"Error saving LDA and BERT books: {e}")

def get_saved_books(engine):
    """Load books from the specified file for the given engine."""
    if engine == "lda":
        file_path = "resources/lda_books.json"
    elif engine == "bert":
        file_path = "resources/bert_books.json"
    else:
        print("Invalid engine type specified. Must be 'lda' or 'bert'.")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            books = json.load(f)
        return books
    except FileNotFoundError:
        print(f"File not found: {file_path}. Ensure the books have been saved.")
        return []
    except json.JSONDecodeError:
        print(f"Error decoding JSON in file: {file_path}")
        return []

from backend.lda_engine import LDAEngine
from backend.bert_engine import BertEngine

lda_engine = LDAEngine()
bert_engine = BertEngine()

def get_recommendations(user_ratings, engine="lda"):
    """Get recommendations using the specified engine."""
    if engine == "lda":
        return lda_engine.retrieval(user_ratings, n=10)
    elif engine == "bert":
        return bert_engine.retrieval(user_ratings, n=10)
    else:
        raise ValueError("Invalid engine type. Choose 'lda' or 'bert'.")

if __name__ == "__main__":
    generate_and_save_books(books)
