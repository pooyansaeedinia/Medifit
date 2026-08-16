from django.urls import path
from .views import add_to_cart, cart, checkout, minus_item, remove_item

app_name = 'cart'
urlpatterns = [
    path('', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('add/<int:product_id>/<int:quantity>/', add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', remove_item, name='remove_item'),
    path('minus/<int:item_id>/', minus_item, name='minus_item'),
]