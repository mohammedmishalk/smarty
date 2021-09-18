from django.db import models

# Create your models here.
class userprofile(models.Model):
    username = models.CharField(max_length=255,null=False,unique=True,primary_key=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number=models.CharField(max_length=12,null=True)
    address= models.CharField(max_length=500,null= True)
    DOB = models.DateField(null=True)
    gender = models.BooleanField(null=True)
    ac_type =models.BooleanField()

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

class usernameConvart(models.Model):
    username = models.CharField(max_length=255,primary_key=True)
    new_username = models.CharField(max_length=1000)