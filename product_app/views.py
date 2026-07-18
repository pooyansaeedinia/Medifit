from decimal import Decimal
from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Product

DISCOUNT_RATIO = Decimal('0.76')


def _enrich_product(product):
    detail = product.productdetail_set.first()
    product.badge_detail = detail
    if detail and detail.badge == 'discounted':
        product.display_old_price = (
            product.price / DISCOUNT_RATIO
        ).quantize(Decimal('0.01'))
    else:
        product.display_old_price = None
    return product


def product_list(request):
    products = (
        Product.objects.filter(is_available=True)
        .select_related('brand', 'category')
        .prefetch_related('productdetail_set')
        .order_by('-id')
    )

    for product in products:
        _enrich_product(product)

    paginator = Paginator(products, 12)  # 12 items per page

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
    }
    return render(request, 'product_app/products.html', context)