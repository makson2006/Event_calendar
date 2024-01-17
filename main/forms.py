from django import forms
from django.forms import ModelForm
from .models import Venue
from .models import Event

# Create a venue form
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email_address')
        labels = {
            'name':'',
            'address':'',
            'zip_code':'',
            'phone': '',
            'web': '',
            'email_address':''
        }


        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
            'address': forms.TextInput(attrs={'class':'form-control','placeholder':'address'}),
            'zip_code' : forms.TextInput(attrs={'class':'form-control','placeholder':'zip code'}),
            'phone': forms.TextInput(attrs={'class':'form-control','placeholder':'phone'}),
            'web': forms.TextInput(attrs={'class':'form-control','placeholder':'Web Site'}),
            'email_address': forms.EmailInput(attrs={'class':'form-control','placeholder':'email address'}),
        }

# Create e Event form

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'event_date', 'venue', 'manager', 'description', 'attendees')
        labels = {
            'name':'',
            'event_date':'event_date YYYY-MM-DD HH-MM-SS:',
            'venue':'Venue',
            'manager': '',
            'description': '',
            'attendees':'attendees'
        }


        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
            'event_date': forms.TextInput(attrs={'class':'form-control','placeholder':'event_date'}),
            # 'venue' : forms.TextInput(attrs={'class':'form-control','placeholder':'venue'}),
            'manager': forms.TextInput(attrs={'class':'form-control','placeholder':'manager'}),
            'description': forms.TextInput(attrs={'class':'form-control','placeholder':'description'}),
            # 'attendees': forms.EmailInput(attrs={'class':'form-control','placeholder':'attendees'}),
        }