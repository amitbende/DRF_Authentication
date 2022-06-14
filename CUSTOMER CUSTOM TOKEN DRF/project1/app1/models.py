from itertools import product
from unicodedata import name
from django.db import models

# Create your models here.
class Customer(models.Model):
    def PICTURE(instance, filename):
        return '/'.join(['images', str(instance, name), filename])

    cid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    product = models.CharField(max_length=50)
    price = models.FloatField()
    shop = models.CharField(max_length=50)
    picture = models.ImageField(upload_to = 'PICTURE', blank = True)
