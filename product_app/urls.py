from django.urls import path
from .views import product_list, category_list, product_detail

app_name = 'product_app'

urlpatterns = [
    path('categories/', category_list , name='category'),
    path('products/<int:id>/', product_list, name='product_list'),
    path('products/<slug:slug>/detail/', product_detail, name='product_detail'),
]