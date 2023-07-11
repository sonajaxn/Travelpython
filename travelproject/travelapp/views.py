
from django.shortcuts import render
from django.http import HttpResponse
from .models import place
from .models import panel


# Create your views here.
def demo(request):
   obj=place.objects.all()
   panels=panel.objects.all()
   print("panels",panels)
   return render(request,"index.html",{'result':obj,'panel':panels})


# def demo_panel(request):
   
#    panels=panel.objects.all()
#    return render(request,"index.html",{'res':panels})

