# Generated by Django 5.1.2 on 2024-11-26 10:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0009_alter_festival_options_festivalimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='festival',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='festivals', to='client.festivalcategory'),
        ),
    ]