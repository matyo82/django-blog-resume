# Generated by Django 5.1.4 on 2025-01-02 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_alter_service_icon_class_alter_service_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='slug',
            field=models.SlugField(default='developer', max_length=200),
        ),
    ]
