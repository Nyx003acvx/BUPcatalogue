from django.db import models
import datetime
# Create your models here.


class Landing(models.Model):
    image = models.ImageField(upload_to='uploads/flowers/', null = True, default='', blank= True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500, null=True, default='', blank = True)
    def __str__(self):
        return self.name

class Flower(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500, null=True, default='', blank = True)
    image = models.ImageField(upload_to='uploads/flowers/', null = True, default='', blank= True)
    
    def __str__(self):
        return self.name
