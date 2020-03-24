from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.

def login(request: HttpRequest):
    return render(request, 'shops/auth/../templates/login.html')


def register(request: HttpRequest):
    pass


def home(request: HttpRequest):
    pass