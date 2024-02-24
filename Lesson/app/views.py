from django.shortcuts import render
from .models import Contact

# Create your views here.
from django.http import HttpResponse


def index(request):
    contacts = Contact.objects.all()
    print(contacts)
    return render(request, "index.html", {'data': contacts})


def addContact():
    pass