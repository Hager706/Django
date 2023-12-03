from django.shortcuts import render
from .models import Ritzypro
from .models import Chifon
from .models import Woven
from .models import Lycra
from .models import Linen
from .models import Home
from .models import All
from .models import Ctag

# Create your views here.
def js2(request):
   Alls = All.objects.all()
   return render(request, 'home/js2.html',{'Alls': Alls})


def ritzyall(request):
    Ctags = Ctag.objects.all()
    return render(request,'home/ritzyall.html',{'Ctags': Ctags})

def contact(request):
    return render(request,'home/contact.html')

def ourstory(request):
    return render(request,'home/ourstory.html')

def ritzychifon(request):
    Chifons = Chifon.objects.all()
    return render(request, 'home/ritzychifon.html',{'Chifons': Chifons})

def ritzywoven(request):
    Wovens = Woven.objects.all()
    return render(request, 'home/ritzywoven.html',{'Wovens': Wovens})

def ritzypro(request):   
    Ritzypros = Ritzypro.objects.all()
    return render(request, 'home/ritzypro.html',{'Ritzypros': Ritzypros})

def ritzylycra(request):   
    Lycras = Lycra.objects.all()
    return render(request, 'home/ritzylycra.html',{'Lycras': Lycras})

def ritzylinen(request):   
    Linens = Linen.objects.all()
    return render(request, 'home/ritzylinen.html',{'Linens': Linens})

def sale(request):
    return render(request, 'home/sale.html')

def check(request):
    return render(request, 'home/check.html')

