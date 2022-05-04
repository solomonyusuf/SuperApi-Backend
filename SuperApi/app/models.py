"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Contact(models.Model):
    fullname= models.CharField(max_length=225)
    phoneNumber= models.CharField(max_length=225)
    email= models.CharField(max_length=225)
    message=models.CharField(max_length=225)

class Post(models.Model):
    image=models.ImageField(null=True)
    title=models.CharField(max_length=225)
    body=models.CharField(max_length=5000)
    date=models.DateTimeField()

class Sermon(models.Model):
    image=models.ImageField(null=True)
    name=models.CharField(max_length=225,null=True)
    artist=models.CharField(max_length=225,null=True)
    audio=models.FileField()
    date=models.DateTimeField()

class Video(models.Model):
    image=models.ImageField(null=True)
    video=models.FileField()
    name=models.CharField(max_length=225,null=True)
    artist=models.CharField(max_length=225,null=True)
    date=models.DateTimeField()