from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import BaseModel


class Category(BaseModel):
    title = models.CharField(
        max_length=70,
        verbose_name=_("عنوان")
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        null=True,
        blank=True,
        verbose_name=_("والد")
    )
    is_child = models.BooleanField(default=False, verbose_name=_("فرزند است"))
    slug = models.SlugField(
        unique=True,
        verbose_name=_("ﺎﺳﻼﮔ"),
        null=True,
        blank=True,
        allow_unicode=True
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.title
