from urllib import request
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# model for a score request
class ScoreRequest(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)        
    upvotes = models.IntegerField(default=0)
    like_list = models.ManyToManyField(User, related_name='like_list', default=None, blank=True)
    video_link = models.URLField(max_length=1024, null=True, blank=True)
    link  = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.title