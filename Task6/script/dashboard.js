document.addEventListener("DOMContentLoaded", async function () {
    const blogList = document.getElementById("admin-blog-list");

    async function loadArticles() {
        try {
            const response = await fetch("../blogs/articles.json");
            const articles = await response.json();

            blogList.innerHTML = "";
            articles.forEach((article, index) => {
                const listItem = document.createElement("li");
                listItem.textContent = article.title;
                listItem.addEventListener("click", () => {
                    document.getElementById("article-id").value = index;
                    document.getElementById("title").value = article.title;
                    document.getElementById("content").value = article.content;
                });
                blogList.appendChild(listItem);
            });
        } catch (error) {
            console.error("Error loading articles:", error);
        }
    }

    async function saveArticles(updatedArticles) {
        try {
            await fetch("../blogs/articles.json", {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(updatedArticles)
            });
            loadArticles();
        } catch (error) {
            console.error("Error saving articles:", error);
        }
    }

    document.getElementById("add-btn").addEventListener("click", async function () {
        const newArticle = {
            title: document.getElementById("title").value,
            content: document.getElementById("content").value,
            createdAt: new Date().toISOString()
        };

        const response = await fetch("../blogs/articles.json");
        const articles = await response.json();
        articles.push(newArticle);
        saveArticles(articles);
    });

    document.getElementById("update-btn").addEventListener("click", async function () {
        const id = document.getElementById("article-id").value;
        if (id === "") return;

        const response = await fetch("../blogs/articles.json");
        const articles = await response.json();
        articles[id] = {
            title: document.getElementById("title").value,
            content: document.getElementById("content").value,
            createdAt: articles[id].createdAt
        };
        saveArticles(articles);
    });

    document.getElementById("delete-btn").addEventListener("click", async function () {
        const id = document.getElementById("article-id").value;
        if (id === "") return;

        const response = await fetch("../blogs/articles.json");
        const articles = await response.json();
        articles.splice(id, 1);
        saveArticles(articles);
    });

    loadArticles();
});
