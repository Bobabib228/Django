from django.core.management import call_command
from django.core.management.base import BaseCommand
from catalog.models import Product

class Command(BaseCommand):
    help = 'Add test product to the database from fixture'

    def handle(self, *args, **options):
        Product.objects.all().delete()
        call_command('loaddata', 'product_fixture.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))
