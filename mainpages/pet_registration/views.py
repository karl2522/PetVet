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

def update_pet(request, pet_id):
    # Retrieve the pet instance from the database
    pet = get_object_or_404(Pet, pet_id=pet_id)

    if request.method == 'POST':
        # Populate form with data from POST request, excluding 'owner'
        form = PetRegistrationForm(request.POST, instance=pet)

        if form.is_valid():
            # Save the form data without committing immediately
            updated_pet = form.save(commit=False)
            # Set the owner to the current owner from the pet instance
            updated_pet.owner = pet.owner
            updated_pet.save()  # Save the updated instance with the owner set
            return redirect('pet_profile', pet_id=pet.pet_id)
        else:
            # If form is invalid, print the errors
            print(form.errors)
    else:
        # Populate the form with the existing pet data for GET request
        form = PetRegistrationForm(instance=pet)

    context = {
        'pet': pet,
        'form': form
    }
    return render(request, 'pet_registration/update_pet.html', context)

def pet_registration_success(request, pet_id):
    pet = get_object_or_404(Pet, pet_id=pet_id)
    return render(request, 'pet_registration/pet_registration_success.html', {'pet': pet})

def pet_profile(request, pet_id):
    pet = get_object_or_404(Pet, pet_id=pet_id)  # Fetch the pet instance from the database
    return render(request, 'pet_registration/pet_profile.html', {'pet': pet})
