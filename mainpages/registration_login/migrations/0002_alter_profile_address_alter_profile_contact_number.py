# Generated by Django 5.1.1 on 2024-10-26 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='contact_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
