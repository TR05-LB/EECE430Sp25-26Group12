from django import forms
from .models import VolleyballPlayer

class VolleyballPlayerForm(forms.ModelForm):
    class Meta:
        model = VolleyballPlayer
        fields = ['name', 'date_joined', 'position', 'salary', 'contact_person']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter player name'}),
            'date_joined': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter salary'}),
            'contact_person': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter contact person'}),
        }