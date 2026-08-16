from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from cart.models import Cart, CartItem

# Create your views here.


@login_required
def cart(request):
    user = request.user

    cart = user.cart_set.filter(paid=False).first()

    if not cart:
        cart = Cart.objects.create(user=user)
        
    cart_items = CartItem.objects.filter(cart=cart)

    return render(request, 'cart/cart.html', {
        'cart': cart,
        'cart_items': cart_items
    })
    

def add_to_cart(request, product_id, quantity):
    user = request.user
    cart, created = Cart.objects.get_or_create(user=user, paid=False)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product_id=product_id)
    if not created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity
    cart_item.save()

    return redirect('cart:cart')

def remove_item(request, item_id):
    user = request.user
    cart = user.cart_set.filter(paid=False).first()

    if cart:
        try:
            item = CartItem.objects.get(id=item_id, cart=cart)
            item.delete()
        except CartItem.DoesNotExist:
            pass

    return redirect('cart:cart')


def minus_item(request, item_id):
    user = request.user
    cart = user.cart_set.filter(paid=False).first()

    if cart:
        try:
            item = CartItem.objects.get(id=item_id, cart=cart)
            if item.quantity > 1:
                item.quantity -= 1
                item.save()
            else:
                item.delete()
        except CartItem.DoesNotExist:
            pass

    return redirect('cart:cart')


@login_required
def checkout(request):
    return render(request, 'cart/checkout.html')