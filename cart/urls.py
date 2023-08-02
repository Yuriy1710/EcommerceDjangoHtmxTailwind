from django.urls import path
from . import views


urlpatterns = [
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name="add_to_cart"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('hx-menu-cart/', views.hx_menu_cart, name="hx_menu_cart"),
    path('hx-cart-total/', views.hx_cart_total, name="hx_cart_total"),
    path('update_cart/<int:product_id>/<str:action>/', views.update_cart, name="update_cart"),
]