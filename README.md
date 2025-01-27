# BookRecSys
A web-based application that allows users to rate books and receive personalized recommendations based on their ratings.

## Features
* \textbf{Random Book Sampling}: Displays a random selection of books from a preprocessed dataset to allow users to rate and explore.
* \textbf{LDA Topic Modelling}: Uses Latent Dirichlet Allocation to discover topics from book summaries and classify books based on user preferences.
* \textbf{BERT Embedding}: Implements BERT to compute semantic similarity between book summaries for enhanced recommendation accuracy.
* \texxtbf{User Interaction}: Allows users to input their preferences through ratings and feedback on displayed books.
* \textbf{Personalized Recommendations: Suggests books based on cosine similarity computed from LDA topics and BERT embeddings.
* \textbf{Feedback Collection}: Integrated Google Forms for collecting user feedback on recommendations and system performance.

## Dataset
The dataset contains detailed metadata and textual summaries for books, including:
* \textbf{Book Title}: name of the book.
* \textbf{Author}: author of the book.
* \textbf{Description}: summary of the book.
* \textbf{Image}: a link to the image of the cover of the book.

## Technologies Used
### Frontend:
* \textbf{HTML5} and \textbf{CSS3}: For structuring and styling the web application.
* \textbf{JavaScript}: For dynamic user interactions.
### Backend:
* \textbf{Flask(Python)}: Serves the application and handles API requests.
* \textbf{Pandas}: For dataset preprocessing and manipulation.

### Recommendation Algorithms:
* \textbf{LDA Topic Modelling}: Extracts topics from book summaries.
* \textbf{BERT Embeddings}: Computes semantic similarity between book summaries.
* \textbf{Cosine Similarity}: Measures similarity between user preferences and books.

### Additional Tools:
* \textbf{Google Forms}: Embedded for feedback collection.
* \textbf{Preprocessed Dataset}: Contains clean and structured book data for efficient processing.
