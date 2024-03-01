# Продолжаем работу с авторами, статьями и комментариями. 
# Создайте форму для добавления нового автора в базу данных. 
# Используйте ранее созданную модель Author
from django import forms
from secondapp.models import Author, Post, Comment
from thirdapp.models import Product

class Game(forms.Form):
    choose = forms.ChoiceField(choices=[('coin', 'Монетка'),('dice', 'Кости'),('rand_number', 'Случайное число')])
    attempts = forms.IntegerField(min_value=1, max_value=64)

class NewAuthor(forms.ModelForm):   
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'email', 'bio', 'birth_date']


class NewPost(forms.ModelForm):   
    class Meta:
        model = Post
        fields = ['title', 'body', 'author', 'category', 'pub_flag']

class NewComment(forms.ModelForm):   
    class Meta:
        model = Comment
        fields = ['author', 'post', 'body']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'photo']
        