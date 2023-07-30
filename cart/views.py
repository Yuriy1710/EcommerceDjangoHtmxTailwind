from django.shortcuts import render
from .cart import Cart


def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)
    context = {'cart':cart}
    
    return render(request, 'menu_cart.html')