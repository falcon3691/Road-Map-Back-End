/*const articleList = document.getElementById("article-list");
articleList.innerHTML = ""; // Önce listeyi temizle
fetch("../blogs/articles.json")
    .then(response => response.json())
    .then(value => value.articles.forEach(article => {
        const articleElement = document.createElement("div");
        articleElement.classList.add("article-item"); // CSS için sınıf ekleyebilirsin

        // Blog başlığı ve tarihi içeren HTML bloğu
        articleElement.innerHTML = `
            <a href="blog.html?id=${article.id}">
                <h3>${article.title}</h3>
            </a>
            <p><small>${article.createdAt}</small></p>
            <a href="edit.html?id=${article.id}">EDIT</a>
            <a href="blog.html?id=${article.id}">DELETE</a>
        `;
        articleList.appendChild(articleElement);
    }));*/

import { writeFileSync } from 'fs';

// Read the JSON file
import jsonDataBefore from './data.json';

// Print JSON data before updating
console.log('Before updating JSON:');
console.log(JSON.stringify(jsonDataBefore, null, 2));

// Update the data
jsonDataBefore[0].programmingLanguage.push("JavaScript");
jsonDataBefore[1].programmingLanguage.push("JavaScript");

// Write the updated data back to the JSON file
writeFileSync('./data.json', JSON.stringify(jsonDataBefore, null, 2));

// Print JSON data after updating
console.log('\nAfter updating JSON:');
console.log(JSON.stringify(jsonDataBefore));

console.log('\nData updated successfully.');