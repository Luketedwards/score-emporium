# Generated by Django 3.2.14 on 2022-07-12 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_difficulty'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='difficulty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.difficulty'),
        ),
    ]
