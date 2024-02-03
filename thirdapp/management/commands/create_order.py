from django.core.management.base import BaseCommand
from thirdapp.models import Order, Client, Product
from datetime import datetime

class Command(BaseCommand):
    help = 'Create Order'

    def add_arguments(self, parser):
        parser.add_argument('client_name', type=str, help='Name of the client')
        parser.add_argument('product_name', type=str, help='Name of the product')
        parser.add_argument('fullprice', type=float, help='Full price of the order')

    def handle(self, *args, **kwargs):
        client_name = kwargs['client_name']
        product_name = kwargs['product_name']
        fullprice = kwargs['fullprice']

        try:
            client = Client.objects.get(name=client_name)
            product = Product.objects.get(name=product_name)

            
            order = Order.objects.create(
                client=client,
                product=product,
                fullprice=fullprice,
                orderdate=datetime.today()  
            )

            self.stdout.write(f'Заказ под номером: {order.id} создан')

        except Client.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Клиент с именем {client_name} не найден.'))

        except Product.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Продукт с именем {product_name} не найден.'))
