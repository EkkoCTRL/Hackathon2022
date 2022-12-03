from django.db import models

# Create your models here.
class disaster(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

class content(models.Model):
    city = models.CharField(max_length=200)
    description = models.TextField()
    event = models.ForeignKey(disaster, on_delete=models.CASCADE)