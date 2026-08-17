// // Form submit
// const form = document.getElementById('checkoutForm');

// if (form) {
//     form.addEventListener('submit', function(e) {
//         e.preventDefault();

//         const name = document.getElementById('fullName').value.trim();
//         const email = document.getElementById('email').value.trim();
//         const address = document.getElementById('address').value.trim();

//         if (!name || !email || !address) {
//             alert('Please fill in all required fields.');
//             return;
//         }

//         if (!email.includes('@') || !email.includes('.')) {
//             alert('Please enter a valid email address.');
//             return;
//         }

//         alert('✅ Order placed successfully! Thank you for shopping with Medifit.');
//         form.reset();
//     });
// }