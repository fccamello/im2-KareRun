# Generated by Django 5.1.2 on 2024-10-25 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegLogCreate', '0006_alter_event_bannerimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='bannerimage',
            field=models.ImageField(upload_to='eventbanner/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='inclusionimage',
            field=models.ImageField(upload_to='eventinclusion/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='racerouteimage',
            field=models.ImageField(upload_to='eventraceroute/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='sizechartimage',
            field=models.ImageField(upload_to='eventsizechart/'),
        ),
    ]