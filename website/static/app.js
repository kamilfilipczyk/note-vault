document.addEventListener("DOMContentLoaded", function() {
    const sidebar = document.getElementById("sidebar");
    const hamburgerMenu = document.getElementById("hamburger-menu");
    const homeLink = document.getElementById("home-link");

    hamburgerMenu.addEventListener("click", function() {
        sidebar.classList.toggle("collapsed");
        document.querySelector(".content").classList.toggle("shifted");
    });

    homeLink.addEventListener("click", function() {
        window.location.href = "/";
    });
});
