from django.db import models
from django.contrib.auth.models import User

class cservice(models.Model):
    name=models.CharField(max_length=90)
    email=models.EmailField(max_length=90)
    subject=models.CharField(max_length=90)
    message=models.TextField()

class bookings(models.Model):
    bname=models.CharField(max_length=90)
    bemail=models.EmailField(max_length=90)
    bdtime=models.DateTimeField(max_length=90)
    bpeople=models.CharField(max_length=90)
    brequest=models.TextField()

class popular(models.Model):
    foodname=models.CharField(max_length=50)
    foodimage=models.FileField(upload_to="photo/",max_length=250,null=True,default=None)
    foodprice=models.CharField(max_length=50)
    foodmessage=models.TextField(max_length=90)

class student(models.Model):
    sname = models.CharField(max_length=90,null=True,default=None)
    total_likes=models.IntegerField(default=0)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    post = models.ForeignKey(student, on_delete=models.CASCADE)  

class atendance(models.Model):
    aname = models.CharField(max_length=90)
    atten = models.IntegerField(default=0)
