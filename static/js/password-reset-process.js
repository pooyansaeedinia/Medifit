const resetForm = document.getElementById('reset-password-process-form');
const password1 = document.getElementById('password1');
const password2 = document.getElementById('password2');

if (resetForm) {
    resetForm.addEventListener('submit', function(e) {
        const first = password1.value.trim();
        const second = password2.value.trim();

        if (first.length < 8) {
            e.preventDefault();
            alert('Password must be at least 8 characters');
            return;
        }

        if (first !== second) {
            e.preventDefault();
            alert('Passwords do not match');
        }
    });
}
