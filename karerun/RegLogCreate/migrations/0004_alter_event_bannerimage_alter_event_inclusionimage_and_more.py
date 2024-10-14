# Generated by Django 5.1 on 2024-10-01 03:48

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegLogCreate', '0003_alter_user_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='bannerimage',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/photos/eventbanner/'), upload_to=''),
        ),
        migrations.AlterField(
            model_name='event',
            name='inclusionimage',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/photos/eventinclusion/'), upload_to=''),
        ),
        migrations.AlterField(
            model_name='event',
            name='racerouteimage',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/photos/eventraceroute/'), upload_to=''),
        ),
        migrations.AlterField(
            model_name='event',
            name='sizechartimage',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/photos/eventsizechart/'), upload_to=''),
        ),
    ]