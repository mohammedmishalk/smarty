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





class usernameConvart(models.Model):
    username = models.CharField(max_length=255,primary_key=True)
    new_username = models.CharField(max_length=1000)