# Generated by Django 5.1.1 on 2024-12-09 14:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegLogCreate', '0018_alter_event_eventdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.DateField(blank=True, default=datetime.date(2024, 12, 9)),
        ),
    ]
