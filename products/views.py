# products/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

# Ürün listesi ve detay view'leri
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    # Sıralama mantığını buraya ekleyin
    sort_by = request.GET.get('sort')

    if sort_by == 'price_asc':
        products = products.order_by('price')
    elif sort_by == 'price_desc':
        products = products.order_by('-price')

    return render(request, 'products/product_list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'products/product_detail.html', context)

# Kullanıcı kayıt view'i
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Hesabınız başarıyla oluşturuldu.')
            return redirect('product_list')
    else:
        form = UserCreationForm()
    return render(request, 'products/register.html', {'form': form})