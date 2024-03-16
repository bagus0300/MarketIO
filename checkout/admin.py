from django.contrib import admin
from checkout.models import Order, OrderItem, OrderAddress


class OrderAdmin(admin.ModelAdmin):
    list_display = ["order_id", "user", "address", "email", "date_created"]
    search_fields = ["order_id", "user__username", "email"]
    list_filter = ["date_created"]


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(OrderAddress)
