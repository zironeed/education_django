# Generated by Django 4.2.1 on 2023-06-12 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.DateField(blank=True, null=True, verbose_name='Дата создания'),
        ),
    ]