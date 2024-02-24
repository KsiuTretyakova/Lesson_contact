from .models import Contact
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "last_name", "number", "photo"]
        wigets = {"name": forms.TextInput(attes={"class": "form-control"}),
                  "last_name": forms.TextInput(attes={"class": "form-control"}),
                  "number": forms.TextInput(attes={"class": "form-control"}),
                  "photo": forms.FileInput()
                  }
