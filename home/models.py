from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=15)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    phone = models.IntegerField(default=11)
    file = models.FileField()

class Product(models.Model):
    pass 

class Car(models.Model):
    car_name = models.CharField(max_length=50)
    speed = models.IntegerField(default=80)
    car_model = models.CharField(max_length=100, default='SUV')

class Honda(models.Model):
    bike_name = models.CharField(max_length=20)
    bike_model = models.CharField(max_length=100)
    speed = models.IntegerField(default=100)