from django.db import models

class location(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    description = models.TextField()
    img = models.ImageField(upload_to='images',blank = True)
    Category = models.CharField(max_length=200,blank=True)






