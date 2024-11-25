# Generated by Django 5.1 on 2024-11-25 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegLogCreate', '0016_alter_user_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='isClosed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='maxSlots',
            field=models.IntegerField(default=0),
        ),
    ]
