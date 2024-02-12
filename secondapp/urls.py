from django.urls import path
from . import views 
from .views import author_articles



urlpatterns = [
    path('coin/<int:pk>', views.gen_coins, name='gen_coins'),
    path('dice/<int:pk>', views.gen_dice, name='gen_dice'),
    # path('numb/<int:pk>', views.gen_number, name='gen_number'),
    # path('', home, name='home'),
    # path('about/', about, name='about'),
    path('author_articles/<int:id_author>/', views.author_articles, name='author_articles'),
    path('author_articles/articles/<int:article_id>/', views.full_article, name='full_article'),
    path('author_articles/comments/<int:comment_id>', views.article_comments, name='article_comments'),
]