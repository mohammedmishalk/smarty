from django.db import models

# Create your models here.
class userprofile(models.Model):
    username = models.CharField(max_length=255,null=False,unique=True,primary_key=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    address= models.CharField(max_length=500,null= True)
    DOB = models.DateField(null=True)
    ac_type =models.BooleanField()
    img = models.ImageField(null=True, blank=True, upload_to="images/")


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
    def __str__(self):
        return self.username

class Quality(models.Model):
    username = models.CharField(max_length=255,null=False,unique=True,primary_key=True)
    domain = models.CharField(max_length=50)
    bio = models.CharField(max_length=255)
    qu = models.CharField(max_length=1000)
    ex = models.CharField(max_length=1000)
    def __str__(self):
        return self.username