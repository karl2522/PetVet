# Generated by Django 5.1.1 on 2024-11-03 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('billing_id', models.AutoField(primary_key=True, serialize=False)),
                ('owner_id', models.CharField(max_length=50)),
                ('appointment_id', models.CharField(max_length=50)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_of_payment', models.DateField()),
                ('payment_method', models.CharField(choices=[('CASH', 'Cash'), ('CARD', 'Card')], max_length=10)),
                ('payment_status', models.CharField(choices=[('PENDING', 'Pending'), ('COMPLETED', 'Completed'), ('FAILED', 'Failed')], max_length=10)),
            ],
        ),
    ]
