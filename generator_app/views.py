from django.shortcuts import render
from django.http import HttpResponse
from random import choice

# Create your views here.

def home(request):
    return render(request, 'generator_app/home.html')

def password(request):
    the_password = ""
    characters = list("abcdefghigklmnopqrstuvwxyz")
    length = int(request.GET.get("length", 12))
    if request.GET.get("uppercase"):
        characters.extend(list("ABCDEFGHIGKLMNOPQRSTUVWXYZ"))
    if request.GET.get("numbers"):
        characters.extend(list("0123456789"))
    if request.GET.get("special"):
        characters.extend(list("!@#$%^&*()-\_+=/?"))
    for i in range(length):
        the_password += choice(characters)
    return render(request, 'generator_app/password.html', {"password": the_password})

def about_me(request):
    return render(request, 'generator_app/about_me.html')