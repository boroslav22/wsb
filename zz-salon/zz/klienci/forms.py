from django import forms 
from django.forms import ModelForm
from .models import Zwierze, Wizyty

# Create Zwierze form

class ZwierzeForm(ModelForm):
    class Meta:
        model = Zwierze
        fields = ('imie', 'phone_number', 'email', 'owner', 'city', 'year_birth', 'sex', 'gatunek', 'breed', 'comments')
        labels = {
            'imie': '', 
            'phone_number': '', 
            'email': '', 
            'owner': '', 
            'city': '', 
            'year_birth': '', 
            'sex': 'Płeć:', 
            'gatunek': 'Gatunek:', 
            'breed': '', 
            'comments': '',
        }
        widgets ={
            'owner':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Dane właściciela.'}), 
            'imie': forms.TextInput(attrs={'class':'form-control','placeholder': 'Podaj imię zwierzaka.'}), 
            'phone_number':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Numer telefonu. Do właściciela.'}), 
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Adres email. Też właściciela.'}), 
            'city':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Miejscowość'}), 
            'year_birth':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Rok urodzenia. Pupila.'}), 
            'sex':forms.Select(attrs={'class':'form-select', 'data-live-search':'true', 'placeholder': 'Płeć. Zwierzaka.'}), 
            'gatunek':forms.Select(attrs={'class':'form-select', 'placeholder': 'Gatunek.'}), 
            'breed':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Rasa.'}), 
            'comments':forms.Textarea(attrs={'class':'form-control', 'rows': '3', 'placeholder': 'Uwagi.', 'rows': '3'}),
        }


class WizytyForm(ModelForm):
    class Meta:
        model = Wizyty
        fields = ('zwierze', 'visit_date', 'visit_time',) 
        labels = {
            'zwierze': 'Imie zwierzaka',
            'visit_date': '',
            'visit_time': '',
        }
        widgets ={
            'zwierze':forms.Select(attrs={'class':'form-select', 'placeholder': 'Zwierzak.'}), 
            'visit_date':forms.DateInput(attrs={'class':'form-control datetimepicker-input', 'data-target': '#datetimepicker1'}), 
            'visit_time': forms.TextInput(attrs={'class':'form-control','placeholder': 'Godzina wizyty.'}), 
            }
