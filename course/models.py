from django.db import models

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
    skils = models.CharField(max_length=255)

class text_content (models.Model):
    id=models.CharField(max_length=8,null=False,unique=True,primary_key=True)
    name = models.CharField(max_length=30,null=False)
    content =models.CharField(max_length=1000,null=False)
    reference = models.CharField(max_length=255)
    time = models.IntegerField()
 
    

class img_content (models.Model):
    id = models.CharField(max_length=8,null=False,unique=True,primary_key=True)
    name = models.CharField(max_length=30,null=False)
    img = models.ImageField(upload_to='content/')
    text = models.CharField(max_length=1000,null=False)
    Reference = models.CharField(max_length=255)
    time = models.IntegerField()

class Videos(models.Model):
    id = models.CharField(max_length=100,unique=True, null=False, primary_key= True)
    name = models.CharField(max_length=30,null=False)
    video = models.FileField(upload_to='videos/')
    time = models.IntegerField()

    