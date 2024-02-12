from collections.abc import Iterable
from django.db import models
from random import choice



# class Side(models.Model):
#     NAMES = ['Tail', 'Head']

#     coin_side = models.CharField(max_length=4, default=choice(NAMES))
#     time_stamp = models.DateTimeField(auto_now=True)

#     @staticmethod
#     def last_throws(n=None):
#         if n is None:
#             n = 0
#         sides = Side.objects.all()[-n:]
#         heads_count = tails_count = 0
#         for side in sides:
#             if side.coin_side == 'Tail':
#                 tails_count += 1
#             else:
#                 heads_count += 1
#         return {'Tail': tails_count, 'Head': heads_count}
    

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    birth_date = models.DateField()
    full_name = models.CharField(max_length=200)
    
    def save(self, *args, **kwargs):
        self.full_name = f'{self.first_name} {self.last_name}'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views_count = models.IntegerField(default=0)
    pub_flag = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title 