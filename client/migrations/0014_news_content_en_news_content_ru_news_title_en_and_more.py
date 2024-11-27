# Generated by Django 5.1.2 on 2024-11-27 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0013_remove_festival_address_remove_festival_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='content_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='content_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='title_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='title_ru',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]