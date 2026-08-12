from django.urls import path
from .views import home, shop, about, contact, subscribe

app_name = 'home'
urlpatterns = [
    path('', home, name='home'),
    path('shop/', shop, name='shop'),
    path('about-us/', about, name='about'),
    path('contact-us/', contact, name='contact'),
    path('subscribe/', subscribe, name='subscribe'),
]