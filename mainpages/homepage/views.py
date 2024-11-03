from django.shortcuts import render, redirect
from django.http import JsonResponse
from appointments.models import Appointment

def homepage(request):
    return render(request, 'homepage.html')

def set_appointment(request):
    if request.method == 'POST':
        # Process the form data
        owner_name = request.POST.get('owner_name')
        pet_name = request.POST.get('pet_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        appointment_date = request.POST.get('appointment_date')
        appointment_time = request.POST.get('appointment_time')
        veterinarian_name = request.POST.get('veterinarian_name')
        reason_for_visit = request.POST.get('reason')

        # Save the appointment to the database
        appointment = Appointment.objects.create(
            owner_name=owner_name,
            pet_name=pet_name,
            email=email,
            phone_number=phone_number,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            veterinarian_name=veterinarian_name,
            reason_for_visit=reason_for_visit,
        )

        # Return a JSON response indicating success
        return JsonResponse({'status': 'success', 'message': 'Appointment created successfully.', 'appointment_id': appointment.id})

    # Return an error response if the method is not POST
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)
