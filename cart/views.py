from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from cart.forms import CheckoutForm

from cart.models import Cart, CartItem, Order
from django.db import transaction

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
    
    
@login_required
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


@login_required
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


@login_required
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
def checkout(request, cart_id):
    cart = get_object_or_404(
        Cart,
        id=cart_id,
        user=request.user,
        paid=False
    )

    if not cart.items.exists():
        messages.error(
            request,
            "Your cart is empty. Please add items to your cart before proceeding to checkout."
        )
        return redirect('cart:cart')

    cart_items = CartItem.objects.filter(cart=cart)

    if request.method == 'POST':

        form = CheckoutForm(request.POST)

        if form.is_valid():

            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            postal = form.cleaned_data['postal']
            payment = form.cleaned_data['payment']

            # Convert form payment values to model payment values
            payment_method_map = {
                'card': 'credit_card',
                'paypal': 'paypal',
                'cod': 'cash_on_delivery',
            }

            payment_method = payment_method_map[payment]

            try:
                with transaction.atomic():

                    # Create order
                    order = Order.objects.create(
                        cart=cart,
                        user=request.user,
                        email=request.user.email,
                        phone_number=phone,
                        shipping_address=address,
                        city=city,
                        postal_code=postal,
                        payment_method=payment_method,
                    )

                    # Mark cart as paid
                    cart.paid = True
                    cart.save(update_fields=['paid'])

                messages.success(
                    request,
                    f"Your order #{order.id} has been placed successfully."
                )

                return redirect(
                    'home:home'
                )

            except Exception:
                messages.error(
                    request,
                    "Something went wrong while placing your order. Please try again."
                )

    else:
        form = CheckoutForm()

    return render(
        request,
        'cart/checkout.html',
        {
            'cart': cart,
            'cart_items': cart_items,
            'form': form,
        }
    )