from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def user_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'User OR Password does not match.')
    return render(request, 'account/login_register.html')


def user_logout_view(request):
    logout(request)
    return redirect('home')
