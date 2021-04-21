from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def events_view(request, *args, **kwargs):
    return render(request, "events.html", {})

def about_view(request, *args, **kwargs):
    my_context = {  
        "title" : "This is about us",
        "my_number" : 123,
        "my_list" : [1,2,3]
    } #template context
    return render(request, "about.html", my_context)

