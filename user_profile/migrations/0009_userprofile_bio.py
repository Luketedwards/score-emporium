# Generated by Django 3.2.14 on 2022-09-11 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0008_auto_20220911_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]