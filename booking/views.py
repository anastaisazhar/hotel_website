from django.shortcuts import render

from .models import Room

# Create your views here.

def list_of_rooms(request):
    room_types_list = Room.objects.all()
    return render(request, 'booking/list_of_rooms.html')