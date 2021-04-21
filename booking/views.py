from django.http import HttpResponse
from django.template import loader

from .models import Room

# Create your views here.

def list_of_rooms(request):
    rooms_all = Room.objects.all()
    template = loader.get_template('booking/list_of_rooms.html')
    context = {
        'rooms_all': rooms_all,
    }
    return  HttpResponse(template.render(context, request))