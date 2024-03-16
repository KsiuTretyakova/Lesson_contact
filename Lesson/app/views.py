from django.shortcuts import render, redirect
from .models import Contact
from django.http import HttpResponse
from .forms import ContactForm


def index(request):
    contacts = Contact.objects.all()
    print(contacts)
    return render(request, "index.html", {'data' : contacts, 'title' : 'Contact list'})



def addContact(request):
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(index)
        else:
            error = "ERROR"
    form = ContactForm()
    return render(request, 'index.html', {'form':form, 'error':error})

def delete(request, id, name):
    delete = Contact.objects.get(id=id)
    delete.delete()
    return redirect(index)