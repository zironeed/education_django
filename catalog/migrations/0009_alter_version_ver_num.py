# Generated by Django 4.2.1 on 2023-07-09 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_alter_version_ver_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='ver_num',
            field=models.IntegerField(verbose_name='Версия'),
        ),
    ]
