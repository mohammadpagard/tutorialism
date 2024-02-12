from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from accounts.forms import RegisterForm
from accounts.models import User


class UserRegisterView(View):
    form_class = RegisterForm
    template_name = 'accounts/register.html'

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
            User.objects.bulk_create(
                [
                    User(
                        username=cd['username'],
                    phone=cd['phone'],
                    email=cd['email'],
                    password=cd['password']
                    )
                ],
                ignore_conflicts=True,
            )
            messages.success(request, _('ثبت نام شما با موفقیت انجام شد'), 'success')
            return redirect('home:home')
        else:
            form.errors
        context = {'form': form}
        return render(request, self.template_name, context)
