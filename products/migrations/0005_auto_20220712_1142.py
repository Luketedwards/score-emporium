# Generated by Django 3.2.14 on 2022-07-12 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Guitar_Pro',
            field=models.FileField(null=True, upload_to='static/media/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PDF',
            field=models.FileField(null=True, upload_to='../static/media/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='../static/media/'),
        ),
    ]