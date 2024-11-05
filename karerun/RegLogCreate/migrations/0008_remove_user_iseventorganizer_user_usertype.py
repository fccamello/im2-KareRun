# Generated by Django 5.1 on 2024-11-03 07:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegLogCreate', '0007_alter_event_bannerimage_alter_event_inclusionimage_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='isEventOrganizer',
        ),
        migrations.AddField(
            model_name='user',
            name='userType',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3)]),
        ),
    ]