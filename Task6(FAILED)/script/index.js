document.addEventListener("DOMContentLoaded", async function () {
    try {
        // JSON verisini çek
        const response = await fetch("../blogs/articles.json");
        const data = await response.json();

        // articles dizisini kontrol et
        if (!data.articles) {
            throw new Error("Invalid articles.json format");
        }

        const articleList = document.getElementById("article-list");
        articleList.innerHTML = ""; // Önce listeyi temizle

        // Blog yazılarını ekrana ekle
        data.articles.forEach(article => {
            const articleElement = document.createElement("div");
            articleElement.classList.add("article-item"); // CSS için sınıf ekleyebilirsin

            // Blog başlığı ve tarihi içeren HTML bloğu
            articleElement.innerHTML = `
                <a href="blog.html?id=${article.id}">
                    <h3>${article.title}</h3>
                </a>
                <p><small>${article.createdAt}</small></p>
            `;

            articleList.appendChild(articleElement);
        });

    } catch (error) {
        console.error("Error fetching articles:", error);
        document.getElementById("article-list").innerHTML = "<p>Error loading articles.</p>";
    }
});
