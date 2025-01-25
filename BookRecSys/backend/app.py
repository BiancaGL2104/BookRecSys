from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import pandas as pd
from backend.lda_engine import LDAEngine
from backend.bert_engine import BertEngine

app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")
CORS(app)

# Load dataset
DATASET_PATH = "resources/datasets/popularbooks.csv"
books = pd.read_csv(DATASET_PATH)

user_ratings = {}

@app.route('/')
def home():
    """Serve the home page."""
    return render_template('index.html')

@app.route('/lda')
def lda_page():
    """Serve the LDA recommender page."""
    return render_template('lda.html')

@app.route('/bert')
def bert_page():
    """Serve the BERT recommender page."""
    return render_template('bert.html')

lda_engine = LDAEngine()
bert_engine = BertEngine()

@app.route('/backend/recommendations/<engine>', methods=['POST'])
def get_recommendations_api(engine):
    """Generate recommendations."""
    global user_ratings
    data = request.json

    app.logger.info(f"Received request for engine '{engine}' with data: {data}")

    preferences = data.get("preferences", {})
    if not preferences:
        app.logger.error("Empty or invalid preferences received.")
        return jsonify({"error": "Invalid preferences"}), 400

    user_ratings = preferences

    try:
        if engine == "lda":
            recommendations = LDAEngine().retrieval(user_ratings, n=10)
        elif engine == "bert":
            recommendations = BertEngine().retrieval(user_ratings, n=10)
        else:
            app.logger.error(f"Invalid engine specified: {engine}")
            return jsonify({"error": "Invalid engine specified"}), 400

        app.logger.info(f"Generated recommendations: {recommendations}")
        return jsonify({"recommendations": recommendations})
    except Exception as e:
        app.logger.error(f"Error generating recommendations: {e}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/save_ratings', methods=['POST'])
def save_ratings():
    """Save user ratings."""
    global user_ratings
    user_ratings = request.json.get("preferences", {})
    return jsonify({"message": "Ratings saved successfully!"})

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

if __name__ == '__main__':
    app.run(debug=True)
