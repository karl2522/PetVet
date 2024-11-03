from django.db import models
from registration_login.models import Profile

class Pet(models.Model):
    pet_id = models.CharField(max_length=15, primary_key=True, editable=False)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)  # Referencing the Profile model as the owner
    pet_name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    sex = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Unknown', 'Unknown')])
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    birthday = models.DateField()
    pet_description = models.TextField(blank=True, null=True)
    image_url = models.URLField(max_length=200, blank=True, null=True)  # Image URL

    def save(self, *args, **kwargs):
        if not self.pet_id:
            # Fetch the last saved pet and determine the new pet_id
            last_pet = Pet.objects.all().order_by('pk').last()
            if last_pet and last_pet.pet_id.startswith('PETID'):
                last_id_number = int(last_pet.pet_id.replace('PETID', ''))
                new_id_number = last_id_number + 1
            else:
                new_id_number = 1

            self.pet_id = f"PETID{new_id_number}"
        
        super(Pet, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.pet_name} ({self.breed})"