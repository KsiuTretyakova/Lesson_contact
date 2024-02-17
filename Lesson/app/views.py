from django.shortcuts import render
from django.http import HttpResponse


name = 'Arystarkh'

def index(request):
    return render(
        request,
        'main/index.html',
        {'nameVariable': name, 'title': 'Contacts list'}
    )