document.addEventListener("DOMContentLoaded", function() {
    const closeButtons = document.querySelectorAll('.closebtn');

    closeButtons.forEach(button => {
        button.addEventListener('click', function() {
            const message = this.parentElement;
            message.style.opacity = '0';
            setTimeout(() => { message.style.display = 'none'; }, 600);
        });
    });
});
