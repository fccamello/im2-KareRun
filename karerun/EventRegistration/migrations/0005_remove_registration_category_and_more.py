# Generated by Django 5.1.2 on 2024-11-01 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventRegistration', '0004_registration_age_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='category',
        ),
        migrations.AddField(
            model_name='registration',
            name='category_ni',
            field=models.CharField(default='3k', max_length=100),
        ),
    ]