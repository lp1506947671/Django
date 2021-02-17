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


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    authorDetail = models.OneToOneField(to="AuthorDetail", to_field='id', on_delete=models.CASCADE)


class AuthorDetail(models.Model):
    id = models.AutoField(primary_key=True)
    birthday = models.DateField()
    telephone = models.BigIntegerField()
    addr = models.CharField(max_length=64)


class Publish(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    email = models.EmailField()


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    state = models.BooleanField()
    pub_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    # 与Publish建立一对多的关系,外键字段建立在多的一方
    publish = models.ForeignKey(to="Publish", to_field="id", on_delete=models.CASCADE)
    # 与Author表建立多对多的关系,ManyToManyField可以建在两个模型中的任意一个，自动创建第三张表
    authors = models.ManyToManyField(to='Author')
