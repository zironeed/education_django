from django.core.management import BaseCommand
from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        categories = [
            {'name': 'Фрукт', 'description': 'Не овощ'},
            {'name': 'Овощ', 'description': 'Не фрукт'},
            {'name': 'Ягода', 'description': 'Ни то, ни другое'}
        ]
        creating_categories = []

        Category.objects.all().delete()

        for category in categories:
            creating_categories.append(Category(**category))

        Category.objects.bulk_create(creating_categories)
