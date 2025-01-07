from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from .recommendations import LDAEngine, BertEngine

app = Flask(__name__)
CORS(app)  # Allow all origins, methods, and headers


@app.route("/backend/recommendations", methods=["POST"])
def recommendations():
    """Endpoint for generating recommendations based on user preferences."""
    data = request.get_json()
    engine = data.get("engine")
    preferences = data.get("preferences", {})

    try:
        if engine == "lda":
            lda_engine = LDAEngine()
            recommendations = lda_engine.retrieval(preferences, n=10)
        elif engine == "bert":
            bert_engine = BertEngine()
            recommendations = bert_engine.retrieval(preferences, n=10)
        else:
            return jsonify({"error": "Invalid engine type"}), 400

        return jsonify({"recommendations": recommendations})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/backend/get_books", methods=["GET"])
def get_books():
    engine = request.args.get("engine")
    if engine not in ["lda", "bert"]:
        return jsonify({"error": "Invalid engine specified"}), 400

    file_path = f"resources/{engine}_books.json"
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            books = json.load(f)
        return jsonify(books)
    except FileNotFoundError:
        return jsonify({"error": "Books file not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
