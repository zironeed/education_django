# Generated by Django 4.2.1 on 2023-06-27 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_remove_category_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='last_change',
            field=models.DateField(auto_now=True, verbose_name='Последнее изменение'),
        ),
    ]
