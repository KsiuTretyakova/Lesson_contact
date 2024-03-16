from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
# Create your views here.
from django.http import HttpResponse


def index(request):
    contacts = Contact.objects.all()
    print(contacts)
    return render(request, "index.html", {'data': contacts, 'form': ContactForm()})


def addContact(request):
    error = ""
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(index)
        else:
            error = "ERROR"
        form = ContactForm()
        return (request, "main/index.html",
                {'form': form, 'error': error})


def delete(request, id, name):
    delete = Contact.objects.get(id=id)
    delete.delete()
    return redirect(index)
