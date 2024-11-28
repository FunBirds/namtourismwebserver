# Generated by Django 5.1.2 on 2024-11-28 15:45

import client.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0027_festivalposter'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='festivalposter',
            options={'verbose_name': 'Festival Poster', 'verbose_name_plural': 'Festival Posters'},
        ),
        migrations.AlterField(
            model_name='festivalposter',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=client.models.festival_poster_video_upload_path),
        ),
    ]
