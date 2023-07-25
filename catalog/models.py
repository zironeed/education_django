from django.db import models
from config import settings

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.CharField(max_length=100, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='images/', unique=True, **NULLABLE, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    last_change = models.DateField(auto_now=True, verbose_name='Последнее изменение')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Owner')

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    @property
    def active_version(self):
        return self.version_set.last()


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, **NULLABLE, verbose_name='slug')
    body = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='images/', **NULLABLE, verbose_name='Изображение')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Признак публикации')
    view_count = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    ver_num = models.IntegerField(verbose_name='Версия')
    ver_name = models.CharField(max_length=100, verbose_name='Название версии')
    is_published = models.BooleanField(default=True, verbose_name='Признак версии')

    def __str__(self):
        return f'Версия {self.ver_num} | {self.ver_name}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
