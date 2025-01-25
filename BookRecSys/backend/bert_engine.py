import pandas as pd
import numpy as np
import pickle
import torch
from torchmetrics.functional import pairwise_cosine_similarity
from bertopic import BERTopic

class BertEngine:
    def __init__(self):
        """Initialize the BERT engine."""
        self.books = pd.read_csv('resources/datasets/popularbooks.csv')
        self.topic_model = BERTopic.load("Models/bertopic_model")
        with open("Models/books_bert_features.pickle", "rb") as file:
            self.bert_features = pickle.load(file)

    def get_distances(self, selected_titles):
        """Calculate cosine distances."""
        selected = [
            self.bert_features[self.books[self.books['Title'] == title].index[0]]
            for title in selected_titles
            if title in self.books['Title'].values
        ]
        all_features = torch.tensor(np.array(self.bert_features))
        distances = pairwise_cosine_similarity(torch.tensor(selected), all_features)
        return distances.numpy()

    def retrieval(self, preferences, n=5):
        """Retrieve recommendations."""
        selected_titles = list(preferences.keys())
        distances = self.get_distances(selected_titles)
        avg_distances = np.mean(distances, axis=0)
        top_indices = np.argsort(-avg_distances)[:n]
        recommendations = self.books.iloc[top_indices]
        return recommendations.to_dict(orient="records")
