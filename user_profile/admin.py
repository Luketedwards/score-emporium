from django.contrib import admin
from .models import UserProfile


# Register your models here.

class userProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'profile_picture',
        'cover_photo',
        'sales_number',
        'sales_income',
        'money_due',
        'vendor',
        'sort_code',
        'account_number',
        'card_name',
        'profile_picture',
        'cover_photo',
        'average_rating',
    )

admin.site.register(UserProfile, userProfileAdmin)
