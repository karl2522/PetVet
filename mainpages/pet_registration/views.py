from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PetRegistrationForm, PetUpdateForm, SPECIES_CHOICES
from registration_login.models import Profile
from .models import Pet
from datetime import date
from appointments.models import Appointment

@login_required
def pet_registration(request):
    if request.method == 'POST':
        form = PetRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.owner = request.user.profile
            pet.save()
            return redirect('pet_registration_success', pet_id=pet.pet_id)
    else:
        form = PetRegistrationForm()
    return render(request, 'pet_registration/pet_registration.html', {'form': form})

@login_required
def update_pet(request, pet_id):
    pet = get_object_or_404(Pet, pet_id=pet_id)
    
    # Check if the user is the owner of the pet
    if pet.owner != request.user.profile:
        messages.error(request, "You don't have permission to edit this pet's profile.")
        return redirect('pet_list_by_owner')

    if request.method == 'POST':
        form = PetRegistrationForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            updated_pet = form.save(commit=False)
            updated_pet.owner = pet.owner  # Ensure the owner remains unchanged
            updated_pet.save()
            messages.success(request, f"{pet.pet_name}'s profile has been updated successfully!")
            return redirect('pet_profile', pet_id=pet.pet_id)
    else:
        form = PetRegistrationForm(instance=pet)

    return render(request, 'pet_registration/pet_registration.html', {
        'form': form,
        'pet': pet,
        'is_update': True
    })

@login_required
def pet_list_by_owner(request):
    # Get the profile of the current user
    profile = request.user.profile
    # Get all pets owned by this user
    pets = Pet.objects.filter(owner=profile)
    # Get unique species
    species_list = [choice[0] for choice in SPECIES_CHOICES]  # Get just the values, not the display names
    return render(request, 'pet_registration/pet_list_by_owner.html', {
        'pets': pets,
        'species_list': species_list
    })

@login_required
def pet_profile(request, pet_id):
    pet = get_object_or_404(Pet, pet_id=pet_id)
    
    # Check if the user is the owner of the pet
    if pet.owner != request.user.profile:
        messages.error(request, "You don't have permission to view this pet's profile.")
        return redirect('pet_list_by_owner')
    
    # Get medical records
    medical_history = pet.medical_records.all()[:5]  # Get last 5 records
    
    # Get vaccinations
    vaccinations = pet.vaccinations.all()[:5]  # Get last 5 vaccinations
    
    # Get upcoming appointments
    upcoming_appointments = Appointment.objects.filter(
        pet=pet,
        date__gte=date.today()
    ).order_by('date', 'time')[:5]
    
    # Get medical files
    medical_files = pet.medical_files.all()[:5]  # Get last 5 files
    
    context = {
        'pet': pet,
        'medical_history': medical_history,
        'vaccinations': vaccinations,
        'upcoming_appointments': upcoming_appointments,
        'medical_files': medical_files,
    }
    
    return render(request, 'pet_registration/pet_profile.html', context)

def pet_registration_success(request, pet_id):
    pet = get_object_or_404(Pet, pet_id=pet_id)
    return render(request, 'pet_registration/pet_registration_success.html', {'pet': pet})

@login_required
def delete_pet(request, pet_id):
    # Get the pet object or return 404
    pet = get_object_or_404(Pet, pet_id=pet_id)
    
    # Check if the logged-in user is the owner of the pet
    if pet.owner != request.user.profile:
        messages.error(request, "You don't have permission to delete this pet.")
        return redirect('pet_list_by_owner')
    
    # Store pet name for success message
    pet_name = pet.pet_name
    
    # Delete the pet
    pet.delete()
    
    # Add success message
    messages.success(request, f'{pet_name} has been successfully removed.')
    
    return redirect('pet_list_by_owner')
