# Generated by Django 5.1.1 on 2024-11-28 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0013_remove_userprofile_birthdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='cover_photo',
            field=models.ImageField(default='photos/default.png', upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(default='photos/default.png', upload_to='photos/'),
        ),
    ]
