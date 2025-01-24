from django.db import models

# Create your models here.

class Student(models.Model):
    # id field django automatically adds and it is a primaray key
    
    # id = models.AutoField()
    first_name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True)
    file = models.FileField()
    
class Car(models.Model):
    car_name=models.CharField(max_length=500)
    speed = models.IntegerField(default=50)
    
    def __str__(self)->str:
        return self.car_name
    