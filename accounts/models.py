from django.db import models

class UserProfile(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)
    password = models.CharField(max_length=32)

