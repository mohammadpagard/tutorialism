from django.db import models
from django.utils.translation import gettext_lazy as _

from course.models import Course
from accounts.models import User
from common.models import BaseModel


class Order(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="orders",
        verbose_name=_("کاربر")
    )
    total_price = models.PositiveIntegerField(
        default=0,
        verbose_name=_("قیمت کل")
    )
    is_paid = models.BooleanField(
        default=False,
        verbose_name=_("وضعیت پرداخت")
    )

    class Meta:
        verbose_name = _("سفارش")
        verbose_name_plural = _("سفارش ها")

    def __str__(self):
        return str(self.user.phone)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name=_("سفارش")
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="order_items",
        verbose_name=_("دوره")
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name=_("تعداد")
    )
    price = models.PositiveIntegerField(
        default=0,
        verbose_name=_("قیمت")
    )

    class Meta:
        verbose_name = _("آیتم سفارش ها")
        verbose_name_plural = _("آیتم های سفارش")

    def __str__(self):
        return str(self.course.title)
