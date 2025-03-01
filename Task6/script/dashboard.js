document.addEventListener("DOMContentLoaded", function () {
    const articlesList = document.getElementById("articles-list");
    const API_URL = "http://localhost:3000/articles";

    function loadArticles() {
        fetch(API_URL)
            .then(response => response.json())
            .then(data => {
                articlesList.innerHTML = "";
                data.forEach(article => {
                    const listItem = document.createElement("li");
                    listItem.innerHTML = `
                        <strong>${article.title}</strong> - ${article.createdAt}
                        <button onclick="window.location.href='edit.html?id=${article.id}'">Düzenle</button>
                        <button onclick="deleteArticle('${article.id}')">Sil</button>
                    `;
                    articlesList.appendChild(listItem);
                });
            })
            .catch(error => console.error("Yazılar yüklenirken hata oluştu:", error));
    }

    window.deleteArticle = function (id) {
        if (confirm("Bu yazıyı silmek istediğinizden emin misiniz?")) {
            fetch(`${API_URL}/${id}`, { method: "DELETE" })
                .then(() => loadArticles())
                .catch(error => console.error("Yazı silinirken hata:", error));
        }
    };

    loadArticles();
});
