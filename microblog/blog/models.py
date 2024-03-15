from django.db import models

# Create your models here.
class Blog(models.Model):
    # id
    content = models.CharField(max_length=200)
    date_posted = models.DateTimeField(auto_now_add=True)

