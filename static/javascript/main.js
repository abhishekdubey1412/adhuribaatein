let toggle = document.querySelector('.toggle');
let Navbar = document.querySelector('.navbar');
let NavbarMenu = document.querySelector('.menu');
let hiddenToggleDiv = document.querySelector('#hidden_toggle')

let isMenuVisible = false; // Track the visibility state of the menu

toggle.addEventListener('click', () => {
    if (!isMenuVisible) {
        // Show the menu
        Navbar.classList.add('active_nav');
        toggle.classList.add('active_toggle');
        hiddenToggleDiv.style.display = 'none';
        NavbarMenu.style.display = 'block';
    } else {
        // Hide the menu
        Navbar.classList.remove('active_nav');
        toggle.classList.remove('active_toggle');
        hiddenToggleDiv.style.display = 'block';
        NavbarMenu.style.display = 'none';
    }

    // Toggle the visibility state
    isMenuVisible = !isMenuVisible;
});
