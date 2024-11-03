from django.shortcuts import render, redirect, get_object_or_404
from .forms import PetRegistrationForm
from registration_login.models import Profile
from .models import Pet

def pet_registration(request):
    if request.method == 'POST':
        form = PetRegistrationForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            user_id = request.POST.get('owner')  # Assuming you're getting user_id from the form selection
            pet.owner = get_object_or_404(Profile, user_id=user_id)  # Fetch the Profile instance using user_id
            pet.save()  # pet_id is automatically generated now
            return redirect('pet_registration_success', pet_id=pet.pet_id)  # Pass the pet_id to the success page
    else:
        form = PetRegistrationForm()

    context = {'form': form}
    return render(request, 'pet_registration/pet_registration.html', context)

def pet_registration_success(request, pet_id):
    pet = get_object_or_404(Pet, pet_id=pet_id)
    return render(request, 'pet_registration/pet_registration_success.html', {'pet': pet})

def pet_profile(request, pet_id):
    pet = get_object_or_404(Pet, pet_id=pet_id)  # Fetch the pet instance from the database
    return render(request, 'pet_registration/pet_profile.html', {'pet': pet})
