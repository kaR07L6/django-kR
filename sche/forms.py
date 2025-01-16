from django import forms
from .models import Sche


class ScheForm(forms.ModelForm):
    class Meta:
        model = Sche
        fields = ["title", "date", "description"]
