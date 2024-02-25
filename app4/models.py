from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True) 
    
    def __str__(self):
        return self.name 
    
class Product(models.Model):
    name = models.CharField(max_length=40, unique=True)
    description = models.TextField(max_length=500)
    price = models.FloatField()
    quantity = models.IntegerField()
    appenddate = models.DateField(auto_now_add=True)
    # photo = models.ImageField(upload_to='thirdapp/', null=True, blank=True, default=['name'])
    
    # def __str__(self):
    #     return self.name 
