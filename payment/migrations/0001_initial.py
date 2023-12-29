# Generated by Django 5.0 on 2023-12-29 18:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.PositiveIntegerField(default=0, verbose_name='قیمت کل')),
                ('is_paid', models.BooleanField(default=False, verbose_name='وضعیت پرداخت')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ساخت')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='تاریخ آخرین بروزرسانی')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'سفارش',
                'verbose_name_plural': 'سفارش ها',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='تعداد')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='قیمت')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='course.course', verbose_name='دوره')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='payment.order', verbose_name='سفارش')),
            ],
            options={
                'verbose_name': 'آیتم سفارش ها',
                'verbose_name_plural': 'آیتم های سفارش',
            },
        ),
    ]
