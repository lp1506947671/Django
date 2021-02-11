from django.db import models

# Create your models here.
"""
id:auto
title:Char
state:Boolean
pub_date:date
price:decimal
publish:char

"""


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    state = models.BooleanField()
    pub_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publish = models.CharField(max_length=32)
