from django.db import models
import datetime


# Create your models here.


from django.db import models

class FlowerFeed(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500, null=True, default='', blank = True)
    image = models.ImageField(upload_to='uploads/flowers/', null = False, default='', blank= False)
    
    def __str__(self):
        return self.name
