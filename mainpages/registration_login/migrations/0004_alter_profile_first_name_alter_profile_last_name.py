# Generated by Django 5.1.1 on 2024-10-31 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_login', '0003_remove_profile_id_profile_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='Unknown', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='Unknown', max_length=50),
        ),
    ]