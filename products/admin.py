from django.contrib import admin
from .models import Product, Category, Difficulty

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
        'vendor'
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class DifficultyAdmin(admin.ModelAdmin):
    list_display = (
        'level',
    )    

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Difficulty, DifficultyAdmin)