from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import MyUserCreationForm
from .models import User
from room.models import Room, Message, Topic
from django.contrib.auth.decorators import login_required
from . forms import UserForm

# Create your views here.
def user_login_view(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'User OR Password does not match.')
    context = {'page': page}
    return render(request, 'account/login_register.html', context)


def user_logout_view(request):
    logout(request)
    return redirect('home')


def user_register_view(request):
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration.')
    return render(request, 'account/login_register.html', {'form': form})

def user_profile_view(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics = Topic.objects.all()
    context = {'user': user,  'rooms': rooms, 'room_messages': room_messages, 'topics': topics}
    return render(request, 'account/user_profile.html', context)


@login_required(login_url='user_login')
def user_update_view(request):
    user = request.user
    form = UserForm(instance=user)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_profile', pk=user.id)
    context = {'form': form , 'user': user}
    return render(request, 'account/user_update.html', context)
