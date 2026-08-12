from django.shortcuts import render, redirect
from product_app.views import _enrich_product
from django.core.mail import send_mail
from django.conf import settings

from product_app.models import Product, Category, Comments


# Create your views here.


def home(request):
    products = (Product.objects.filter
                (is_available=True, category__name='Health care')
                .select_related('brand', 'category')
                .prefetch_related('productbadge_set')
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
    products = (Product.objects.filter
                (is_available=True)
                .select_related('brand', 'category')
                .prefetch_related('productdetail_set')
                .order_by('-id')[:8]
                )
    
    
    products_2 = (Product.objects.filter
                (is_available=True)
                .select_related('brand', 'category')
                .prefetch_related('productdetail_set')
                .order_by('id')[:8]
                )
    

    for product in products:
        _enrich_product(product)
        
    
    for product in products_2:
        _enrich_product(product)
        
        
    categories = Category.objects.all()
    
    context = {
        'products': products,
        'products_2': products_2,
        'categories': categories,
    }
    
    return render(request, "home/medical-shop.html", context)


def about(request):
    return render(request, "home/about.html")


def contact(request):
    if request.method == 'POST':
        user_email = request.POST.get('email')
        user_name = request.POST.get('full_name')
        user_message = request.POST.get('message')

        send_mail(
            subject=f"{user_name} feedback",
            message=user_message,
            from_email=user_email,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )
        
    return render(request, "home/contact.html")


def subscribe(request):
    if request.method == 'POST':
        user_email = request.POST.get('email')

        send_mail(
            subject="Welcome to MEDIFIT",
            message="""Thank you for subscribing to our newsletter!
                We are excited to have you on board and look
                forward to keeping you updated with the latest news,
                offers, and promotions from MEDIFIT.""",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user_email],
            fail_silently=False,
        )

        return redirect(request.META.get('HTTP_REFERER', 'home:home'))

    return redirect('home:home')
