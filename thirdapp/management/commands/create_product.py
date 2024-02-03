from django.core.management.base import BaseCommand
from thirdapp.models import Product


class Command(BaseCommand):
    help = 'Create Product'


    def handle(self, *args, **kwargs):
        product =Product(name='TV', description='A good modern TV', price='149.9', quantity='30', appenddate='01.02.2024')
        ...
        product.save()
        self.stdout.write(f'Product created!')