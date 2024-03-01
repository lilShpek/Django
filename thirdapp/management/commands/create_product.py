from django.core.management.base import BaseCommand
from thirdapp.models import Product


class Command(BaseCommand):
    help = 'Create Product'


    def handle(self, *args, **kwargs):
        product = Product(name='Mouse', description='Logitech', price='55', quantity='500', appenddate='06.02.2024')
        ...
        product.save()
        self.stdout.write(f'Product created!')