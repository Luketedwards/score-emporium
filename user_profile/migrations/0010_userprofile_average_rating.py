# Generated by Django 3.2.14 on 2022-09-11 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0009_userprofile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='average_rating',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
