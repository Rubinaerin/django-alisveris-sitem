# cart/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart, CartItem
from products.models import Product
from django.contrib import messages

# Kullanıcıya ait sepeti bulan yardımcı fonksiyon
def get_user_cart(request):
    user = request.user
    if user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=user)
        return cart
    else:
        # Kullanıcı giriş yapmamışsa session'dan sepeti yönetir
        cart_id = request.session.get('cart_id')
        if cart_id:
            try:
                # Session'daki sepet var mı kontrol et
                cart = Cart.objects.get(id=cart_id)
            except Cart.DoesNotExist:
                # Yoksa yeni bir sepet oluştur ve session'a kaydet
                cart = Cart.objects.create()
                request.session['cart_id'] = cart.id
        else:
            # Session'da cart_id yoksa yeni bir sepet oluştur
            cart = Cart.objects.create()
            request.session['cart_id'] = cart.id
        return cart


def cart_detail(request):
    cart = get_user_cart(request)
    context = {'cart': cart}
    return render(request, 'cart/cart_detail.html', context)

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = get_user_cart(request)
    
    quantity = 1
    if request.method == 'POST':
        try:
            quantity = int(request.POST.get('quantity', 1))
            if quantity < 1:
                quantity = 1
        except (ValueError, TypeError):
            quantity = 1

    try:
        cart_item = CartItem.objects.get(cart=cart, product=product)
        current_cart_quantity = cart_item.quantity
    except CartItem.DoesNotExist:
        cart_item = None
        current_cart_quantity = 0

    if (current_cart_quantity + quantity) > product.stock:
        messages.error(request, f'"{product.name}" için yeterli stok yok. Sepetinizde zaten {current_cart_quantity} adet var. Mevcut stok: {product.stock} adet.')
        return redirect('products:product_detail', pk=product.id)
    
    if cart_item:
        cart_item.quantity += quantity
        cart_item.save()
    else:
        CartItem.objects.create(cart=cart, product=product, quantity=quantity)
    
    # Mevcut mesajları kontrol et ve yalnızca bir tane ekle
    # Mesajlar varsa (örneğin aynı sayfada başka bir işlemden gelen mesaj) 
    # yeni mesaj ekleme
    existing_messages = list(messages.get_messages(request))
    if not existing_messages:
        messages.success(request, f'"{product.name}" sepete {quantity} adet eklendi.')
        
    return redirect('cart:cart_detail')
    

def remove_from_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.user.is_authenticated:
        # Oturum açmış kullanıcı için sepeti user'a göre bul
        cart = get_object_or_404(Cart, user=request.user)
    else:
        # Oturum açmamış kullanıcı için sepeti session_key'e göre bul
        # Bu durumda Cart modelinizde session_key alanı olmalı
        # Eğer bu alan yoksa, burası hata verecektir
        cart = get_object_or_404(Cart, session_key=request.session.session_key)

    try:
        cart_item = CartItem.objects.get(cart=cart, product=product)
        cart_item.delete()
    except CartItem.DoesNotExist:
        pass

    return redirect('cart:cart_detail')

def update_cart(request, product_id):
    if request.method == 'POST':
        cart = get_user_cart(request)
        product = get_object_or_404(Product, pk=product_id)
        
        try:
            quantity = int(request.POST.get('quantity', 0))
            cart_item = CartItem.objects.get(cart=cart, product=product)
            
            if quantity > 0:
                if quantity <= product.stock:
                    cart_item.quantity = quantity
                    cart_item.save()
                    messages.success(request, f'"{product.name}" için sepet miktarı güncellendi.')
                else:
                    messages.error(request, f'"{product.name}" için yeterli stok yok. Mevcut stok: {product.stock} adet.')
            else:
                cart_item.delete()
                messages.success(request, f'"{product.name}" sepetinizden kaldırıldı.')
        except (ValueError, TypeError, CartItem.DoesNotExist):
            messages.error(request, 'Sepet güncellenirken bir sorun oluştu.')
            
    return redirect('cart:cart_detail')