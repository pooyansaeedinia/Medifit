from django.urls import path
from .views import home, shop

app_name = 'home'
urlpatterns = [
    path('', home, name='home'),
    path('shop/', shop, name='shop'),
]