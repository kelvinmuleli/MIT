from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .models import Teacher


# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contacts(request):
    return render(request, 'contact.html')


def services(request):
    return render(request, 'services.html')


def index(request):
    return render(request, 'index.html')


def iportfolio(request):
    return render(request, 'iportfolio.html')


def student(request):
    students = Student.objects.all()
    return render(request, 'students list.html', {"students": students})


def teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers.html', {"teachers": teachers})
def insert_students(request):
    return render(request,'insert.html')