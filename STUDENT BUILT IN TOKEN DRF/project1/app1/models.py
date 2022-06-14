from unicodedata import name
from django.db import models

# Create your models here.
class Student(models.Model):
    def PICTURE(instance, filename):
        return '/'.join(['images', str(instance, name), filename])

    roll_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    classs = models.CharField(max_length=50)
    section = models.CharField(max_length=50)
    marks = models.FloatField()
    address = models.CharField(max_length=50)
    picture = models.ImageField(upload_to = 'PICTURE', blank = True)

