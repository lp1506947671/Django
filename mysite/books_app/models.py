from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    email = models.EmailField(blank=True)
    tel = models.CharField(max_length=32, blank=True)


class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(decimal_places=2, max_digits=8)
