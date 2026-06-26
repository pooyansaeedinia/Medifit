// Contact form
const contactForm = document.getElementById('contactForm');

if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
        e.preventDefault();

        const name = document.getElementById('fullName').value.trim();
        const email = document.getElementById('emailAddress').value.trim();
        const message = document.getElementById('message').value.trim();

        if (!name || !email || !message) {
            alert('Please fill in all required fields.');
            return;
        }

        alert('Thank you for your message! We will get back to you soon.');
        contactForm.reset();
    });
}

// FAQ
const faqItems = document.querySelectorAll('.faq-item');

faqItems.forEach(function (item) {
    const question = item.querySelector('.faq-question');

    question.addEventListener('click', function () {
        faqItems.forEach(function (other) {
            if (other !== item && other.classList.contains('active')) {
                other.classList.remove('active');
            }
        });
        item.classList.toggle('active');
    });
});