from django.db import models

class Room(models.Model):
    small_size = 's'
    medium_size = 'm'
    large_size = 'l'

    room_types = [
        (small_size, 'small'),
        (medium_size, 'medium'),
        (large_size, 'large'),
    ]

    number = models.CharField(default='',max_length=100)
    room_type = models.CharField(max_length=1,choices=room_types,default=small_size) 
    view = models.BooleanField()
    price = models.IntegerField(default=0)

    def __str__(self):
        return f'Room {self.number}, {self.room_type}' 

class Booking(models.Model):
    room = models.ForeignKey(Room,on_delete=models.CASCADE,related_name='all_bookings')
    first_name = models.CharField(default='',max_length=100)
    second_name = models.CharField(default='',max_length=100)
    email = models.CharField(default='',max_length=100)
    checkin_date = models.DateTimeField('check-in date')
    checkout_date = models.DateTimeField('check-out date')
