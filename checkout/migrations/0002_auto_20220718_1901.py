# Generated by Django 3.2.14 on 2022-07-18 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delivery_cost',
        ),
        migrations.RemoveField(
            model_name='order',
            name='grand_total',
        ),
    ]
