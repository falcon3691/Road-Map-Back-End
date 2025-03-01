document.addEventListener("DOMContentLoaded", function () {
    const nav = document.createElement("nav");
    nav.innerHTML = `
        <ul>
            <li><a href="index.html">Ana Sayfa</a></li>
            <li><a href="dashboard.html">Admin Paneli</a></li>
        </ul>
    `;
    document.body.insertAdjacentElement("afterbegin", nav);
});
