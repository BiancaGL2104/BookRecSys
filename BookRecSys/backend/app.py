from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_cors import CORS
from backend.recommendations import get_saved_books

app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")
CORS(app)

user_ratings = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/lda')
def lda_page():
    return render_template('lda.html')

@app.route('/bert')
def bert_page():
    return render_template('bert.html')

@app.route('/save_ratings', methods=['POST'])
def save_ratings():
    global user_ratings
    data = request.json
    user_ratings = data.get("preferences", {})
    return jsonify({"message": "Ratings saved successfully!"})

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    feedback = request.form
    print("Feedback received:", feedback)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
