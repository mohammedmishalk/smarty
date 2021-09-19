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