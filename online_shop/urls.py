from django.urls import path
from online_shop.views import *

urlpatterns = [
    path('', home, name='home'),
    path('product', product_list, name='product_list'),
    path('product/<int:product_id>/', product_detail, name='product-detail'),
    path('cart', cart, name='cart'),
    path('checkout', checkout, name='checkout'),
    path('register', register, name='register'),
    path('login', log_in, name='login'),
    path('wishlist', wishlist, name='wishlist'),
    path('contact', contact, name='contact'),
    path('profile', profile_page, name='profile_page'),
]