from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from ckeditor_uploader.fields import RichTextUploadingField

from category.models import CourseCategory
from teacher.models import Teacher
from accounts.models import User
from common.models import BaseModel


class Course(BaseModel):
    title = models.CharField(
        max_length=50,
        verbose_name=_("عنوان دوره")
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='courses',
        verbose_name=_("آموزگار")
    )
    section = models.CharField(
        max_length=3,
        verbose_name=_("تعداد قسمت ها")
    )
    description = RichTextUploadingField(verbose_name=_("توضیحات"))
    categories = models.ManyToManyField(
        CourseCategory,
        related_name='courses',
        verbose_name=_("دسته بندی ها")
    )
    price = models.PositiveIntegerField(
        default=0,
        help_text=_("به ریال وارد شود"),
        verbose_name=("قیمت")
    )
    discount = models.PositiveIntegerField(
        verbose_name=_("درصد تخفیف"),
        null=True,
        blank=True
    )
    banner = models.ImageField(
        upload_to='images/course-banner/',
        verbose_name=_("بنر")
    )
    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True,
        allow_unicode=True,
        verbose_name=_("اسلاگ")
    )
    sold_to = models.ManyToManyField(
        User,
        related_name='courses',
        blank=True,
        verbose_name=_("خرید ها")
    )
    sale_count = models.PositiveIntegerField(
        default=0,
        verbose_name=_("تعداد فروش")
    )

    class Meta:
        verbose_name = _("دوره")
        verbose_name_plural = _("دوره ها")

    def __str__(self):
        return self.title

    @property
    def discount_price(self):
        price = self.price
        discount = self.discount
        discount_price = discount * price
        division_discount_price = discount_price / 100
        subtract_result = division_discount_price - price
        result = int(abs(subtract_result))
        return result
    
    def get_absolute_url(self):
        return reverse(
            'course:course_detail',
            kwargs={'course_id': self.id, 'course_slug': self.slug}
        )
