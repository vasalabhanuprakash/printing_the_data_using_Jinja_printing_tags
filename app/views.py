from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def dhoni(request):
    d={'name':'Ms.Dhoni','age':42}

    return render(request, 'dhoni.html',d)