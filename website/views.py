from django.shortcuts import render
from django.http import HttpResponse
from .models import destination
# from.models import Blog

def home(request):
    return render(request,"index.html")


def about(request):
    return render(request,"about.html")

def projectstable(request):
    return render(request,"projectstable.html")


def contact(request):
    return render(request,"contact.html")


def resume(request):
    return render(request,"resume.html")


def image(request):

    obj=destination()

    obj.img="areef.jpeg"
    return render(request,"imageframe.html",{"obj":obj})






# Create your views here.
