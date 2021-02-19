# Generated by Django 3.1.6 on 2021-02-19 09:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reco', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='cover_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='covers/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='webseries',
            name='cover_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='covers/'),
            preserve_default=False,
        ),
    ]