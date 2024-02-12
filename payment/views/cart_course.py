from django.shortcuts import redirect
from django.views import View

from urllib.parse import unquote

from payment.cart import Cart
from course.models import Course

CART_DETAIL_URL = 'payment:cart_detail'


class CartAddCourseView(View):
    def post(self, request, course_id=None):
        cart = Cart(request)
        course = Course.objects.filter(id=course_id).first()
        cart.add(course)
        return redirect(CART_DETAIL_URL)


class CartRemoveCourseView(View):
    def get(self, request, course_id=None):
        cart = Cart(request)
        course = Course.objects.filter(id=course_id).first()
        cart.remove(course)
        return redirect(CART_DETAIL_URL)
