import pandas as pd
import pickle
import numpy as np
import torch
from torchmetrics.functional import pairwise_cosine_similarity
from bertopic import BERTopic

class BertEngine:
    def __init__(self):
        self.books = pd.read_csv('resources/datasets/book_summaries_cleaned.csv')
        self.topic_model = BERTopic.load("Models/bertopic_model")
        with open("Models/books_bert_features.pickle", "rb") as file:
            self.bert_features = pickle.load(file)

    def retrieval(self, preferences, n=5):
        selected_indices = [self.books.index[self.books['ID'] == book_id][0] for book_id in preferences.keys()]
        distances = pairwise_cosine_similarity(
            torch.tensor([self.bert_features[i] for i in selected_indices]),
            torch.tensor(self.bert_features)
        ).numpy()
        weighted_scores = np.dot(preferences.values(), distances)
        return [self.books.iloc[i]['Title'] for i in weighted_scores.argsort()[-n:][::-1]]
