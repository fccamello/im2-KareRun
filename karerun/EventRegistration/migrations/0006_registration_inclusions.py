# Generated by Django 5.1.2 on 2024-11-01 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventRegistration', '0005_remove_registration_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='inclusions',
            field=models.CharField(default='0', max_length=100),
        ),
    ]
