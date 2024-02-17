from django import forms
from django.utils.translation import gettext_lazy as _

from phonenumber_field.formfields import PhoneNumberField


class UserLoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'field'
            })

    login_phone = PhoneNumberField(
        region='IR',
        label=_("شماره همراه")
    )
    login_password = forms.CharField(label=_("رمز عبور"), widget=forms.PasswordInput())
