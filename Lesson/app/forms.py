from .models import Contact
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "last_name", "number", "photo"]
        widgets = {
            "name" : forms.TextInput(attrs={"class" : "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "number": forms.TextInput(attrs={"class": "form-control"}),
            "photo" : forms.FileInput()
        }