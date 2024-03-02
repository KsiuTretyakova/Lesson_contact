from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact
from .forms import ContacForm


def index(request):
    contacts = Contact.objects.all()
    return render(
        request,
        'main/index.html',
        {'data': contacts, 'title': 'Contacts list'}
    )

def addContact(request):
    error =  ""
    if request.method == "POST":
        form = ContacForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(index)
        else:
            error = "ERROR"
    form = ContacForm()
    return(request, 'main/index.html',
           {'form': form, 'error': error})
