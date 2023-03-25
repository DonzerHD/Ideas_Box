// Wait for the page to load before executing the code
document.addEventListener('DOMContentLoaded', function () {

    // Get the button that toggles the dropdown menu
    var sortMenuButton = document.querySelector('#sortMenu');

    // Get the dropdown menu itself
    var dropdownMenu = document.querySelector('.dropdown-menu');

    // Get all the dropdown items
    var dropdownMenuItems = document.querySelectorAll('.dropdown-item');

    // Function to hide the dropdown menu
    function hideDropdown() {
        dropdownMenu.classList.remove('show');
    }

    // Function to show the dropdown menu
    function showDropdown() {
        dropdownMenu.classList.add('show');
    }

    // Function to toggle the dropdown menu visibility
    function toggleDropdown() {
        dropdownMenu.classList.contains('show') ? hideDropdown() : showDropdown();
    }

    // Add an event listener to the button that toggles the dropdown menu
    sortMenuButton.addEventListener('click', function (event) {
        event.stopPropagation();
        toggleDropdown();
    });

    // Add an event listener to each dropdown item to hide the dropdown menu when an item is clicked
    dropdownMenuItems.forEach(function (item) {
        item.addEventListener('click', function (event) {
            event.stopPropagation();
            hideDropdown();
        });
    });

    // Add an event listener to the document body to hide the dropdown menu when the user clicks outside of it
    document.body.addEventListener('click', function () {
        hideDropdown();
    });
});