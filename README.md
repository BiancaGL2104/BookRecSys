# BookRecSys
A web-based application that allows users to rate books and receive personalized recommendations based on their ratings.

---

## Features
* **Random Book Sampling**: Displays a random selection of books from a preprocessed dataset to allow users to rate and explore.
* **LDA Topic Modelling**: Uses Latent Dirichlet Allocation to discover topics from book summaries and classify books based on user preferences.
* **BERT Embedding**: Implements BERT to compute semantic similarity between book summaries for enhanced recommendation accuracy.
* **User Interaction**: Allows users to input their preferences through ratings and feedback on displayed books.
* **Personalized Recommendations**: Suggests books based on cosine similarity computed from LDA topics and BERT embeddings.
* **Feedback Collection**: Integrated Google Forms for collecting user feedback on recommendations and system performance.

---

## Dataset
The dataset contains detailed metadata and textual summaries for books, including:
* **Book Title**: name of the book.
* **Author**: author of the book.
* **Description**: summary of the book.
* **Image**: a link to the image of the cover of the book.

---

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

---

## Installation and Setup
### Clone the Repository

### Download the Pre-trained Models 

### Install Dependencies

### Set Up Environment Variables

### Run the Application 

---

## Project Structure
```
BookRecSys/
│
├── backend/
│   ├── app.py                    # Main Flask app
│   ├── api.py                    # API endpoints
│   ├── recommendations.py        # Recommendation logic
|   ├── bert.py                   # API server for BERT system
|   ├── bert_engine.py            # BERT recommendation engine
│   ├── lda.py                    # API server for LDA system
│   ├── lda_engine.py             # LDA recommendation engine
│
├── frontend/
│   ├── static/
│   │   ├── images/               # Image files
│   │   └── style.css             # CSS style
|   |   └── script.js             # Frontend JavaScript
│   ├── templates/
│   │   └── index.html            # Landing page
|   |   └── lda.html              # LDA rating page
|   |   └── bert.html             # BERT rating page 
│
├── resources/
|   │   ├── dataset/
|   |   |   └── popularbooks.csv   # Books dataset
├── requirements.txt               # Python dependencies
└── README.md         
```

---

## User Instructions
1. **Choose recommendation engine**: When landing the app, you will see two buttons with the two recommendation systems. Choose which one you want to begin with.
2. **Rate Books**: On the rating page of the chosen system, you will see a random selection of books. Rate each book out of 5 star based on your interest.
3. **Get Recommendations**: Submit your ratings by pressing the get recommendations button to receive personalized book recommendations.
4. **Provide Feedback**: Share the experience using the Google Form.

---

## How It Works
### Dataset:
* A preprocessed dataset with books' metadata and summaries.
* Randomly select books for user interaction.

### LDA Topic Modelling:
* Extracts latent topics from book summaries.
* Classifies books based on their thematic content.

### BERT Embedding:
* Converts book summaries into semantic vectors.
* Measures similarity between user preferences and book preferences and book embeddings.

### Recommendation Logic:
* Uses cosine similarity to suggest the best-matching books for each system.

---

## Future Enhancements
* Add user authentication to save preferences and track reading history.
* Expand dataset with more genres and international books.
* Allow users to search and add their favorite books.
* Introduce advanced visualizations for topic modeling results.
* Combine LDA and BERT to improve personalization of book recommendations.
