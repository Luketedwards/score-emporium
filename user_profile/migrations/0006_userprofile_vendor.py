# Generated by Django 3.2.14 on 2022-08-30 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_userprofile_money_due'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='vendor',
            field=models.BooleanField(default=False),
        ),
    ]
