from django.db import models

# Create your models here.

class Worker(models.Model):

    name = models.CharField(max_length=150)
    age = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)

    class Meta:
        ordering = ['name']