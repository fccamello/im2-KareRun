# Generated by Django 5.1.2 on 2024-12-10 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegLogCreate', '0022_alter_event_closedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(default='M', max_length=10),
        ),
    ]
