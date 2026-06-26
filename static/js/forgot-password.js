const recoveryForm = document.getElementById('recovery-form');
const emailInput = document.getElementById('recovery-email');

recoveryForm.addEventListener('submit', function(e) {
    e.preventDefault();

    const email = emailInput.value.trim();

    if (email === '') {
        alert('Please enter your email address');
        return;
    }

    alert('Reset link sent to ' + email);
    recoveryForm.reset();
});