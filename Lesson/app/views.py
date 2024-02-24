from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact


def index(request):
    contacts = Contact.objects.all()
    return render(
        request,
        'main/index.html',
        {'data': contacts, 'title': 'Contacts list'}
    )

def addContact():
    pass