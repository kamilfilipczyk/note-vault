document.addEventListener("DOMContentLoaded", function() {
    const sidebar = document.getElementById("sidebar");
    const hamburgerMenu = document.getElementById("hamburger-menu");
    const homeLink = document.getElementById("home-link");

    hamburgerMenu.addEventListener("click", function() {
        sidebar.classList.toggle("collapsed");
        document.querySelector(".content").classList.toggle("shifted");
        document.querySelector(".topbar").classList.toggle("shifted");
    });

    homeLink.addEventListener("click", function() {
        window.location.href = "/";
    });
});

function openAddNoteModal() {
    document.getElementById("addNoteModal").style.display = "block";
}

function closeAddNoteModal() {
    document.getElementById("addNoteModal").style.display = "none";
}

function autoResizeTextarea(event) {
    const textarea = event.target;
    textarea.style.height = 'auto';
    textarea.style.height = (textarea.scrollHeight) + 'px';
}

document.addEventListener("DOMContentLoaded", function() {
    const textarea = document.getElementById("noteContent");
    textarea.addEventListener("input", autoResizeTextarea);
    textarea.style.height = 'auto';
    textarea.style.height = (textarea.scrollHeight) + 'px';
});
