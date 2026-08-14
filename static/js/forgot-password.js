const recoveryForm = document.getElementById('recovery-form');
const emailInput = document.getElementById('recovery-email');

if (recoveryForm) {
    recoveryForm.addEventListener('submit', function(e) {
        const email = emailInput.value.trim();

        if (email === '') {
            e.preventDefault();
            alert('Please enter your email address');
        }
    });
}
