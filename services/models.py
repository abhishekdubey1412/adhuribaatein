from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=55)
    password = models.IntegerField()

class Post(models.Model):
    user = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    content = models.TextField()
    pub_date = models.DateTimeField()

class Stroy(models.Model):
    user = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    content = models.TextField()
    pub_date = models.DateTimeField()