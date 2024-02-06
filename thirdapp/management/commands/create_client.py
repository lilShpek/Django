from django.core.management.base import BaseCommand
from thirdapp.models import Client


class Command(BaseCommand):
    help = 'Create Client'


    def handle(self, *args, **kwargs):
        client = Client(name='Victoria', email='victoria@mail.ru', telenumber='5437545452', address='pyshkin_62', registerdate='06.02.2024')
        ...
        client.save()
        self.stdout.write(f'Client created!')