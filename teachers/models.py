from os import SEEK_CUR, name
from django.db import models

# Create your models here.
class contact(models.Model):
    username = models.CharField(max_length=255,null=False,unique=True,primary_key=True)
    facebook=models.CharField(max_length=500)
    instagram=models.CharField(max_length=500)
    twitter=models.CharField(max_length=500)
    linked_in=models.CharField(max_length=500)
    youtube=models.CharField(max_length=500)
    github=models.CharField(max_length=500)
    gitlab=models.CharField(max_length=500)
    website=models.CharField(max_length=500)


class Quality(models.Model):
    username = models.CharField(max_length=255,null=False,unique=True,primary_key=True)
    domain = models.CharField(max_length=50)
    bio = models.CharField(max_length=255)
    qu = models.CharField(max_length=1000)
    ex = models.CharField(max_length=1000)

class course(models.Model):
    course_id=models.CharField(max_length=255,null=False,unique=True,primary_key=True)
    techer_id=models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    desciptions = models.CharField(max_length=5000)
    week = models.IntegerField(default=0)
    unit = models.IntegerField(default=0)
    enroled = models.IntegerField(default=0)
    time = models.CharField(max_length=20,null=False)
    rating = models.IntegerField(default=0)

"""

class assignments(models.Model):
    name= models.CharField(max_length=100,unique=True, null=False, primary_key= True)
    file = models.FileField(upload_to='assignments/')

class exam (models.Model):
    name = models.CharField(max_length=100,unique=True, null=False, primary_key= True)
    question = models.CharField(max_length=1000)
    options = models.CharField(max_length=1000)
    answer= models.CharField(max_length=255)

class project (models.Model):
    name =models.CharField(max_length=100,unique=True, null=False, primary_key= True)
    file = models.FileField(upload_to='projects/')"""