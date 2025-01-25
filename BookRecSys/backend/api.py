from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import pandas as pd
import os
from backend.lda_engine import LDAEngine
from backend.bert_engine import BertEngine

app = Flask(__name__, static_folder='../frontend/static')
CORS(app)

# Load the dataset
DATASET_PATH = "resources/datasets/popularbooks.csv"
if not os.path.exists(DATASET_PATH):
    raise FileNotFoundError(f"Dataset not found at {DATASET_PATH}")
books = pd.read_csv(DATASET_PATH)

def get_saved_books():
    """Fetch a sample of books."""
    return books.sample(5).to_dict(orient="records")

@app.route("/")
def serve_frontend():
    """Serve the frontend."""
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:path>")
def serve_static_files(path):
    """Serve static files for the frontend."""
    return send_from_directory(app.static_folder, path)

@app.route('/backend/get_books/<engine>', methods=['GET'])
def get_books_api(engine):
    """Fetch books for the given engine."""
    try:
        if engine == "lda":
            saved_books = LDAEngine().books.sample(5).to_dict(orient="records")
        elif engine == "bert":
            saved_books = BertEngine().books.sample(5).to_dict(orient="records")
        else:
            return jsonify({"error": f"Unknown engine: {engine}"}), 400

        # Directly use the dataset values without placeholders
        response = [
            {
                "title": book["Title"],
                "author": book["Author"],
                "description": book["Description"],
                "image": book["Image"],
            }
            for book in saved_books
        ]
        return jsonify(response)
    except Exception as e:
        app.logger.error(f"Error fetching books: {e}")
        return jsonify({"error": "Internal server error"}), 500


@app.route("/backend/get_books", methods=["GET"])
def get_books():
    """Fetch saved books."""
    try:
        saved_books = get_saved_books()
        return jsonify(saved_books)
    except Exception as e:
        app.logger.error(f"Error fetching books: {e}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    app.run(debug=True)
