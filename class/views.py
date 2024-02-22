from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contacts(request):
    return render(request,'contact.html')
def services(request):
    return render(request,'services.html')
def index(request):
    return render(request, 'index.html')
def iportfolio(request):
    return render(request, 'iportfolio.html')
