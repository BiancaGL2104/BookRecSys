document.addEventListener("DOMContentLoaded", () => {
    const bodyClass = document.body.className;

    if (bodyClass.includes("lda-page")) {
        populateBooks("lda");
    } else if (bodyClass.includes("bert-page")) {
        populateBooks("bert");
    }
});

function populateBooks(engine) {
    fetch(`/backend/get_books?engine=${engine}`)
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
                    <img src="${book.image || "/static/images/default-book.jpg"}" alt="${book.title}" />
                    <p><strong>${book.title}</strong> by ${book.author}</p>
                    <a href="${book.summary_link}" target="_blank" class="summary-link">Read Summary</a>
                    <div class="star-rating" data-id="${book.id}">
                        ${[...Array(5)]
                            .map(
                                (_, i) =>
                                    `<span class="star" data-value="${i + 1}">&#9733;</span>`
                            )
                            .join("")}
                    </div>
                `;
                bookRatingsDiv.appendChild(bookDiv);
            });
            addStarRatingListeners();
        })
        .catch((error) => console.error("Error fetching books:", error));
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
                stars.forEach((s, i) => s.classList.toggle("selected", i < ratingValue));
            });
        });
    });
}
