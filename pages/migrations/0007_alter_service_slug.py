# Generated by Django 5.1.4 on 2025-01-02 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_service_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
