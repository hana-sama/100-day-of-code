from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=225)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    upload = models.FileField(null=True, blank=True, upload_to='uploads/%Y/%m/%d/')
    title_tag = models.CharField(max_length=255, default="Welcome to Blogsinzzz")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title + '|' + str(self.author)
    
    def get_absolute_url(self):
        # return reverse("article_detail", args={str(self.id)})
        return reverse('home')
