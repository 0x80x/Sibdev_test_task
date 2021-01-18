from django.contrib import admin
from .models import *


# Register your models here.


class DealsAdmin(admin.ModelAdmin):
    # Отображение полей
    list_display = ('id', 'customer', 'item', 'total', 'quantity', 'date',)
    # Поля по которым будет выполняться поиск
    search_fields = ('customer', 'item', 'date',)


admin.site.register(Deals, DealsAdmin)
