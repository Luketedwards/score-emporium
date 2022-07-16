from django.contrib import admin
from .models import Product, Genre, Difficulty

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'genre',
        'price',
        'rating',
        'image',
        'vendor'
    )

    ordering = ('sku',)

class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class DifficultyAdmin(admin.ModelAdmin):
    list_display = (
        'level',
    )    

admin.site.register(Product, ProductAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Difficulty, DifficultyAdmin)