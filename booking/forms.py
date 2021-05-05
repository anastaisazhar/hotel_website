from django import forms
from django.forms import ModelForm
from .models import Booking
from .models import Room
import datetime


class BookingForm(forms.Form):

    def validate_checkin_date(self):
        if self.checkin_date > datetime.date.today:
            return self
        else:
            raise ValidationError('This date has already passed.')

    def validate_checkout_date(self):
        date1 = self.checkin_date
        date2 = self.checkout_date
        if date1 < date2:
            return self
        else:
            raise ValidationError("The check-in date can't be sooner than the check-out date.")


    small_size = 's'
    medium_size = 'm'
    large_size = 'l'

    room_types = [
        (small_size, 'small'),
        (medium_size, 'medium'),
        (large_size, 'large'),
    ]

    first_name = forms.CharField(label='First Name') 
    second_name = forms.CharField(label='Second Name')
    email = forms.EmailField()
    room_type = forms.ChoiceField(label='Room Type', choices = room_types, initial=small_size)
    checkin_date = forms.DateField(labelx='Check-in Date', initial=datetime.date.today, validators=[validate_checkin_date])
    checkout_date = forms.DateField(label='Check-out Date', initial=datetime.date.today,validators=validate_checkout_date)