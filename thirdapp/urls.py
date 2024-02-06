from django.urls import path 
from .views import game, newauthor, newpost, AllOrders




urlpatterns = [
    path('gen/games/', game, name='game'),
    path('newauthor/', newauthor, name='newauthor'),
    path('newpost/', newpost, name='newpost'),
    path('allorders/', AllOrders.as_view(), name='ordered_products_list'),
]    