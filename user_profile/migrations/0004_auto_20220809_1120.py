# Generated by Django 3.2.14 on 2022-08-09 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_remove_userprofile_purchased_scores'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='sales_income',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='sales_number',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
    ]