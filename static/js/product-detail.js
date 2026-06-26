// Increase and decrease
const qtyInput = document.getElementById('quantity');
const decreaseBtn = document.getElementById('decreaseQty');
const increaseBtn = document.getElementById('increaseQty');

if (decreaseBtn) {
    decreaseBtn.addEventListener('click', function () {
        let value = parseInt(qtyInput.value) || 1;
        if (value > 1) {
            qtyInput.value = value - 1;
        }
    });
}

if (increaseBtn) {
    increaseBtn.addEventListener('click', function () {
        let value = parseInt(qtyInput.value) || 1;
        if (value < 99) {
            qtyInput.value = value + 1;
        }
    });
}

if (qtyInput) {
    qtyInput.addEventListener('change', function () {
        let value = parseInt(qtyInput.value) || 1;
        if (value < 1) value = 1;
        if (value > 99) value = 99;
        qtyInput.value = value;
    });
}

// Customer reviews
const track = document.getElementById('reviewSliderTrack');
const prevBtn = document.getElementById('prevReviewBtn');
const nextBtn = document.getElementById('nextReviewBtn');

if (track && prevBtn && nextBtn) {
    let index = 0;
    let perView = window.innerWidth <= 768 ? 1 : 2;
    let totalItems = document.querySelectorAll('#reviewSliderTrack .review-card').length;

    function update() {
        const card = track.querySelector('.review-card');
        if (!card) return;

        const width = card.offsetWidth;
        const gap = 30;
        const maxIndex = Math.max(0, totalItems - perView);

        if (index > maxIndex) index = maxIndex;
        if (index < 0) index = 0;

        track.style.transform = 'translateX(-' + (index * (width + gap)) + 'px)';
    }


    prevBtn.addEventListener('click', function() {
        if (index > 0) { index--; update(); }
    });

    nextBtn.addEventListener('click', function() {
        const max = Math.max(0, totalItems - perView);
        if (index < max) { index++; update(); }
    });

    window.addEventListener('resize', function() {
        perView = window.innerWidth <= 768 ? 1 : 2;
        totalItems = document.querySelectorAll('#reviewSliderTrack .review-card').length;
        update();
    });

    update();
}

// ========== RECENT PRODUCTS SLIDER ==========
const recentTrack = document.getElementById('recentSliderTrack');
const prevRecentBtn = document.getElementById('prevRecentBtn');
const nextRecentBtn = document.getElementById('nextRecentBtn');
const recentDots = document.getElementById('recentDots');

if (recentTrack && prevRecentBtn && nextRecentBtn) {
    let recentIndex = 0;
    let recentPerView = 3;
    let recentTotal = document.querySelectorAll('#recentSliderTrack .product-card').length;

    function updateRecent() {
        const card = recentTrack.querySelector('.product-card');
        if (!card) return;

        const width = card.offsetWidth;
        const gap = 30;
        const max = Math.max(0, recentTotal - recentPerView);

        if (recentIndex > max) recentIndex = max;
        if (recentIndex < 0) recentIndex = 0;

        recentTrack.style.transform = 'translateX(-' + (recentIndex * (width + gap)) + 'px)';
        updateRecentDots();
    }

    function updateRecentDots() {
        if (!recentDots) return;
        const count = Math.max(0, recentTotal - recentPerView) + 1;
        let html = '';
        for (let i = 0; i < count; i++) {
            html += '<div class="dot ' + (i === recentIndex ? 'active' : '') + '" data-r="' + i + '"></div>';
        }
        recentDots.innerHTML = html;

        recentDots.querySelectorAll('.dot').forEach(function(d) {
            d.addEventListener('click', function() {
                recentIndex = parseInt(this.getAttribute('data-r'));
                updateRecent();
            });
        });
    }

    prevRecentBtn.addEventListener('click', function() {
        if (recentIndex > 0) { recentIndex--; updateRecent(); }
    });

    nextRecentBtn.addEventListener('click', function() {
        const max = Math.max(0, recentTotal - recentPerView);
        if (recentIndex < max) { recentIndex++; updateRecent(); }
    });

    window.addEventListener('resize', function() {
        if (window.innerWidth <= 576) {
            recentPerView = 1;
        } else if (window.innerWidth <= 992) {
            recentPerView = 2;
        } else {
            recentPerView = 3;
        }
        recentTotal = document.querySelectorAll('#recentSliderTrack .product-card').length;
        updateRecent();
    });

    updateRecent();
}