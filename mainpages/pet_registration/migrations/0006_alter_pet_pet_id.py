# Generated by Django 5.1.1 on 2024-11-01 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_registration', '0005_alter_pet_pet_id_alter_pet_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='pet_id',
            field=models.CharField(editable=False, max_length=15, primary_key=True, serialize=False),
        ),
    ]
