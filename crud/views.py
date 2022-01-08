from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('<h1> Wellcome !!!<br><a href="myapp">Myapp</a><br><a href="/admin">ADMIN</a></h1>')
