# Generated by Django 5.1.2 on 2024-11-28 11:42

import client.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0023_photogallery'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photogallery',
            options={'verbose_name': 'Fotogalereya', 'verbose_name_plural': 'Fotogalereya'},
        ),
        migrations.RenameField(
            model_name='photogallery',
            old_name='address',
            new_name='address_en',
        ),
        migrations.AddField(
            model_name='photogallery',
            name='address_ru',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='photogallery',
            name='address_uz',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='PhotoGalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=client.models.photo_gallery_image_upload_path)),
                ('photo_gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='client.photogallery')),
            ],
            options={
                'verbose_name': 'Fotogalereya Rasm',
                'verbose_name_plural': 'Fotogalereya Rasmlar',
            },
        ),
    ]
