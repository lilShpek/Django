from django.shortcuts import render
from django.http import HttpResponse
from random import choice, randint
import logging
from .models import Post, Comment

logger = logging.getLogger('secondapp.views')

def log(view):
    def wrapper(request, *args, **kwargs):
        res = view(request, *args, **kwargs)
        # print(res.content)
        logger.info(f'The function {view.__name__} was returned {res.content}')
        return res
    return wrapper


@log
def gen_coins(request, numb):
    result = [choice(['tail', 'head']) for _ in range(numb)]
    return render(request, 'secondapp/index.html', {'res': result})

@log
def gen_dice(request, numb):
    result = [choice(['Выпала кость 1', 'Выпала кость 2', 'Выпала кость 3', 'Выпала кость 4', 'Выпала кость 5', 'Выпала кость 6']) for _ in range(numb)]
    return render(request, 'secondapp/dice.html', {'res': result})

@log
def gen_number(request):
    return HttpResponse(f'Выпало случайное число: {randint(0, 100)}')


# def home(request):
#     html = '<h1>Добро пожаловать на главную страницу моего сайта!</h1>'
#     logger.info("Посещена главная страница")
#     return HttpResponse(html)


# def about(request):
#     html = '<h1>Это страница на которой написано немного информации обо мне</h1><p><h1>Привет! Меня зовут Даниил Калараш, я из города Кишинёв, учусь в школе, в 11 классе, увлекаюсь программированием.</h1></p>'
#     logger.info("Посещена страница 'Обо мне'")
#     return HttpResponse(html)


def author_articles(request, id_author):
    articles = Post.objects.filter(author_id=id_author)
    return render(request, 'secondapp/author.html', {'res': articles})

def full_article(request, article_id):
    full = Post.objects.get(id=article_id)
    return render(request, 'secondapp/post.html', {'post': full})

def article_comments(request, comment_id):
    comments = Comment.objects.filter(id=comment_id)
    return render(request, 'secondapp/comment.html', {'comm': comments})

# Create your views here.
