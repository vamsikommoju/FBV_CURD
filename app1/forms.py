from django import forms
from app1.models import *

class Personsform(forms.ModelForm):
    class Meta:
        model = Persons
        fields = '__all__'
        
