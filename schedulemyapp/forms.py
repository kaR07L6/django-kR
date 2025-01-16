from django import forms
from .models import Director, Movie, Log
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter event name'}),
        }

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ("name",)

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ("title", "watch_date", "director")

class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = ("movie", "text")
