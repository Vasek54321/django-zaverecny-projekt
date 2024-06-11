from django.shortcuts import render
from .models import Auto, Majitel

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def AutoListView(request):
    auta = Auto.objects.all()
    context = {
        'auta': auta
    }
    return render(request, 'app/AutoListView.html', context)

def MajitelListView(request):
    majitele = Majitel.objects.all()
    context = {
        'majitele': majitele
    }
    return render(request, 'app/MajitelListView.html', context)