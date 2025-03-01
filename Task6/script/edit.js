document.addEventListener("DOMContentLoaded", function () {
    const API_URL = "http://localhost:3000/articles";
    const urlParams = new URLSearchParams(window.location.search);
    const articleId = urlParams.get("id");

    const titleInput = document.getElementById("title");
    const dateInput = document.getElementById("createdAt");
    const contentInput = document.getElementById("content");
    const articleIdInput = document.getElementById("article-id");
    const blogForm = document.getElementById("blog-form");
    const pageTitle = document.getElementById("page-title");

    if (articleId) {
        // Sayfa "Düzenleme" için açıldıysa
        pageTitle.textContent = "Yazıyı Düzenle";
        fetch(`${API_URL}/${articleId}`)
            .then(response => response.json())
            .then(article => {
                titleInput.value = article.title;
                dateInput.value = article.createdAt;
                contentInput.value = article.content;
                articleIdInput.value = article.id;
            })
            .catch(error => console.error("Yazı yüklenirken hata:", error));
    }

    blogForm.addEventListener("submit", function (event) {
        event.preventDefault();

        const newArticle = {
            title: titleInput.value,
            createdAt: dateInput.value,
            content: contentInput.value
        };

        const method = articleId ? "PATCH" : "POST";
        const url = articleId ? `${API_URL}/${articleId}` : API_URL;

        fetch(url, {
            method: method,
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(newArticle)
        })
            .then(() => {
                window.location.href = "dashboard.html"; // Yönetim paneline geri dön
            })
            .catch(error => console.error("Yazı kaydedilirken hata:", error));
    });
});
