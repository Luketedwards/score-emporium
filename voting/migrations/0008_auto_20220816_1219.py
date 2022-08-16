# Generated by Django 3.2.14 on 2022-08-16 12:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('voting', '0007_alter_liketracker_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='scorerequest',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='likeTracker',
        ),
    ]
