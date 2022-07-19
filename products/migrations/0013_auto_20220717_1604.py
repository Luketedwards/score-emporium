# Generated by Django 3.2.14 on 2022-07-17 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Guitar_Pro',
            new_name='Guitar_Pro_Locked',
        ),
        migrations.AddField(
            model_name='product',
            name='Guitar_Pro_Unlocked',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]