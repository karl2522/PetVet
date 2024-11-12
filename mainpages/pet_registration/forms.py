from django import forms
from .models import Pet

class PetRegistrationForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['owner', 'pet_name', 'breed', 'species', 'sex', 'weight', 'birthday', 'pet_description']
        exclude = ['pet_id']  # Exclude the non-editable pet_id field
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }

class PetUpdateForm(forms.ModelForm):
    class Meta:
        model = Pet
        exclude = ['pet_id', 'owner']  # Exclude both pet_id and owner fields
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }
