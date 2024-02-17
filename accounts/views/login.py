from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.utils.translation import gettext_lazy as _

from accounts.forms import UserLoginForm


class UserLoginView(View):
    template_name = 'accounts/login.html'
    form_class = UserLoginForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['login_phone'], password=cd['login_password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'با موفقیت وارد حساب کاربری خود شدید', 'success')
                return redirect('home:home')
            messages.error(request, 'شماره تماس یا رمز عبور شما اشتباه بود', 'danger')
        context = {'form': form}
        return render(request, self.template_name, context)
