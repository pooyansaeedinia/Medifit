// ========== LATEST PRODUCTS SLIDER ==========
const latestTrack = document.getElementById('latestSliderTrack');
const prevLatestBtn = document.getElementById('prevLatestBtn');
const nextLatestBtn = document.getElementById('nextLatestBtn');
const latestDots = document.getElementById('latestProductDots');

let latestCurrentIndex = 0;
let latestItemsPerView = 4;
let latestTotalItems = 0;

function updateLatestItemsPerView() {
    const width = window.innerWidth;
    if (width <= 576) {
        latestItemsPerView = 1;
    } else if (width <= 768) {
        latestItemsPerView = 2;
    } else if (width <= 992) {
        latestItemsPerView = 3;
    } else {
        latestItemsPerView = 4;
    }
}

function updateLatestTotalItems() {
    const items = document.querySelectorAll('#latestSliderTrack .product-card');
    latestTotalItems = items.length;
}

function updateLatestSlider() {
    const maxIndex = Math.ceil(latestTotalItems - latestItemsPerView);
    if (latestCurrentIndex > maxIndex) {
        latestCurrentIndex = maxIndex;
    }
    if (latestCurrentIndex < 0) {
        latestCurrentIndex = 0;
    }

    const itemWidth = latestTrack.children[0]?.offsetWidth || 0;
    const gap = 30;
    const translateX = latestCurrentIndex * (itemWidth + gap);
    latestTrack.style.transform = 'translateX(-' + translateX + 'px)';

    updateLatestDots();
}

function updateLatestDots() {
    if (!latestDots) return;
    const maxIndex = Math.ceil(latestTotalItems - latestItemsPerView);
    const dotCount = maxIndex + 1;

    let dotsHtml = '';
    for (let i = 0; i < dotCount; i++) {
        dotsHtml += '<div class="dot ' + (i === latestCurrentIndex ? 'active' : '') + '" data-index="' + i + '"></div>';
    }
    latestDots.innerHTML = dotsHtml;

    const dots = document.querySelectorAll('#latestProductDots .dot');
    for (let i = 0; i < dots.length; i++) {
        dots[i].addEventListener('click', function() {
            latestCurrentIndex = parseInt(this.getAttribute('data-index'));
            updateLatestSlider();
        });
    }
}

function nextLatest() {
    const maxIndex = Math.ceil(latestTotalItems - latestItemsPerView);
    if (latestCurrentIndex < maxIndex) {
        latestCurrentIndex++;
        updateLatestSlider();
    }
}

function prevLatest() {
    if (latestCurrentIndex > 0) {
        latestCurrentIndex--;
        updateLatestSlider();
    }
}

if (prevLatestBtn) {
    prevLatestBtn.addEventListener('click', prevLatest);
}
if (nextLatestBtn) {
    nextLatestBtn.addEventListener('click', nextLatest);
}

function initLatestSlider() {
    updateLatestItemsPerView();
    updateLatestTotalItems();
    updateLatestSlider();
}

window.addEventListener('resize', function() {
    updateLatestItemsPerView();
    updateLatestTotalItems();
    updateLatestSlider();
});

initLatestSlider();