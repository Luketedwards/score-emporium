from django.contrib import admin
from .models import UserProfile

# Register your models here.

class userProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'sales_number',
        'sales_income',
        'money_due'
    )

admin.site.register(UserProfile, userProfileAdmin)
