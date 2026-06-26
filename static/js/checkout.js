function loadOrderSummary() {
    const subtotal = 100;
    const shipping = 5;
    const total = subtotal + shipping;

    document.getElementById('subtotal').textContent = '$' + subtotal;
    document.getElementById('shipping').textContent = '$' + shipping;
    document.getElementById('total').textContent = '$' + total;
}

loadOrderSummary();

// Form submit
const form = document.getElementById('checkoutForm');

if (form) {
    form.addEventListener('submit', function(e) {
        e.preventDefault();

        const name = document.getElementById('fullName').value.trim();
        const email = document.getElementById('email').value.trim();
        const address = document.getElementById('address').value.trim();

        if (!name || !email || !address) {
            alert('Please fill in all required fields.');
            return;
        }

        if (!email.includes('@') || !email.includes('.')) {
            alert('Please enter a valid email address.');
            return;
        }

        alert('✅ Order placed successfully! Thank you for shopping with Medifit.');
        form.reset();
    });
}