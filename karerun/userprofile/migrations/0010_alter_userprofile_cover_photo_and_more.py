# Generated by Django 5.1.1 on 2024-10-25 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0009_remove_userprofile_cover_img_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='cover_photo',
            field=models.BinaryField(blank=True, editable=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.BinaryField(blank=True, editable=True, null=True),
        ),
    ]
