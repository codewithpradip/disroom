from django.shortcuts import render, redirect
from .models import Room, Message, Topic
from .forms import RoomForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.
def room_detail_view(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all()
    participants = room.participants.all()
    if request.method == 'POST':
        new_message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room_detail', pk=room.id)
    context = {'room': room, 'room_messages': room_messages, 'participants': participants}
    return render(request, 'room/room_detail.html', context)


@login_required(login_url='user_login')
def create_room_view(request):
    form = RoomForm()
    topics = Topic.objects.all()
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
        )
        return redirect('home')
        # form = RoomForm(request.POST)
        # if form.is_valid():
        #     room = form.save(commit=False)
        #     room.host = request.user
        #     form.save()
        #     return redirect('home')
    context = {'form': form, 'topics': topics}
    return render(request, 'room/create_room_form.html', context)


@login_required(login_url='user_login')
def update_room_view(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    topics = Topic.objects.all()
    if request.user != room.host:
        return HttpResponse("You are not allow here !!")
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()
        # form = RoomForm(request.POST, instance=room)
        # if form.is_valid():
        #     form.save()
        return redirect('home')
    context = {'form': form, 'topics': topics, 'room': room}
    return render(request, 'room/create_room_form.html', context)


@login_required(login_url='user_login')
def delete_room_view(request, pk):
    room = Room.objects.get(id=pk)
    if request.user != room.host:
        return HttpResponse("You are not allow here !!")
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'room/delete.html', {'obj': room})


@login_required(login_url='login_page')
def delete_message_view(request, pk):
    message = Message.objects.get(id=pk)
    if request.user != message.user:
        return HttpResponse("You are not allow here !!")

    if request.method == 'POST':
        message.delete()
        return redirect('home')
    return render(request, 'room/delete.html', {'obj': message})