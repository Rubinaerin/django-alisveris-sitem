from django.contrib import admin
from .models import Order, OrderItem

# OrderItem'ı Order modeline satır içi (inline) ekleyin
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

# Order modelini yönetici panelinde kaydedin
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created']
    list_filter = ['created', 'updated']
    inlines = [OrderItemInline]