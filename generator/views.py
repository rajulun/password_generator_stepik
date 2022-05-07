from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLQPRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    lenght = int(request.GET.get('lenght', 12))
    thepassword = ''
    for i in range(lenght):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})

def description(request):
    return render(request, 'generator/description.html')