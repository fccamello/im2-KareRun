# Generated by Django 5.1.1 on 2024-11-03 02:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrganizerEventPage', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='cover_photo',
            field=models.ImageField(blank=True, null=True, upload_to='event_covers/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='participant',
            name='payment_status',
            field=models.CharField(choices=[('paid', 'Paid'), ('unpaid', 'Unpaid')], max_length=50),
        ),
        migrations.AlterField(
            model_name='participant',
            name='registration_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
