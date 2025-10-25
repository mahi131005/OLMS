// Get all "View Resources" buttons
const viewButtons = document.querySelectorAll('.view-button');

// Add click event listeners to each button
viewButtons.forEach(button => {
    button.addEventListener('click', function (event) {
        event.preventDefault(); // Prevent default link behavior

        // Get the target modal ID from the data attribute
        const targetModalId = this.getAttribute('data-modal-target');

        // Get the target modal element
        const targetModal = document.getElementById(targetModalId);

        // Add blur background to the body
        document.body.classList.add('blur-background');

        // Open the modal
        if (targetModal) {
            targetModal.style.display = 'block';
        }
    });
});

// Get all close buttons
const closeButtons = document.querySelectorAll('.close');

// Add click event listeners to each close button
closeButtons.forEach(button => {
    button.addEventListener('click', function () {
        // Find the closest modal and hide it
        const modal = this.closest('.modal');
        if (modal) {
            modal.style.display = 'none';
        }

        // Remove blur background from the body
        document.body.classList.remove('blur-background');
    });
});

// Close the modal when clicking outside of it
window.addEventListener('click', function (event) {
    if (event.target.classList.contains('modal')) {
        event.target.style.display = 'none';

        // Remove blur background from the body
        document.body.classList.remove('blur-background');
    }
});