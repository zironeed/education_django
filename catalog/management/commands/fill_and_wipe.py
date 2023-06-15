from django.core.management import BaseCommand
from catalog.models import Category, Product
import json

path = r'C:\Users\User\PycharmProjects\djangoFirstTask\data.json'


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        categories = []
        products = []

        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for item in data:
            if item['model'] == 'catalog.category':
                categories.append(Category(**item['fields']))

            elif item['model'] == 'catalog.product':
                item['fields']['category'] = Category.objects.get('id')
                products.append(Product(**item['fields']))

        Category.objects.bulk_create(categories)
        Product.objects.bulk_create(products)
