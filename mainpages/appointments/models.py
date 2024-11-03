from django.db import models

class Appointment(models.Model):
    owner_name = models.CharField(max_length=100)
    pet_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    veterinarian_name = models.CharField(max_length=100)
    reason_for_visit = models.TextField()

    def __str__(self):
        return f"{self.owner_name} - {self.pet_name}"
