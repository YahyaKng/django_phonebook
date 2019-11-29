from django import forms 
from .models import Phonebook


class PhonebookForm(forms.ModelForm):
    class Meta:
        model = Phonebook
        fields = '__all__'