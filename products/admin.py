from django.contrib import admin
from .models import Product, Genre, Difficulty, Review

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (

        'name',
        'genre',
        'price',
        'rating',
        'image',
        'vendor'
    )


class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class DifficultyAdmin(admin.ModelAdmin):
    list_display = (
        'level',
    )


class reviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'ratings',
        'subject',
        'content',
        'created_by',
        'date'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Difficulty, DifficultyAdmin)
admin.site.register(Review, reviewAdmin)
