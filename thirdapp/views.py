from django.shortcuts import render
from .forms import Game, NewAuthor, NewPost
from secondapp.views import gen_coins, gen_dice, gen_number, author_articles, full_article
from .models import Order
from django.views import View
from django.utils import timezone
from datetime import timedelta


def game(request):
    if request.method == "POST":
        form = Game(request.POST)
        if form.is_valid():
            choose = form.cleaned_data.get('choose')
            attempts = form.cleaned_data.get('attempts')
            if choose == 'coin':
                return gen_coins(request, attempts)
            elif choose == 'dice':
                return gen_dice(request, attempts)
            elif choose == 'rand_number':
                return gen_number(request)
        else:
            return render(request, 'thirdapp/game.html', {'form': form})
        
    return render(request, 'thirdapp/game.html', {'form': Game()})



def newauthor(request):
    if request.method == "POST":
        form = NewAuthor(request.POST)
        if form.is_valid():
            author = form.save()
            return author_articles(request, author.pk)
        else:
            return render(request, 'thirdapp/newauthor.html', {'form': form})
    return render(request, 'thirdapp/newauthor.html', {'form': NewAuthor()})


def newpost(request):
    if request.method == "POST":
        form = NewPost(request.POST)
        if form.is_valid():
            post = form.save()
            return full_article(request, post.pk)
        else:
            return render(request, 'thirdapp/newpost.html', {'form': form})
    return render(request, 'thirdapp/newpost.html', {'form': NewPost()})


class AllOrders(View):
    def get(self, request, *args, **kwargs):
        today = timezone.now()
        last_week = today - timedelta(days=7)
        last_month = today - timedelta(days=30)
        last_year = today - timedelta(days=365)

        orders_last_week = Order.objects.filter(orderdate__gte=last_week)
        orders_last_month = Order.objects.filter(orderdate__range=[last_month, today])
        orders_last_year = Order.objects.filter(orderdate__range=[last_year, today])

        products_last_week = self.get_unique_products(orders_last_week)
        products_last_month = self.get_unique_products(orders_last_month)
        products_last_year = self.get_unique_products(orders_last_year)


        context = {
            'products_last_week': products_last_week,
            'products_last_month': products_last_month,
            'products_last_year': products_last_year,
        }

        return render(request, 'all.html', context)
    
    def get_unique_products(self, orders):
        unique_products = set(orders.values_list('product__name', flat=True))
        return list(unique_products)





            



