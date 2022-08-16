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
    likes = models.ManyToManyField(User, related_name='likes')
    video_link = models.URLField(max_length=1024, null=True, blank=True)
    link  = models.URLField(max_length=1024, null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='requests', on_delete=models.CASCADE, default=User )


    def __str__(self):
        return self.title

