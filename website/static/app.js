document.addEventListener("DOMContentLoaded", function() {
    const sidebar = document.getElementById("sidebar");
    const hamburgerMenu = document.getElementById("hamburger-menu");

    hamburgerMenu.addEventListener("click", function() {
        sidebar.classList.toggle("visible");
    });
});
