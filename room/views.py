from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm

# Create your views here.
def room_detail_view(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'room/room_detail.html', context)

def create_room_view(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'room/create_room_form.html', context)

def update_room_view(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'room/create_room_form.html', context)


def delete_room_view(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'room/delete_room.html', {'obj': room})
