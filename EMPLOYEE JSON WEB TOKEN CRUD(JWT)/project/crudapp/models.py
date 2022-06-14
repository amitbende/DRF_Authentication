from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    salary = models.FloatField()
    address = models.CharField(max_length=50)
    picture = models.ImageField(upload_to = 'PICTURE', blank = True)