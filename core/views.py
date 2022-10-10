from django.shortcuts import render
from room.models import Room,Topic

# Create your views here.
def home_view(request):
    rooms = Room.objects.all()
    topics = Topic.objects.all()
    room_count = rooms.count()
    context = {'rooms': rooms, 'room_count': room_count, 'topics': topics}
    return render(request, 'core/home.html', context)
