from django.db import models

# Create your models here.
class Gallery(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=100)