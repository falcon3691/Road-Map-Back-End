document.addEventListener("DOMContentLoaded", async function () {
    // URL'den 'id' parametresini al
    const urlParams = new URLSearchParams(window.location.search);
    const articleId = urlParams.get("id");

    if (!articleId) {
        document.body.innerHTML = "<h1>Error: Missing article data</h1>";
        return;
    }

    try {
        // JSON verisini çek
        const response = await fetch("../blogs/articles.json");
        const data = await response.json();

        // articles dizisini kontrol et
        if (!data.articles) {
            throw new Error("Invalid articles.json format");
        }

        // ID'ye göre makaleyi bul
        const article = data.articles.find(a => a.id === articleId);

        if (!article) {
            document.body.innerHTML = "<h1>Error: Article not found</h1>";
            return;
        }

        // Blog sayfasına veriyi aktar
        document.querySelector(".blog-post h2").textContent = article.title;
        document.querySelector(".date span").textContent = article.createdAt;
        document.querySelector(".blog-content").textContent = article.content;
    } catch (error) {
        console.error("Error fetching article:", error);
        document.body.innerHTML = `<h1>Error loading article</h1>`;
    }
});
