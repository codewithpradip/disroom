from rest_framework.decorators import api_view
from rest_framework.response import Response
from room.models import Room
from .serializers import RoomSerializer

@api_view(['GET'])
def get_rountes_view(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /apt/rooms/:pk'
    ]
    return Response(routes)

@api_view(['GET'])
def get_rooms_views(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_room_detail_views(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)
