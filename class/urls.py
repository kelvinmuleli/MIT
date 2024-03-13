from django.urls import path
from . import views

urlpatterns = [

    path('', views.home),
    path('about/', views.about),
    path('contact/', views.contacts),
    path('services/',views.services),
    path('index/', views.index),
    path('iportfolio/', views.iportfolio),
    path('students/', views.student),
    path('teachers/', views.teachers),
    path('insert_students/', views.insert_students)


]