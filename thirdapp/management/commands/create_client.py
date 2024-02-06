from django.core.management.base import BaseCommand
from thirdapp.models import Client


class Command(BaseCommand):
    help = 'Create Client'


    def handle(self, *args, **kwargs):
        client = Client(name='Alex', email='alexxx@mail.ru', telenumber='0694783942', address='pyshkin_62', registerdate='01.02.2024')
        ...
        client.save()
        self.stdout.write(f'Client created!')