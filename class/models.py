from django.db import models


# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=20, blank=False)
    phone = models.IntegerField()
    email = models.EmailField(blank=False)
    image = models.ImageField(upload_to='images/',blank=False,default="default.jpg")

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=30, blank=False, default="john")
    phone = models.IntegerField(blank=False, default="95")
    email = models.EmailField(blank=False, default="email@m.com")


    def __str__(self):
        return self.name
