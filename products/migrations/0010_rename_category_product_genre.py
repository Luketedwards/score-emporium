# Generated by Django 3.2.14 on 2022-07-16 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_product_difficulty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='genre',
        ),
    ]