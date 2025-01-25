import pandas as pd
import numpy as np

class LDAEngine:
    def __init__(self):
        """Initialize LDA engine."""
        self.books = pd.read_csv('resources/datasets/popularbooks.csv')
        self.similarity_matrix = np.load("Models/similarity_matrix-2.npy")
        # Normalize dataset titles
        self.books['Title'] = self.books['Title'].str.strip().str.lower()


    def retrieval(self, preferences, n=5):
        """Get recommendations."""
        indices = [self.books[self.books['Title'] == title].index[0] for title in preferences.keys()]
        weights = np.array(list(preferences.values())).reshape(-1, 1)
        scores = np.mean(np.multiply(self.similarity_matrix[indices], weights), axis=0)
        top_indices = np.argsort(-scores)[:n]
        
        recommendations = self.books.iloc[top_indices].copy()
        recommendations['Title'] = recommendations['Title'].fillna("Untitled")
        recommendations['Author'] = recommendations['Author'].fillna("Unknown Author")
        recommendations['Description'] = recommendations['Description'].fillna("No description available.")
        recommendations['Image'] = recommendations['Image'].apply(
            lambda x: x if pd.notnull(x) and str(x).startswith("http") else "/static/images/default-book.jpg"
        )
        
        return recommendations.to_dict(orient="records")
