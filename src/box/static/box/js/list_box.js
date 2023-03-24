document.addEventListener('DOMContentLoaded', function () {
    var sortMenuButton = document.querySelector('#sortMenu');
    var dropdownMenu = document.querySelector('.dropdown-menu');
    var dropdownMenuItems = document.querySelectorAll('.dropdown-item');

    function hideDropdown() {
        dropdownMenu.classList.remove('show');
    }

    function showDropdown() {
        dropdownMenu.classList.add('show');
    }

    function toggleDropdown() {
        dropdownMenu.classList.contains('show') ? hideDropdown() : showDropdown();
    }

    sortMenuButton.addEventListener('click', function (event) {
        event.stopPropagation();
        toggleDropdown();
    });

    dropdownMenuItems.forEach(function (item) {
        item.addEventListener('click', function (event) {
            event.stopPropagation();
            hideDropdown();
        });
    });

    document.body.addEventListener('click', function () {
        hideDropdown();
    });
});