# Generated by Django 3.2.14 on 2022-10-07 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_product_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(blank=True, default='0', max_length=254, null=True),
        ),
    ]