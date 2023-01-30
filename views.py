from itertools import product
from django.shortcuts import render
from django.http import HttpResponse
from . models import product

# Create your views here.
def index(request):
    pro=product.objects.all
    return render(request,'index.html',{'products':pro})
def about(request):
    return HttpResponse('<h1> HELLO </h1>')
def login(request):
    return render(request,'login.html')
def signin(request):
    return render(request,'signin.html')
def catlog(request):
    return render(request,'catlog.html')