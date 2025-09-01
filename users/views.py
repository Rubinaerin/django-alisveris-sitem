# users/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse # `reverse` fonksiyonunu içe aktarmayı unutmayın
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate 
from orders.models import Order 



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hesabınız başarıyla oluşturuldu! Şimdi giriş yapabilirsiniz.')
            return redirect(reverse('users:login'))
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Başarıyla giriş yaptınız, {username}.')
                return redirect('products:product_list')
            else:
                messages.error(request, 'Kullanıcı adı veya parola hatalı.')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.info(request, "Başarıyla çıkış yaptınız.")
    return redirect('products:product_list')


@login_required
def user_profile(request):
    user_orders = Order.objects.filter(user=request.user).order_by('-created')
    context = {
        'user_orders': user_orders
    }
    return render(request, 'users/profile.html', context)