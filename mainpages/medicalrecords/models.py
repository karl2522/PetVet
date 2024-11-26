from django.db import models


# Assuming Pet model is already defined in the same or another app
class Pet(models.Model):
    # Fields for Pet model (e.g., PetID, Name, etc.)
    pet_id = models.AutoField(primary_key=True)
    pet_name = models.CharField(max_length=100)

    def __str__(self):
        return self.pet_name


class MedicalRecord(models.Model):
    medical_record_id = models.AutoField(primary_key=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    date_recorded = models.DateField()
    symptoms = models.TextField()
    diagnosis = models.TextField()
    treatment = models.TextField()
    prescription = models.TextField()

    def __str__(self):
        return f"Record for {self.pet.pet_name} on {self.date_recorded}"
