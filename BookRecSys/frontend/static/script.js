document.addEventListener("DOMContentLoaded", () => {
    const bodyClass = document.body.className;

    if (bodyClass.includes("lda-page")) {
        populateBooks("lda");
        document
            .getElementById("get-recommendations")
            .addEventListener("click", () => getRecommendations("lda"));
    } else if (bodyClass.includes("bert-page")) {
        populateBooks("bert");
        document
            .getElementById("get-recommendations")
            .addEventListener("click", () => getRecommendations("bert"));
    }
});

function populateBooks(engine) {
    fetch(`/backend/get_books/${engine}`)
        .then((response) => {
            if (!response.ok) {
                throw new Error("Failed to fetch books");
            }
            return response.json();
        })
        .then((books) => {
            const bookRatingsDiv = document.getElementById("book-ratings");
            bookRatingsDiv.innerHTML = ""; // Clear previous content

            books.forEach((book) => {
                const bookDiv = document.createElement("div");
                bookDiv.className = "book";
                bookDiv.innerHTML = `
                    <img src="${book.image}" alt="${book.title || "Untitled"}" />
                    <p><strong>${book.title}</strong> by ${book.author}</p>
                    <a href="#" class="summary-link">Read Summary</a>
                    <div class="star-rating" data-id="${book.title}">
                        ${[...Array(5)]
                            .map((_, i) => `<span class="star" data-value="${i + 1}">&#9733;</span>`)
                            .join("")}
                    </div>
                `;
                bookRatingsDiv.appendChild(bookDiv);
            });

            addStarRatingListeners();
        })
        .catch((error) => console.error("Error fetching books:", error));
}

function getRecommendations(engine) {
    const preferences = {};

    // Collect user ratings
    document.querySelectorAll(".star-rating").forEach((rating) => {
        const bookId = rating.dataset.id; // Get book ID
        const userRating = rating.dataset.rating || 0; // Get rating value
        if (userRating > 0) {
            preferences[bookId] = parseInt(userRating, 10);
        }
    });

    if (Object.keys(preferences).length === 0) {
        alert("Please rate at least one book before getting recommendations.");
        return;
    }

    console.log("Sending preferences to backend:", preferences); // Debug log

    // Send preferences to the backend
    fetch(`/backend/recommendations/${engine}`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ preferences }), // Ensure proper format
    })
        .then((response) => {
            if (!response.ok) {
                throw new Error("Failed to fetch recommendations");
            }
            return response.json();
        })
        .then((data) => {
            displayRecommendations(data.recommendations);
        })
        .catch((error) => console.error("Error fetching recommendations:", error));
}


function addStarRatingListeners() {
    document.querySelectorAll(".star-rating").forEach((rating) => {
        const stars = Array.from(rating.querySelectorAll(".star"));

        stars.forEach((star, index) => {
            star.addEventListener("mouseover", () => {
                stars.forEach((s, i) => s.classList.toggle("selected", i <= index));
            });

            rating.addEventListener("mouseleave", () => {
                stars.forEach((s) => s.classList.remove("selected"));
                const value = rating.dataset.rating || 0;
                stars.forEach((s, i) => i < value && s.classList.add("selected"));
            });

            star.addEventListener("click", () => {
                const ratingValue = index + 1;
                rating.dataset.rating = ratingValue;
                console.log(`Rating for ${rating.dataset.id}: ${ratingValue}`); // Log rating updates
                stars.forEach((s, i) => s.classList.toggle("selected", i < ratingValue));
            });
        });
    });
}


function displayRecommendations(recommendations) {
    console.log("Recommendations received:", recommendations); // Debug log

    const recommendationsSection = document.getElementById("recommendations");
    const recommendationsList = document.getElementById("recommendations-list");

    recommendationsList.innerHTML = ""; // Clear previous recommendations

    books.forEach((book) => {
        const bookItem = document.createElement("div");
        bookItem.className = "book";
        bookItem.innerHTML = `
            <img src="${book.image}" alt="${book.title || "Untitled"}" />
            <p><strong>${book.title}</strong> by ${book.author}</p>
        `;

        recommendationsList.appendChild(bookItem);
    });

    recommendationsSection.style.display = "block"; // Show recommendations section
}
