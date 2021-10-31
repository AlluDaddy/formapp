from django.db import models
import os

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=20)
    reg = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    branch = models.CharField(max_length=20,default=" ")
    email = models.EmailField(max_length=20,default=" ")
    image = models.ImageField(upload_to=('media/images/'), blank=True, null=True)

    
    def __str__(self):
        return self.reg

