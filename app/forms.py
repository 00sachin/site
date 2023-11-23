from django import forms
from .models import Person

class MyForm(forms.ModelForm):
    class Meta:
        Model = Person
        fields = ["name", "email", "desc",]
        labels = {'name': "Name", "email": "E-mail","desc": "Say Something",}

