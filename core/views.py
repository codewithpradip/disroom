from django.shortcuts import render
from room.models import Room,Topic
from django.db.models import Q

# Create your views here.
def home_view(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    topics = Topic.objects.all()
    room_count = rooms.count()
    context = {'rooms': rooms, 'room_count': room_count, 'topics': topics}
    return render(request, 'core/home.html', context)
