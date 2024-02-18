from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=30,
        unique=True,
        verbose_name=_("نام کاربری")
    )
    phone = PhoneNumberField(
        region='IR',
        unique=True,
        verbose_name=_("شماره همراه")
    )
    fullname = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("نام و نام‌ خانوادگی")
    )
    email = models.EmailField(
        null=True,
        blank=True,
        verbose_name=_("ایمیل")
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("فعال")
    )
    is_admin = models.BooleanField(
        default=False,
        verbose_name=_("ادمین")
    )

    objects = UserManager()
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _("کاربر")
        verbose_name_plural = _("کاربر ها")

    def __str__(self) -> str:
        return str(self.phone)

    def save(self, *args, **kwargs):
        self.email = self.email.lower().strip()
        self.username = self.username.lower().strip()
        result = super().save(*args, **kwargs)
        return result

    @property
    def is_staff(self):
        return self.is_admin
