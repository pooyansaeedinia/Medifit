// mobile menu
const mobileBtn = document.getElementById('mobileMenuBtn');
const mobileMenu = document.getElementById('mobileMenu');

if (mobileBtn && mobileMenu) {
    mobileBtn.addEventListener('click', function() {
        mobileMenu.classList.toggle('open');
    });

    const menuLinks = document.querySelectorAll('.mobile-menu a');
    for (let i = 0; i < menuLinks.length; i++) {
        menuLinks[i].addEventListener('click', function() {
            mobileMenu.classList.remove('open');
        });
    }

    document.addEventListener('click', function(event) {
        if (mobileMenu.classList.contains('open')) {
            const isClickOnMenuBtn = mobileBtn.contains(event.target);
            const isClickInsideMenu = mobileMenu.contains(event.target);

            if (!isClickOnMenuBtn && !isClickInsideMenu) {
                mobileMenu.classList.remove('open');
            }
        }
    });
}

// Search modal
const searchIcon = document.querySelector('.header-icons .bi-search');
const searchModal = document.getElementById('searchModal');
const closeSearchBtn = document.getElementById('closeSearchModal');
const searchModalOverlay = document.querySelector('.search-modal-overlay');
const searchInput = document.getElementById('searchInput');

function openSearchModal() {
    if (!searchModal) return;
    searchModal.classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeSearchModal() {
    if (!searchModal) return;
    searchModal.classList.remove('active');
    document.body.style.overflow = '';
    if (searchInput) {
        searchInput.value = '';
    }
}

if (searchIcon) {
    searchIcon.addEventListener('click', openSearchModal);
}

if (closeSearchBtn) {
    closeSearchBtn.addEventListener('click', closeSearchModal);
}

if (searchModalOverlay) {
    searchModalOverlay.addEventListener('click', closeSearchModal);
}

document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && searchModal && searchModal.classList.contains('active')) {
        closeSearchModal();
    }
});

// Mobile search modal
const mobileSearchIconNew = document.querySelector('.mobile-search-icon');
const mobileSearchModal = document.getElementById('mobileSearchModal');
const closeMobileSearch = document.getElementById('closeMobileSearch');
const cancelMobileSearch = document.getElementById('cancelMobileSearch');
const mobileSearchInput = document.getElementById('mobileSearchInput');
const mobileSearchForm = document.getElementById('mobileSearchForm');
const mobileSuggestions = document.getElementById('mobileSuggestions');
const mobileSearchResults = document.getElementById('mobileSearchResults');

function openMobileSearch() {
    if (mobileSearchModal) {
        mobileSearchModal.classList.add('active');
        document.body.style.overflow = 'hidden';
        setTimeout(function() {
            if (mobileSearchInput) {
                mobileSearchInput.focus();
            }
        }, 100);
    }
}

function closeMobileSearchModal() {
    if (mobileSearchModal) {
        mobileSearchModal.classList.remove('active');
        document.body.style.overflow = '';
        if (mobileSearchInput) {
            mobileSearchInput.value = '';
        }
        if (mobileSuggestions) {
            mobileSuggestions.style.display = 'block';
        }
        if (mobileSearchResults) {
            mobileSearchResults.style.display = 'none';
        }
    }
}

function submitMobileSearch(query) {
    if (!mobileSearchForm || !mobileSearchInput) return;
    mobileSearchInput.value = query.trim();
    if (mobileSearchInput.value) {
        mobileSearchForm.submit();
    }
}

if (mobileSearchIconNew) {
    mobileSearchIconNew.addEventListener('click', openMobileSearch);
}

if (closeMobileSearch) {
    closeMobileSearch.addEventListener('click', closeMobileSearchModal);
}

if (cancelMobileSearch) {
    cancelMobileSearch.addEventListener('click', closeMobileSearchModal);
}

if (mobileSearchInput) {
    mobileSearchInput.addEventListener('keydown', function(e) {
        if (e.key === 'Enter') {
            e.preventDefault();
            submitMobileSearch(mobileSearchInput.value);
        }
    });
}

const mobileTags = document.querySelectorAll('.mobile-suggestions-tags span');
for (let i = 0; i < mobileTags.length; i++) {
    mobileTags[i].addEventListener('click', function() {
        submitMobileSearch(this.textContent);
    });
}

document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && mobileSearchModal && mobileSearchModal.classList.contains('active')) {
        closeMobileSearchModal();
    }
});

// ========== PRODUCT SLIDER ==========
const productTrack = document.getElementById('productSliderTrack');
const prevProductBtn = document.getElementById('prevProductBtn');
const nextProductBtn = document.getElementById('nextProductBtn');
const productDots = document.getElementById('productDots');

let productCurrentIndex = 0;
let productItemsPerView = 4;
let productTotalItems = 0;

function updateProductItemsPerView() {
    const width = window.innerWidth;
    if (width <= 576) {
        productItemsPerView = 1;
    } else if (width <= 768) {
        productItemsPerView = 2;
    } else if (width <= 992) {
        productItemsPerView = 3;
    } else {
        productItemsPerView = 4;
    }
}

function updateProductTotalItems() {
    const items = document.querySelectorAll('#productSliderTrack .product-card');
    productTotalItems = items.length;
}

function updateProductSlider() {
    if (!productTrack) return;

    const maxIndex = Math.ceil(productTotalItems - productItemsPerView);
    if (productCurrentIndex > maxIndex) {
        productCurrentIndex = maxIndex;
    }
    if (productCurrentIndex < 0) {
        productCurrentIndex = 0;
    }

    const itemWidth = productTrack.children[0]?.offsetWidth || 0;
    const gap = 30;
    const translateX = productCurrentIndex * (itemWidth + gap);
    productTrack.style.transform = 'translateX(-' + translateX + 'px)';

    updateProductDots();
}

function updateProductDots() {
    if (!productDots) return;
    const maxIndex = Math.ceil(productTotalItems - productItemsPerView);
    const dotCount = maxIndex + 1;

    let dotsHtml = '';
    for (let i = 0; i < dotCount; i++) {
        dotsHtml += '<div class="dot ' + (i === productCurrentIndex ? 'active' : '') + '" data-index="' + i + '"></div>';
    }
    productDots.innerHTML = dotsHtml;

    const dots = document.querySelectorAll('#productDots .dot');
    for (let i = 0; i < dots.length; i++) {
        dots[i].addEventListener('click', function() {
            productCurrentIndex = parseInt(this.getAttribute('data-index'));
            updateProductSlider();
        });
    }
}

function nextProduct() {
    const maxIndex = Math.ceil(productTotalItems - productItemsPerView);
    if (productCurrentIndex < maxIndex) {
        productCurrentIndex++;
        updateProductSlider();
    }
}

function prevProduct() {
    if (productCurrentIndex > 0) {
        productCurrentIndex--;
        updateProductSlider();
    }
}

if (prevProductBtn) {
    prevProductBtn.addEventListener('click', prevProduct);
}
if (nextProductBtn) {
    nextProductBtn.addEventListener('click', nextProduct);
}

// Slider
const reviewTrack = document.getElementById('reviewSliderTrack');
const prevReviewBtn = document.getElementById('prevReviewBtn');
const nextReviewBtn = document.getElementById('nextReviewBtn');
const reviewDots = document.getElementById('reviewDots');

let reviewCurrentIndex = 0;
let reviewItemsPerView = 2;
let reviewTotalItems = 0;

function updateReviewItemsPerView() {
    const width = window.innerWidth;
    if (width <= 768) {
        reviewItemsPerView = 1;
    } else {
        reviewItemsPerView = 2;
    }
}

function updateReviewTotalItems() {
    const items = document.querySelectorAll('#reviewSliderTrack .review-card');
    reviewTotalItems = items.length;
}

function updateReviewSlider() {
    if (!reviewTrack) return;

    const maxIndex = Math.ceil(reviewTotalItems - reviewItemsPerView);
    if (reviewCurrentIndex > maxIndex) {
        reviewCurrentIndex = maxIndex;
    }
    if (reviewCurrentIndex < 0) {
        reviewCurrentIndex = 0;
    }

    const itemWidth = reviewTrack.children[0]?.offsetWidth || 0;
    const gap = 30;
    const translateX = reviewCurrentIndex * (itemWidth + gap);
    reviewTrack.style.transform = 'translateX(-' + translateX + 'px)';

    updateReviewDots();
}

function updateReviewDots() {
    if (!reviewDots) return;
    const maxIndex = Math.ceil(reviewTotalItems - reviewItemsPerView);
    const dotCount = maxIndex + 1;

    let dotsHtml = '';
    for (let i = 0; i < dotCount; i++) {
        dotsHtml += '<div class="dot ' + (i === reviewCurrentIndex ? 'active' : '') + '" data-index="' + i + '"></div>';
    }
    reviewDots.innerHTML = dotsHtml;

    const dots = document.querySelectorAll('#reviewDots .dot');
    for (let i = 0; i < dots.length; i++) {
        dots[i].addEventListener('click', function() {
            reviewCurrentIndex = parseInt(this.getAttribute('data-index'));
            updateReviewSlider();
        });
    }
}

function nextReview() {
    const maxIndex = Math.ceil(reviewTotalItems - reviewItemsPerView);
    if (reviewCurrentIndex < maxIndex) {
        reviewCurrentIndex++;
        updateReviewSlider();
    }
}

function prevReview() {
    if (reviewCurrentIndex > 0) {
        reviewCurrentIndex--;
        updateReviewSlider();
    }
}

if (prevReviewBtn) {
    prevReviewBtn.addEventListener('click', prevReview);
}
if (nextReviewBtn) {
    nextReviewBtn.addEventListener('click', nextReview);
}

function initSliders() {
    updateProductItemsPerView();
    updateProductTotalItems();
    updateProductSlider();

    updateReviewItemsPerView();
    updateReviewTotalItems();
    updateReviewSlider();
}

window.addEventListener('resize', function() {
    updateProductItemsPerView();
    updateProductTotalItems();
    updateProductSlider();

    updateReviewItemsPerView();
    updateReviewTotalItems();
    updateReviewSlider();
});

initSliders();