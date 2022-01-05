from django.contrib import admin

from orders.models import OrderModel


@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    search_fields = ['full_name']
    list_display = ['order_id', 'full_name', 'phone', 'price', 'pay',  'status', 'created_at']
    list_filter = ['created_at', 'pay', 'status']
