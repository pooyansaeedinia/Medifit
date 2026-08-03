from django.urls import path
from .views import product_list, category_list

app_name = 'product_app'

urlpatterns = [
    path('categories/', category_list , name='category'),
    path('products/', product_list, name='product_list'),
]