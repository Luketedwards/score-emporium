# Generated by Django 3.2.14 on 2022-07-11 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20220705_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='video',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]