from django.contrib import admin
from .models import Buyer, Game


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')
    search_fields = ('name',)
    list_per_page = 10

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'description', 'size', 'age_limited')
    list_filter = ('age_limited',)
    search_fields = ('title',)

    fieldsets = (
        (None, {
            'fields': ('title', 'size', 'age_limited')
        }),
        ('Доп. параметры', {
            'fields': ('description', )
        })
    )