# Generated by Django 5.1.1 on 2024-11-03 01:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('RegLogCreate', '0007_alter_event_bannerimage_alter_event_inclusionimage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('registrationid', models.BigAutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=100)),
                ('inclusions', models.JSONField()),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to='RegLogCreate.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to='RegLogCreate.user')),
            ],
        ),
    ]
