from django.shortcuts import render
from product_app.views import _enrich_product

from product_app.models import Product


# Create your views here.


def home(request):
    products = (Product.objects.filter
                (is_available=True, category__name='Health care')
                .select_related('brand', 'category')
                .prefetch_related('productdetail_set')
                .order_by('-id')
                )

    for product in products:
        _enrich_product(product)

    context = {
        'products': products
    }
    return render(request, "home/home-page.html", context)


def shop(request):
    return render(request, "home/medical-shop.html")
