from django.shortcuts import render
from django.views import View

from payment.cart import Cart


class CartView(View):
    def get(self, request):
        cart = Cart(request)
        cart_length = len([item for item in cart])    # length of cart values
        context = {
            'cart': cart,
            'cart_length': cart_length
        }
        return render(request, 'payment/cart_detail.html', context)
