# Generated by Django 3.2.14 on 2022-08-12 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scorerequest',
            name='created_at',
        ),
        migrations.AddField(
            model_name='scorerequest',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
