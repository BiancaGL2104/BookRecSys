#!/usr/bin/env python3
# coding: utf-8

"""
API server for the BERT-based RecSys engine.
"""

from flask import Flask, request, jsonify
from waitress import serve
from bert_engine import BertEngine


app = Flask(__name__)
eng = BertEngine()

@app.route("/retrieval", methods=["POST"])
def retrieval():
    """
    preferences = {"000-03W3-0000": 5, "000-02UP-0000": 5, "000-03IY-0000": 5, "000-0344-0000": 5, "000-02XU-0000": 5,
                   "000-01DN-0000": 5, "000-04PW-0000": 5, "000-017I-0000": 5, "000-04S4-0000": 5}
    """
    preferences = request.json

    recommendations = eng.retrieval(preferences, n=9)
    return jsonify(recommendations)


# Use a production server instead of Flask's built-in one.
# app.run(debug=False, port=10502)
serve(app, port=10502, threads=10)