from django.db import models

class Billing(models.Model):
    PAYMENT_METHODS = [
        ('CASH', 'Cash'),
        ('CARD', 'Card'),
    ]
    
    PAYMENT_STATUS = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed'),
    ]

    billing_id = models.AutoField(primary_key=True)
    owner_id = models.CharField(max_length=50)
    appointment_id = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_of_payment = models.DateField()
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS)

    def __str__(self):
        return f"Billing {self.billing_id} - Owner ID: {self.owner_id} - Appointment ID: {self.appointment_id}"
