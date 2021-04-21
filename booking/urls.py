from django.urls import path

from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.list_of_rooms, name="all_rooms")
]