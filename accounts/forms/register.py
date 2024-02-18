from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.password_validation import validate_password

from phonenumber_field.formfields import PhoneNumberField

from accounts.models import User


class UserRegisterForm(forms.Form):
    register_username = forms.CharField(required=True, label=_("نام کاربری"), widget=forms.TextInput())
    register_phone = PhoneNumberField(region='IR', label=_("شماره همراه"))
    register_password = forms.CharField(
        required=True,
        label=_("رمز عبور"),
        widget=forms.PasswordInput(),
        validators=[validate_password]
    )
    register_password2 = forms.CharField(
        required=True,
        label=_("تکرار رمز عبور"),
        widget=forms.PasswordInput()
    )
    register_email = forms.EmailField(label=_("ایمیل"), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'field'
            })

    def clean_username(self):
        uname = self.cleaned_data['register_username']
        user = User.objects.filter(username=uname)
        if user:
            raise ValidationError(_("این نام کاربری از قبل وجود دارد"))
        return uname

    def clean_email(self):
        email = self.cleaned_data['register_email']
        user = User.objects.filter(email=email)
        if user:
            raise ValidationError(_("این ایمیل از قبل وجود دارد"))
        return email

    def clean_phone(self):
        phone = self.cleaned_data['register_phone']
        user = User.objects.filter(phone=phone)
        if user:
            raise ValidationError(_("این شماره همراه از قبل وجود دارد"))
        return phone

    def clean(self):
        cd = super().clean()
        p1 = cd.get('register_password1')
        p2 = cd.get('register_password2')
        if p1 and p2 and p2 != p1:
            raise ValidationError(_("رمز های عبور باید باهم برابر باشند"))
