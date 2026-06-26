function updateSummary() {
    let subtotal = 0;
    const items = document.querySelectorAll('.cart-item');

    for (let i = 0; i < items.length; i++) {
        const total = parseFloat(items[i].querySelector('.item-total').textContent.replace('$', ''));
        subtotal += total;
    }

    const shipping = items.length > 0 ? 5 : 0;
    document.getElementById('subtotal').textContent = '$' + subtotal;
    document.getElementById('shipping').textContent = '$' + shipping;
    document.getElementById('total').textContent = '$' + (subtotal + shipping);
}

const items = document.querySelectorAll('.cart-item');

for (let i = 0; i < items.length; i++) {
    const item = items[i];
    const input = item.querySelector('.qty-input');
    const price = parseFloat(item.querySelector('.cart-item-price').textContent.replace('$', ''));
    const totalSpan = item.querySelector('.item-total');

    function calc() {
        const qty = parseInt(input.value) || 1;
        totalSpan.textContent = '$' + (price * qty);
        updateSummary();
    }

    item.querySelector('.qty-btn:first-child').addEventListener('click', function() {
        if (parseInt(input.value) > 1) { input.value = parseInt(input.value) - 1; calc(); }
    });

    item.querySelector('.qty-btn:last-child').addEventListener('click', function() {
        if (parseInt(input.value) < 99) { input.value = parseInt(input.value) + 1; calc(); }
    });

    input.addEventListener('change', function() {
        let qty = parseInt(this.value) || 1;
        if (qty < 1) qty = 1;
        if (qty > 99) qty = 99;
        this.value = qty;
        calc();
    });

    item.querySelector('.remove-btn').addEventListener('click', function() {
        if (confirm('Remove?')) { item.remove(); updateSummary(); }
    });

    calc();
}