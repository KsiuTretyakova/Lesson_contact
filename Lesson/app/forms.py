from .models import Contact
from django import forms

class ContacForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "surname", "phone_number", "photo"]
        widgets = {
            "name" : forms.TextInput(attrs = {"class" : "form-controle"}),
            "surname" : forms.TextInput(attrs = {"class" : "form-controle"}),
            "phone_number" : forms.TextInput(attrs = {"class" : "form-controle"}),
            "photo" : forms.FileInput()
        }