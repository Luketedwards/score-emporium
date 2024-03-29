from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'username',
                       'order_total',
                       )

    fields = ('order_number', 'user_profile', 'date', 'username', 'full_name',
              'email', 'phone_number',
              'order_total')

    list_display = ('order_number', 'date', 'full_name', 'username',
                    'order_total')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
