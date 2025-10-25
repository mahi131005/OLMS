// Local Storage Logic for both .what-youll-learn and .key-projects
document.addEventListener('DOMContentLoaded', () => {
    // Checkboxes for .what-youll-learn
    const checkboxes = document.querySelectorAll('.what-youll-learn input[type="checkbox"]');
    const checkboxTexts = document.querySelectorAll('.what-youll-learn .checkbox-text');

    // Checkboxes for .key-projects
    const projectCheckboxes = document.querySelectorAll('.key-projects input[type="checkbox"]');
    const projectCheckboxTexts = document.querySelectorAll('.key-projects .checkbox-text');

    // Load saved state from local storage for .what-youll-learn
    checkboxes.forEach(checkbox => {
        const isChecked = localStorage.getItem(checkbox.id) === 'true';
        checkbox.checked = isChecked;
    });

    // Load saved state from local storage for .key-projects
    projectCheckboxes.forEach(checkbox => {
        const isChecked = localStorage.getItem(checkbox.id) === 'true';
        checkbox.checked = isChecked;
    });

    // Save state to local storage when checkbox is clicked for .what-youll-learn
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', () => {
            localStorage.setItem(checkbox.id, checkbox.checked);
            if (checkbox.checked) {
                showCongratsMessage();
                triggerConfetti(); // Trigger confetti when checkbox is checked
            }
        });
    });

    // Save state to local storage when checkbox is clicked for .key-projects
    projectCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', () => {
            localStorage.setItem(checkbox.id, checkbox.checked);
            if (checkbox.checked) {
                showCongratsMessage();
                triggerConfetti(); // Trigger confetti when checkbox is checked
            }
        });
    });

    // Add click event to <span> elements to toggle checkbox state for .what-youll-learn
    checkboxTexts.forEach(span => {
        span.addEventListener('click', () => {
            const checkboxId = span.getAttribute('data-for');
            const checkbox = document.getElementById(checkboxId);
            checkbox.checked = !checkbox.checked; // Toggle checkbox state
            checkbox.dispatchEvent(new Event('change')); // Trigger change event
        });
    });

    // Add click event to <span> elements to toggle checkbox state for .key-projects
    projectCheckboxTexts.forEach(span => {
        span.addEventListener('click', () => {
            const checkboxId = span.getAttribute('data-for');
            const checkbox = document.getElementById(checkboxId);
            checkbox.checked = !checkbox.checked; // Toggle checkbox state
            checkbox.dispatchEvent(new Event('change')); // Trigger change event
        });
    });
});

// Congrats Message Logic
function showCongratsMessage() {
    const congratsMessage = document.getElementById('congratsMessage');
    congratsMessage.style.display = 'block';
    setTimeout(() => {
        congratsMessage.style.display = 'none';
    }, 3000);
}

// Confetti Logic
function triggerConfetti() {
    confetti({
        particleCount: 200, // Number of confetti particles
        spread: 90, // Spread of confetti
        origin: { y: 0.6 } // Origin of the confetti (0.6 means slightly above the bottom)
    });
}