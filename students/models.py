from typing import Dict, List
from django.db import models

# Create your models here.


class StudentOverview(models.Model):
    std_id = models.CharField(max_length=255,null=False,unique=True,primary_key=True)
    course_dtls = models.JSONField(default=dict)
    std_skils = models.JSONField(default=list) 