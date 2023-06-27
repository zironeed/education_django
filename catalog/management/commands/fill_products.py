from django.core.management import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        products = [
            {'name': 'Яблоко', 'description': 'Кислое', 'image': '', 'category': 'Фрукт', 'price': 150.0},
            {'name': 'Картофель', 'description': 'Пюрешка)', 'image': '', 'category': 'Овощ', 'price': 110.0},
            {'name': 'Клубника', 'description': 'Сладкое', 'image': '', 'category': 'Ягода', 'price': 215.0}
        ]

        creating_products = []

        Product.objects.all().delete()

        for product in products:
            category = product['category']
            product['category'] = Category.objects.get(name=category)

            creating_products.append(Product(**product))

        Product.objects.bulk_create(creating_products)

