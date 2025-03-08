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

    fetch("../blogs/articles.json")
    .then(response => response.json())
    .then(value => {
        if (value.articles && Array.isArray(value.articles)) {
            const foundArticle = value.articles.find(article => article.id === articleId);
            
            if (foundArticle) {
                pageTitle.textContent = "Yazıyı Düzenle";
                titleInput.value = foundArticle.title;
                dateInput.value = foundArticle.createdAt;
                contentInput.value = foundArticle.content;
                articleIdInput.value = foundArticle.id;
            }
        } else {
            console.log("Beklenen JSON formatı farklı olabilir.");
        }
    })
    .catch(error => console.error("Hata:", error));


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
