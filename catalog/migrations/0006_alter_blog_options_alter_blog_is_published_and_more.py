# Generated by Django 4.2.1 on 2023-07-08 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_blog_alter_product_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'Блог', 'verbose_name_plural': 'Блоги'},
        ),
        migrations.AlterField(
            model_name='blog',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Признак публикации'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, unique=True, upload_to='images/', verbose_name='Изображение'),
        ),
    ]
