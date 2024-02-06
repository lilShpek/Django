# Создайте три модели Django: клиент, товар и заказ.

# Клиент может иметь несколько заказов. Заказ может содержать несколько товаров. Товар может входить в несколько заказов.

# Поля модели «Клиент»:
# — имя клиента
# — электронная почта клиента
# — номер телефона клиента
# — адрес клиента
# — дата регистрации клиента

# Поля модели «Товар»:
# — название товара
# — описание товара
# — цена товара
# — количество товара
# — дата добавления товара

# Поля модели «Заказ»:
# — связь с моделью «Клиент», указывает на клиента, сделавшего заказ
# — связь с моделью «Товар», указывает на товары, входящие в заказ
# — общая сумма заказа
# — дата оформления заказа

# *Допишите несколько функций CRUD для работы с моделями по желанию. Что по вашему мнению актуально в такой базе данных.

from django.db import models



class Client(models.Model):
    name = models.CharField(max_length=30, unique=True)
    email = models.EmailField()
    telenumber = models.IntegerField()
    address = models.TextField(max_length=80)
    registerdate = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Имя: {self.name}, email: {self.email}, Номер телефона: {self.telenumber}, Адрес: {self.address}, День регистрации: {self.registerdate}'

class Product(models.Model):
    name = models.CharField(max_length=40, unique=True)
    description = models.TextField(max_length=500)
    price = models.FloatField()
    quantity = models.IntegerField()
    appenddate = models.DateField(auto_now_add=True)

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, to_field='name', db_column='client')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, to_field='name', db_column='product')
    fullprice = models.FloatField()
    orderdate = models.DateField(auto_now_add=True)


# Доработать магазин
# Создайте шаблон для вывода всех заказов клиента и списком товаров внутри каждого заказа.
# Подготовьте необходимый маршрут и представление.

# Домашнее задание задание
# Продолжаем работать с товарами и заказами.

# Создайте шаблон, который выводит список заказанных клиентом товаров из всех его заказов с сортировкой по времени:
# — за последние 7 дней (неделю)
# — за последние 30 дней (месяц)
# — за последние 365 дней (год)

# Товары в списке не должны повторятся.
# Create your models here.