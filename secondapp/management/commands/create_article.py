from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from secondapp.models import Post, Author
from random import choice
from datetime import datetime


class Command(BaseCommand):
    help = 'Create article'


    def handle(self, *args, **kwargs):
        authors = Author.objects.all()
        article = Post(
            title=lorem_ipsum.words(count=10, common=False),
            body=lorem_ipsum.paragraphs(count=3, common=False),
            author=choice(authors),
            date=datetime.now().strftime('%Y-%m-%d'),
            category=choice(lorem_ipsum.WORDS).capitalize(),
            pub_flag=choice([True, False])    
        )
        article.save()
        print('Создание статей завершено')