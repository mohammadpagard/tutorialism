from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from payment.cart import Cart
from payment.models import Order, OrderItem


class OrderDetailView(LoginRequiredMixin, View):
    def get(self, request, order_id=None):
        order = get_object_or_404(Order, id=order_id)
        context = {'order': order}
        return render(request, 'payment/order_detail.html', context)


class OrderCreateView(LoginRequiredMixin, View):
    def get(self, request):
        cart = Cart(request)
        order = Order.objects.create(
            user=request.user,
            total_price=cart.total_price()
        )
        for item in cart:
            OrderItem.objects.bulk_create(
                [
                    OrderItem(
                        order=order,
                        course=item['course'],
                        price=item['price'],
                        quantity=item['quantity']
                    )
                ],
                ignore_conflicts=True,
            )
        cart.clear()
        return redirect('payment:order_detail', order.id)
