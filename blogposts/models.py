from django.db import models


# Create your models here.

class NewPost(models.Model):
    title = models.CharField(max_length=100)
    post_image = models.ImageField(upload_to='images/')
    overview = models.TextField()
    author = models.CharField(max_length=50)
    categories = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    reading_time = models.CharField(max_length=50)


class LatestPost(models.Model):
    post_image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    timestamp = models.DateTimeField()


class Popular(models.Model):
    post_image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
