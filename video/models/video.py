from django.db import models
from django.utils.translation import gettext_lazy as _

from ckeditor_uploader.fields import RichTextUploadingField

from teacher.models import Teacher
from common.models import BaseModel


class Video(BaseModel):
    title = models.CharField(
        max_length=100,
        verbose_name=_("عنوان")
    )
    description = RichTextUploadingField(verbose_name=_("توضیحات"))
    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True,
        allow_unicode=True,
        verbose_name=_("اسلاگ")
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='%(class)svideos',
        verbose_name=_("آموزگار")
    )

    class Meta:
        abstract = True

    def __str__(self: str) -> str:
        return self.title
