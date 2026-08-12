from decimal import Decimal

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Product, Category

DISCOUNT_RATIO = Decimal('0.76')


def category_list(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'product_app/category.html', context)


def _enrich_product(product):
    detail = product.productbadge_set.first()
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

    products = Product.objects.filter(is_available=True)

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
        .prefetch_related("productbadge_set")
        .order_by("-id")
    )

    paginator = Paginator(products, 15)
    page_obj = paginator.get_page(request.GET.get("page"))

    for product in page_obj:
        _enrich_product(product)

    return render(
        request,
        "product_app/products.html",
        {
            "products": page_obj,
            "query": query,
        },
    )


def product_detail(request, slug):
    product = get_object_or_404(
        Product.objects.select_related("brand", "category").prefetch_related(
            "productbadge_set", "productdescription_set"
        ),
        slug=slug,
    )
    
    recent_products = Product.objects.filter(is_available=True).exclude(id=product.id).order_by('-id')[:10]
    
    product_comments = product.comments_set.filter(product=product).order_by('-date')
    _enrich_product(product)

    return render(
        request,
        "product_app/product_detail.html",
        {
            "product": product,
            "product_comments": product_comments,
            "recent_products": recent_products,
        },
    )
