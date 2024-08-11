from django import forms
from .models import Travel


class TravelForm(forms.ModelForm):
    class Meta:
        model = Travel
        fields = ('title', 'photo', 'description', 'popular_place', 'price', 'author')
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'autocomplete':'off', 'type': 'hidden'}),
        }