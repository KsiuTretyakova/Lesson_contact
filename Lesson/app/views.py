from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

from .forms import ContactForm
from .models import Contact


def index(request):
    contacts = Contact.objects.all()
    return render(
        request,
        'main/index.html',
        {'data': contacts, 'title': 'Contacts list', 'form': ContactForm()}
    )

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
    return render(request, 'main/index.html', {'form':form, 'error':error})


def deleteContact(request):
    error = ""
    if request.method == "POST":
        try:
            object = Contact.objects.get(phone_number=request.POST.__getitem__("phone_number"))
            object.delete()
        except:
            return index(request)

    return index(request)


def editContact(request):
    error = ""
    if request.method == "POST":
        try:
            object = Contact.objects.get(phone_number=request.POST.__getitem__("phone_number"))
            object.delete()
        except:
            return index(request)
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(index)
        else:
            error = "ERROR"
    return index(request)
    