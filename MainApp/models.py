from django.db import models


# Create your models here.
class Color(models.Model):
    name = models.CharField(max_length=32)

class Item(models.Model):
    name  = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    count = models.PositiveIntegerField() 
    description = models.CharField(max_length=100,default="базовое описание")
    colors = models.ManyToManyField(to= Color)

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title