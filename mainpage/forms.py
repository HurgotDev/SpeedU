from django import forms

from .models import Departament, City

class RegisterForm(forms.Form):
    DEPARTAMENT_CHOICES  = [('', '-- Elija departamento --'),] + [(d.id, d.name) for d in Departament.objects.all()]    
    CITIES_CHOICES = [(c.id, c.name) for c in City.objects.all()]

    name = forms.CharField(label='Nombres', max_length=100, required=True)
    lastname = forms.CharField(label='Apellidos', max_length=100, required=True)
    email = forms.EmailField(label='Correo Electrónico', required=True)
    phone = forms.CharField(label='Teléfono - Celular', required=True)    
    departament = forms.ChoiceField(choices=DEPARTAMENT_CHOICES)
    city = forms.ChoiceField(choices=CITIES_CHOICES)
    institution = forms.CharField(label='Institución', required=True)
    terms = forms.BooleanField(label='Acepto el acuerdo general del servicio', required=True)


class NewsletterForm(forms.Form):
    email = forms.EmailInput()