# Generated by Django 5.0 on 2024-01-04 13:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_sold_to'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='sold_to',
        ),
        migrations.AddField(
            model_name='course',
            name='sold_to',
            field=models.ManyToManyField(blank=True, null=True, related_name='courses', to=settings.AUTH_USER_MODEL, verbose_name='خرید ها'),
        ),
    ]
