# Generated by Django 5.1.1 on 2024-12-02 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0014_alter_userprofile_cover_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='cover_photo',
            field=models.ImageField(default='photos/default.jpg', upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(default='photos/default.jpg', upload_to='photos/'),
        ),
    ]