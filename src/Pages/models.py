from django.db import models

# Create your models here.

# class {model}(models.Model)
class User(models.Model):
    firstname = models.CharField(max_length=50)
    surname   = models.CharField(max_length=50)
    email     = models.EmailField()
    password  = models.CharField(max_length=100)

class FileStore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fileName  = models.CharField(max_length=100)

class LearningPage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pageOneComplete = models.BooleanField()
