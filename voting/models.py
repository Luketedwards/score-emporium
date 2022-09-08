from urllib import request
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# model for a score request
class ScoreRequest(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)        
    upvotes = models.IntegerField(default=0)
    liked = models.ManyToManyField(User, related_name='liked', blank=True, default=None)
    video_link = models.URLField(max_length=1024, null=True, blank=True)
    link  = models.URLField(max_length=1024, null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='requests', on_delete=models.CASCADE, default=User )
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comments(models.Model):
    score = models.ForeignKey(ScoreRequest, related_name='comments', on_delete=models.CASCADE)
    content = models.CharField(max_length=300, blank=False)
    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE )
    date = models.DateTimeField(auto_now=True)   
    
class ScoreSubmissions(models.Model):
    score = models.ForeignKey(ScoreRequest, related_name='submissions', on_delete=models.CASCADE)
    content = models.CharField(max_length=300, blank=False)
    link = models.URLField(max_length=1024, blank=True, null=True)
    PDF = models.FileField(null=True, blank=True)
    PDFpath = models.CharField(max_length=1024, blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='submissions', on_delete=models.CASCADE )
    date = models.DateTimeField(auto_now=True)    
    accepted = models.BooleanField(default=False)