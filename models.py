from django.db import models

# Create your models here.

small_size = 's'
medium_size = 'm'
large_size = 'l'

room_types = [
    (small_size, 'small'),
    (medium_size, 'medium'),
    (large_size, 'large'),
]

class Room(models.Model):
    number = models.CharField(default='', max_length=100)
    room_type = models.CharField(max_length=1, choices=room_types, default=small_size) 
    view = models.BooleanField(default=False)
    price = models.IntegerField(default=0)

class Booking(models.Model):
    def choose_room(self):
        for r in Room.objects.get(room_type=self.room_type):
            if r.number==59:
                return r
    
    room_type = models.CharField(max_length=1, choices=room_types, default=small_size)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='all_bookings',default=choose_room)
    first_name = models.CharField(default='', max_length=100)
    second_name = models.CharField(default='', max_length=100)
    email = models.EmailField(default='', max_length=100)
    checkin_date = models.DateField('check-in date')
    checkout_date = models.DateField('check-out date')


# room30 = Room.objects.create(number = 30, room_type = 's', view = False, price = 60)
# room31 = Room.objects.create(number = 31, room_type = 's', view = False, price = 60)
# room32 = Room.objects.create(number = 32, room_type = 's', view = False, price = 60)
# room33 = Room.objects.create(number = 33, room_type = 's', view = False, price = 60)
# room34 = Room.objects.create(number = 34, room_type = 's', view = False, price = 60)
# room35 = Room.objects.create(number = 35, room_type = 's', view = False, price = 60)
# room36 = Room.objects.create(number = 36, room_type = 's', view = True, price = 80)
# room37 = Room.objects.create(number = 37, room_type = 's', view = True, price = 80)
# room38 = Room.objects.create(number = 38, room_type = 'm', view = True, price = 550)
# room39 = Room.objects.create(number = 39, room_type = 'm', view = True, price = 550)

# room40 = Room.objects.create(number = 40, room_type = 'm', view = True, price = 550)
# room41 = Room.objects.create(number = 41, room_type = 'm', view = True, price = 550)
# room42 = Room.objects.create(number = 42, room_type = 'm', view = False, price = 450)
# room43 = Room.objects.create(number = 43, room_type = 'm', view = False, price = 450)
# room44 = Room.objects.create(number = 44, room_type = 'm', view = False, price = 450)
# room45 = Room.objects.create(number = 45, room_type = 'm', view = False, price = 450)
# room46 = Room.objects.create(number = 46, room_type = 'm', view = False, price = 450)
# room47 = Room.objects.create(number = 47, room_type = 'm', view = False, price = 450)
# room48 = Room.objects.create(number = 48, room_type = 'm', view = False, price = 450)
# room49 = Room.objects.create(number = 49, room_type = 'm', view = False, price = 450)

# room50 = Room.objects.create(number = 50, room_type = 'm', view = False, price = 450)
# room51 = Room.objects.create(number = 51, room_type = 'm', view = False, price = 450)
# room52 = Room.objects.create(number = 52, room_type = 'l', view = False, price = 850)
# room53 = Room.objects.create(number = 53, room_type = 'l', view = False, price = 850)
# room54 = Room.objects.create(number = 54, room_type = 'l', view = False, price = 850)
# room55 = Room.objects.create(number = 55, room_type = 'l', view = False, price = 850)
# room56 = Room.objects.create(number = 56, room_type = 'l', view = True, price = 1000)
# room57 = Room.objects.create(number = 57, room_type = 'l', view = True, price = 1000)
# room58 = Room.objects.create(number = 58, room_type = 'l', view = True, price = 1000)
# room59 = Room.objects.create(number = 59, room_type = 'l', view = True, price = 1000)