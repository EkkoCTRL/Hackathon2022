from django.db import models

# Create your models here.
class Disaster(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    

    def __str__(self):
        return self.name

class Content(models.Model):
    city = models.CharField(max_length=200)
    description = models.TextField()
    event = models.ForeignKey(Disaster, on_delete=models.CASCADE)
    checks = models.BooleanField(default=False)

    def __str__(self):
        return self.city+ '-' + self.event.name                        