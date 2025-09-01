# orders/views.py

from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Order, OrderItem
from cart.models import Cart, CartItem
from django.contrib.auth.decorators import login_required 
from cart.views import get_user_cart


@login_required
def create_order(request):
    cart = get_user_cart(request)

    if request.method == 'POST':
        if not cart.items.exists():
            messages.error(request, "Sipariş oluşturmak için sepetinizde ürün bulunmuyor.")
            return redirect('cart:cart_detail')

        with transaction.atomic():
            # Siparişi oluştur
            order = Order.objects.create(user=request.user)

            for cart_item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    price=cart_item.product.price
                )
                # Stoktan düşürme işlemi
                cart_item.product.stock -= cart_item.quantity
                cart_item.product.save()

            # Sepeti ve sepet öğelerini temizle
            cart.items.all().delete()

            messages.success(request, f'Siparişiniz başarıyla oluşturuldu. Sipariş No: {order.pk}')

            return redirect('orders:order_detail', order_id=order.pk)

    # GET isteği geldiğinde sipariş önizleme sayfasını göster
    context = {'cart': cart}
    return render(request, 'orders/create_order.html', context)

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id, user=request.user)
    context = {
        'order': order,
    }
    return render(request, 'orders/order_detail.html', context)