# Generated by Django 3.2.14 on 2022-07-05 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_vendor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='product',
            name='Guitar_Pro',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='PDF',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
