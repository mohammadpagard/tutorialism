from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        db_index=True,
        default=timezone.now,
        verbose_name=_("تاریخ ساخت")
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("تاریخ آخرین بروزرسانی"))

    class Meta:
        abstract = True
