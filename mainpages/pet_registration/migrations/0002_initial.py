# Generated by Django 5.1 on 2024-11-16 01:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pet_registration', '0001_initial'),
        ('registration_login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration_login.profile'),
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='pet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medical_records', to='pet_registration.pet'),
        ),
        migrations.AddField(
            model_name='medicalfile',
            name='pet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medical_files', to='pet_registration.pet'),
        ),
        migrations.AddField(
            model_name='vaccination',
            name='pet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vaccinations', to='pet_registration.pet'),
        ),
    ]