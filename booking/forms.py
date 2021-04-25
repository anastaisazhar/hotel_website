from django import forms

from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'first_name',
            'second_name',
            'email',
            'room',
            'checkin_date',
            'checkout_date'
        ]