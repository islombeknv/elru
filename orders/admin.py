from django.contrib import admin

from orders.models import OrderModel


@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    search_fields = ['order_id', 'user', 'full_name']
    list_display = ['order_id', 'full_name', 'price', 'phone', 'status']
    list_filter = ['created_at', 'pay', 'status']
