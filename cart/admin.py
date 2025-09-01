# cart/admin.py

from django.contrib import admin
from .models import Cart, CartItem
from django.db.models import Sum

# Cart modeli için özel bir Admin sınıfı oluşturun
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    # Admin listeleme sayfasında gösterilecek alanlar
    list_display = ('id', 'display_user', 'get_total_price')

    def display_user(self, obj):
        if obj.user:
            return obj.user.username
        else:
            return "Misafir"
    
    display_user.short_description = "Kullanıcı"

    def get_total_price(self, obj):
        total_price = obj.items.aggregate(total_price=Sum('quantity'))['total_price']
        return total_price if total_price is not None else 0
    
    get_total_price.short_description = 'Toplam Fiyat'

# CartItem modelini admin panelinde göster
admin.site.register(CartItem)