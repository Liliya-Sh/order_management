"""
Административные настройки для приложения restaurant_ordering.
"""

from django.contrib import admin

from .models import Menu, OrderItem, Order, Customer


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Админка для управления заказами."""
    list_display = ['creation_time', 'comment', 'status_cook', 'status_delivery', 'payment_state']
    list_filter = ['creation_time', 'status_cook', 'status_delivery', 'payment_state']
    list_per_page = 7


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    """Админка для управления элементами заказа."""
    list_display = ['order', 'product', 'quantity', 'price', 'discount']
    list_filter = ['order', 'product']
    list_per_page = 7


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """Админка для управления меню."""
    list_display = ['name_product', 'slug', 'description', 'price', 'created']
    list_editable = ['price', 'description',]
    prepopulated_fields = {'slug': ('name_product',)}
    list_per_page = 7


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """Админка для управления клиентами."""
    list_display = ['name', 'phone_number', 'address']
    list_per_page = 10
