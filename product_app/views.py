from decimal import Decimal
from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q

from .models import Product, Category


def category_list(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'product_app/category.html', context)


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


def product_list(request, id):
    query = request.GET.get("q", "").strip()

    products = Product.objects.filter(
        is_available=True
    )

    if id != 0:
        products = products.filter(category_id=id)

    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(short_description__icontains=query) |
            Q(description__icontains=query) |
            Q(brand__name__icontains=query) |
            Q(category__name__icontains=query)
        )

    products = (
        products
        .select_related("brand", "category")
        .prefetch_related("productdetail_set")
        .order_by("-id")
    )

    for product in products:
        _enrich_product(product)

    paginator = Paginator(products, 15)

    page_obj = paginator.get_page(
        request.GET.get("page")
    )

    return render(
        request,
        "product_app/products.html",
        {
            "products": page_obj,
        }
    )

