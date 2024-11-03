from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import JsonResponse
from appointments.models import Appointment
from django.shortcuts import render, get_object_or_404

# Render appointments page
def appointments_page(request):
    # Query all appointments (or filter as needed)
    pending_appointments = Appointment.objects.all()  # Adjust based on your needs
    static_status = "Pending"  # Static status as you requested
    print(pending_appointments)

    return render(request, "appointments.html", {
        'pending_appointments': pending_appointments,
        'static_status': static_status,
    })

def cancel_appointment(request, id):
    if request.method == 'POST':
        appointment = get_object_or_404(Appointment, id=id)  
        appointment.delete()

        messages.success(request, 'Appointment Cancelled successfully!')
        return redirect('appointments_page')  
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)


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

        messages.success(request, 'Appointment added successfully!')
        return redirect('appointments_page')  # Redirect to the appointments page

    # Return an error response if the method is not POST
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)
