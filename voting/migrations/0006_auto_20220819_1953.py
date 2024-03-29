# Generated by Django 3.2.14 on 2022-08-19 19:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('voting', '0005_auto_20220819_1947'),
    ]

    operations = [
        # migrations.AddField(
        #     model_name='scorerequest',
        #     name='likes',
        #     field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        # ),
        migrations.AddField(
            model_name='scoresubmissions',
            name='PDF',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='scoresubmissions',
            name='link',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        # migrations.CreateModel(
        #     name='Comment',
        #     fields=[
        #         ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('content', models.CharField(max_length=300)),
        #         ('date', models.DateTimeField(auto_now=True)),
        #         ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to=settings.AUTH_USER_MODEL)),
        #         ('score', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='voting.scorerequest')),
        #     ],
        # ),
    ]
