from typing import Dict, List
from django.db import models

# Create your models here.


class StudentOverview(models.Model):
    std_id = models.CharField(max_length=255,null=False,unique=True)
    cour_id = models.CharField(max_length=255,null=True,unique=True)
    completed =models.IntegerField(default=0)
    progress = models.JSONField(default = dict)
    doe = models.DateField(auto_now=True)
    doc = models.DateField(null=True)

class sdtSkils (models.Model):
    std_id = models.CharField(max_length=255,null=False,unique=True)
    skilset = models.JSONField()
    
class skilsNcourse (models.Model):
    std_id = models.CharField(max_length=255,null=False,unique=True,primary_key=True)
    skilset = models.JSONField(default=list)
    courses = models.JSONField(default=list)

class StdOverview(models.Model):
    id = models.CharField(max_length=255,primary_key=True)
    std_id = models.CharField(max_length=255,null=False)
    cour_id = models.CharField(max_length=255,null=True)
    thr_id = models.CharField(max_length=255,null=True)
    cour_name = models.CharField(max_length=255,null=True)
    completed =models.IntegerField(default=0)
    progress = models.JSONField(default = dict)
    doe = models.DateField(auto_now_add=True)
    doc = models.DateField(null=True)

class completed(models.Model):
    stud_id = models.CharField(max_length=255)
    course_id = models.CharField(max_length=255)
    completed_weeks = models.JSONField(default = list)
    completed_content = models.JSONField(default = list)