document.getElementById("add-form").addEventListener("submit", function (event) {
    event.preventDefault();

    const newArticle = {
        title: document.getElementById("title").value,
        createdAt: document.getElementById("createdAt").value,
        content: document.getElementById("content").value
    };

    fetch("http://localhost:3000/articles", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(newArticle)
    })
    .then(() => window.location.href = "dashboard.html")
    .catch(error => console.error("Error adding article:", error));
});
