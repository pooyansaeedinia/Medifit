from django.shortcuts import render
from product_app.views import _enrich_product

from product_app.models import Product, Category, Comments


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


    categories = Category.objects.all()

    comments = Comments.objects.all().order_by('-rate')[:5]

    context = {
        'products': products,
        'categories': categories,
        'comments': comments
    }
    return render(request, "home/home-page.html", context)


def shop(request):
    return render(request, "home/medical-shop.html")


def about(request):
    return render(request, "home/about.html")


def contact(request):
    return render(request, "home/contact.html")
