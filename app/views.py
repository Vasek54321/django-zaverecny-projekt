from django.shortcuts import render, get_object_or_404
from .models import Auto, Majitel, Vyrobce

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

def VyrobceListView(request):
    vyrobci = Vyrobce.objects.all()
    context = {
        'vyrobci': vyrobci
    }
    return render(request, 'app/VyrobceListView.html', context)



def AutoDetailView(request, id_auto):
    auto = get_object_or_404(Auto, pk=id_auto)
    return render(request, 'app/AutoDetailView.html', {'auto': auto})

def MajitelDetailView(request, id_majitel):
    majitel = get_object_or_404(Majitel, pk=id_majitel)
    return render(request, 'app/MajitelDetailView.html', {'majitel': majitel})

def VyrobceDetailView(request, id_vyrobce):
    vyrobce = get_object_or_404(Vyrobce, pk=id_vyrobce)
    return render(request, 'app/VyrobceDetailView.html', {'vyrobce': vyrobce})
