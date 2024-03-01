from django.urls import path 
from .views import game, newauthor, newpost, newcomment, AllOrders, add_product




urlpatterns = [
    path('games/', game, name='game'),
    path('newauthor/', newauthor, name='newauthor'),
    path('newpost/', newpost, name='newpost'),
    path('newcomment/', newcomment, name='newcomment'),
    path('allorders/', AllOrders.as_view(), name='ordered_products_list'),
    path('newproduct/', add_product, name='newproduct'),
]    