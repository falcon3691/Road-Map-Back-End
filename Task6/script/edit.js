document.addEventListener("DOMContentLoaded", function () {
    const urlParams = new URLSearchParams(window.location.search);
    const id = urlParams.get("id");

    if (!id) {
        document.body.innerHTML = "<h1>Hata: Yazı bulunamadı</h1>";
        return;
    }

    fetch(`http://localhost:3000/articles/${id}`)
        .then(response => response.json())
        .then(article => {
            document.getElementById("title").value = article.title;
            document.getElementById("createdAt").value = article.createdAt;
            document.getElementById("content").value = article.content;
        })
        .catch(error => console.error("Error fetching article:", error));

    document.getElementById("edit-form").addEventListener("submit", function (event) {
        event.preventDefault();

        const updatedArticle = {
            title: document.getElementById("title").value,
            createdAt: document.getElementById("createdAt").value,
            content: document.getElementById("content").value
        };

        fetch(`http://localhost:3000/articles/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(updatedArticle)
        })
        .then(() => window.location.href = "dashboard.html")
        .catch(error => console.error("Error updating article:", error));
    });
});
