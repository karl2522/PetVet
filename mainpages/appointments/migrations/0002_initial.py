# Generated by Django 5.1 on 2024-11-16 01:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appointments', '0001_initial'),
        ('pet_registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='pet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='pet_registration.pet'),
        ),
    ]