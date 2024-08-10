from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'   #dictionary can be converted to json but not python objects
    ]
    return Response(routes)



@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all() #objects can not be converted(serialize file) to the json file that's why we need serializers
    serializer = RoomSerializer(rooms, many=True) # many means that we r serializing many objects not a 1-3 objects 
    return Response(serializer.data)

@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    serialize = RoomSerializer(room, many=False)
    return Response(serialize.data)

