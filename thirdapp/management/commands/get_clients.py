from django.core.management.base import BaseCommand
from thirdapp.models import Client


class Command(BaseCommand):
    help = 'Get all Clients'

    def handle(self, *agrs, **kwagrs):
        clients = Client.objects.all()
        self.stdout.write(f'{clients}')