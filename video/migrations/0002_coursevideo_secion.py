# Generated by Django 5.0 on 2023-12-29 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursevideo',
            name='secion',
            field=models.CharField(default=1, max_length=2, verbose_name='شماره قسمت'),
            preserve_default=False,
        ),
    ]
