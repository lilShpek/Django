from django.contrib import admin
from .models import Product, Category
# from secondapp.models import Author, Comment, Post
# from thirdapp.models import Client, Product, Order


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'quantity', 'appenddate']
    ordering = ['name', 'price', '-quantity']
    list_filter = ['appenddate', 'price'] 
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'
    actions = [reset_quantity]

    readonly_fields = ['appenddate', 'description']
    fieldsets = [ 
        ( 
            None,
              { 
                  'classes': ['wide'],
                  'fields': ['name'],
             },
               ),
               ( 'Подробности',
                 { 
                     'classes': ['collapse'],
                       'description': 'Категория товара и его подробное описание',
                         'fields': ['description'],
                           }, 
                           ),
                             ( 
                                 'Бухгалтерия',
                                   { 
                                       'fields': ['price', 'quantity'], 
                                       } 
                                       ),
                                         ( 'Дата и время добавления',
                                           { 
                                               'description': 'Дата и время добавления',
                                                 'fields': ['appenddate'], 
                                                 }
                                        ),
                                    ]



# admin.site.register(Author)
# admin.site.register(Post)
# admin.site.register(Comment)
# admin.site.register(Client)
# admin.site.register(Order)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)


# Проверьте возможность доступа к админке. 
# Создайте суперпользователя и войдите в админ панель
# Подключите к админ панели созданные вами в рамках прошлых семинаров модели в приложениях: 
# случайные числа, 
# блог, 
# магазин, 
# другие, если вы их создавали.

# Создайте в админ панели несколько групп. Логика следующая:
# Группа определяет права внутри своего приложения
# Группа читателей может просматривать модели приложения
# Группа редакторов может читать, добавлять и изменять модели приложения
# Группа админы также может удалять модели
# Создайте десяток разных пользователей. 
# Помимо минимальной информации заполните дополнительные поля модели. 
# Дайте пользователям права из различных групп, а также дополнительные индивидуальные разрешения.