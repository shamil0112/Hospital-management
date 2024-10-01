from django import forms

from .models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        
        widgets = {
            'booking_data' : DateInput(),
        }
        
        labels = {
            'p_name' : "Patient Name : ",
            'p_phone' : "Patient phone :",
            'p_email' : "Patient email :",
            'doc_name' : "Docter Name :",
            'booking_data' : "Booking Date : ",
        }