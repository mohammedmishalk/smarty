from typing import Dict, List
from django.db import models

class course(models.Model):
    course_id=models.CharField(max_length=255,null=False,unique=True,primary_key=True)
    teacher_id=models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    discriptions = models.CharField(max_length=5000,null=True)
    week = models.IntegerField(default=0)
    enroled = models.IntegerField(default=0)
    completed = models.IntegerField(default=0)
    time = models.CharField(max_length=20,null=False)
    rating = models.IntegerField(default=0)
    skils = models.JSONField()
    Questions = models.JSONField(default=dict)
    created_date = models.DateField(auto_now_add=True,null=True)

class regularclass(models.Model):
    class_id = models.CharField(max_length=255,null=False,unique=True,primary_key=True)
    teacher_id=models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    classDiv = models.CharField(max_length=20)
    students =models.ImageField()
    enroled = models.IntegerField(default=0)
    hash = models.CharField(max_length=32,default=0)
    created_date = models.DateField(auto_now_add=True,null=True)


class weeks(models.Model):
    course_id = models.CharField(max_length=255,null=False,unique=True,primary_key=True)
    week= models.JSONField(default=list)
    
class contentOrder(models.Model):
    week = models.CharField(max_length=255,null=False,unique=True,primary_key=True)
    order = models.JSONField()

class text_content (models.Model):
    id=models.CharField(max_length=15,null=False,unique=True,primary_key=True)
    course_id= models.CharField(max_length=15,null=False,default=str)
    name = models.CharField(max_length=30,null=False)
    content =models.JSONField()
    reference = models.CharField(max_length=255)
    time = models.IntegerField()
 

class img_content (models.Model):
    id = models.CharField(max_length=15,null=False,unique=True,primary_key=True)
    course_id= models.CharField(max_length=15,null=False,default=str)
    name = models.CharField(max_length=30,null=False)
    img = models.ImageField(upload_to='content/')
    text = models.CharField(max_length=1000,null=False)
    Reference = models.CharField(max_length=255)
    time = models.IntegerField()

class Videos(models.Model):
    course_id= models.CharField(max_length=15,null=False,default=str)
    id = models.CharField(max_length=100,unique=True, null=False, primary_key= True)
    name = models.CharField(max_length=30,null=False)
    video = models.FileField(upload_to='videos/')
    time = models.IntegerField()
