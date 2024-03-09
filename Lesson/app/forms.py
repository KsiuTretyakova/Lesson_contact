from .models import Contact
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "surname", "phone_number", "photo"]
        widgets = {
            "name" : forms.TextInput(attrs={"class" : "form-control"}),
            "surname" : forms.TextInput(attrs={"class" : "form-control"}),
            "phone_number" : forms.TextInput(attrs={"class" : "form-control"}),
            "photo" : forms.FileInput()
        }
