document.addEventListener("DOMContentLoaded", function () {
    const body = document.body;
    const toggleCheckbox = document.getElementById("dark-mode-toggle");
    const toggleIcon = document.getElementById("toggle-icon");

    // Check localStorage for dark mode setting
    if (localStorage.getItem("darkMode") === "enabled") {
        body.classList.add("dark-mode");
        toggleCheckbox.checked = true;
        toggleIcon.classList.replace("bi-moon-fill", "bi-sun-fill"); // Change to sun
    }

    // Toggle dark mode on button click
    toggleCheckbox.addEventListener("change", function () {
        if (toggleCheckbox.checked) {
            body.classList.add("dark-mode");
            localStorage.setItem("darkMode", "enabled");
            toggleIcon.classList.replace("bi-moon-fill", "bi-sun-fill"); // Moon -> Sun
        } else {
            body.classList.remove("dark-mode");
            localStorage.setItem("darkMode", "disabled");
            toggleIcon.classList.replace("bi-sun-fill", "bi-moon-fill"); // Sun -> Moon
        }
    });
});
