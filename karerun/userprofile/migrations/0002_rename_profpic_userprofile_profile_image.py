# Generated by Django 5.1.1 on 2024-10-01 01:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='profpic',
            new_name='profile_image',
        ),
    ]
