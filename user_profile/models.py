from urllib import request
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """
    A user profile model for maintaining order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    purchased_scores = []
    sales_number = models.DecimalField(
        max_digits=10, decimal_places=0, default=0)
    sales_income = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    money_due = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    vendor = models.BooleanField(default=False)
    sort_code = models.CharField(max_length=10, blank=True)
    account_number = models.CharField(max_length=20, blank=True)
    card_name = models.CharField(max_length=50, blank=True)
    profile_picture = models.ImageField(null=True, blank=True)
    cover_photo = models.ImageField(null=True, blank=True)
    bio = models.CharField(max_length=300, blank=True, null=True)
    average_rating = models.DecimalField(
        max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
        instance.userprofile.save()
