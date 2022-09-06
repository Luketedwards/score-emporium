from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    class Meta:
        verbose_name_plural = 'Genres'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Difficulty(models.Model):

    level = models.CharField(max_length=254)
    

    def __str__(self):
        return self.level
       


class Product(models.Model):
    genre = models.ForeignKey('Genre', null=True, blank=True, on_delete=models.SET_NULL)
    difficulty = models.ForeignKey('Difficulty', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True,)
    vendor = models.CharField(max_length=254, null=True)
    PDF = models.FileField(null=True,)
    Guitar_Pro_Unlocked = models.FileField(null=True,)
    Guitar_Pro_Locked = models.FileField(null=True, blank=True)
    video = models.URLField(max_length=1024, null=True, blank=True)
    
    


    def __str__(self):
        return self.name

def average_rating(self):
    total_reviews = 0

    for review in self.review.all():
        total_reviews += review.ratings

    if total_reviews > 0:
        return total_reviews / self.reviews.count() 

    return 0       

class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    ratings = models.IntegerField(default=0)
    subject = models.CharField(max_length=30, null=True, blank=True)
    content = models.TextField()
    created_by = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE )
    date = models.DateTimeField(auto_now=True)        