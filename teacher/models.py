from django.db import models
from django.utils.translation import gettext_lazy as _

from ckeditor_uploader.fields import RichTextUploadingField

from common.utils import path_with_hash

def avatar_path(instance, filename):
    return f"avatars/teachers/{path_with_hash(filename)}"


class Teacher(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name=_("نام")
    )
    age = models.CharField(
        max_length=2,
        verbose_name=_("سن")
    )
    bio = RichTextUploadingField(null=True, blank=True, verbose_name=_("بایو"))
    profile_image = models.ImageField(
        null=True,
        blank=True,
        verbose_name=_("تصویر پروفایل"),
        help_text=_("If possible, upload an image that is least 120 pixels wide."),
        upload_to=avatar_path,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name=_("تاریخ ثبت نام")
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True,
        verbose_name=_("تاریخ آخرین بروزرسانی")
    )

    class Meta:
        verbose_name = _("آموزگار")
        verbose_name_plural = _("آموزگارها")

    def __str__(self: str) -> str:
        return self.name
