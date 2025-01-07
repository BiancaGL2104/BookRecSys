import sys
import numpy as np
import pandas as pd

class LDAEngine:
    def __init__(self):
        self.books_df = pd.read_csv("resources/datasets/book_summaries_cleaned.csv")
        self.cos_mat = np.load("Models/similarity_matrix.npy")

    def unpack_prefs(self, preferences):
        book_list, weights = zip(*preferences.items())
        weights = [(w - min(weights)) / (max(weights) - min(weights) + sys.float_info.epsilon) for w in weights]
        return list(book_list), weights

    def retrieval(self, preferences, n=3):
        book_list, weights = self.unpack_prefs(preferences)
        score_list = np.sum(
            np.multiply(weights, [self.cos_mat[self.bookid2index(book)] for book in book_list]), axis=0
        ) / len(book_list)
        return [self.books_df.iloc[i]['Title'] for i in score_list.argsort()[-n:][::-1]]
