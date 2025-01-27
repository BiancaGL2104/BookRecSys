# BookRecSys
A web-based application that allows users to rate books and receive personalized recommendations based on their ratings.

## Features
* **Random Book Sampling**: Displays a random selection of books from a preprocessed dataset to allow users to rate and explore.
* **LDA Topic Modelling**: Uses Latent Dirichlet Allocation to discover topics from book summaries and classify books based on user preferences.
* **BERT Embedding**: Implements BERT to compute semantic similarity between book summaries for enhanced recommendation accuracy.
* **User Interaction**: Allows users to input their preferences through ratings and feedback on displayed books.
* **Personalized Recommendations**: Suggests books based on cosine similarity computed from LDA topics and BERT embeddings.
* **Feedback Collection**: Integrated Google Forms for collecting user feedback on recommendations and system performance.

## Dataset
The dataset contains detailed metadata and textual summaries for books, including:
* **Book Title**: name of the book.
* **Author**: author of the book.
* **Description**: summary of the book.
* **Image**: a link to the image of the cover of the book.

## Technologies Used
### Frontend:
* **HTML5** and **CSS3**: For structuring and styling the web application.
* **JavaScript**: For dynamic user interactions.
### Backend:
* **Flask(Python)**: Serves the application and handles API requests.
* **Pandas**: For dataset preprocessing and manipulation.

### Recommendation Algorithms:
* **LDA Topic Modelling**: Extracts topics from book summaries.
* **{BERT Embeddings**: Computes semantic similarity between book summaries.
* **Cosine Similarity**: Measures similarity between user preferences and books.

### Additional Tools:
* **Google Forms**: Embedded for feedback collection.
* **Preprocessed Dataset**: Contains clean and structured book data for efficient processing.
