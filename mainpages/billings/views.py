import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .forms import PaymentForm
from .forms import OwnerSearchForm
from .models import Billing
from django.contrib import messages

# Existing billing overview view
def billing_overview(request, owner_id):
    # Get all billings for the owner
    billings = Billing.objects.filter(owner_id=owner_id)

    # Filter billings to get only those with a 'Pending' status
    pending_card_billings = billings.filter(payment_method='Card', payment_status='Pending')

    return render(request, 'overview.html', {
        'billings': billings,           # All billings for the owner
        'pending_card_billings': pending_card_billings  # Only pending billings
    })

# New add payment view
def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the payment details to the database
            messages.success(request, 'Payment successfully added!')
            return redirect('billings:add_payment')  # Redirect using the correct namespace
    else:
        form = PaymentForm()

    return render(request, 'billing/add_payment.html', {'form': form})


def choose_payment_method(request):
    # Assuming the user is logged in and you can get their latest billing record
    user = request.user  # Get the current user
    latest_billing = Billing.objects.filter(owner_id=user.id).order_by('-date_of_payment').first()  # Get the latest billing record

    if request.method == 'POST':
        # Process the chosen payment method
        selected_method = request.POST.get('payment_method')
        if latest_billing:
            # Update the latest billing record with the chosen payment method
            latest_billing.payment_method = selected_method
            latest_billing.save()
            return redirect('billing_overview')  # Redirect back to the billing overview

    return render(request, 'choose_payment_method.html', {'latest_billing': latest_billing})

def manage_billing(request):
    form = OwnerSearchForm()
    billings = None
    owner_id = None

    if request.method == 'POST':
        form = OwnerSearchForm(request.POST)
        if form.is_valid():
            owner_id = form.cleaned_data['owner_id']
            # Filter billing records by owner_id
            billings = Billing.objects.filter(owner_id=owner_id)

            if not billings.exists():
                form.add_error('owner_id', '| No billing records found for this Owner ID | ')

    return render(request, 'manage_billing.html', {'form': form, 'billings': billings, 'owner_id': owner_id})

def update_billing(request, billing_id):
    if request.method == 'POST':
        try:
            billing = get_object_or_404(Billing, pk=billing_id)
            data = json.loads(request.body)

            billing.appointment_id = data.get('appointment_id')
            billing.total_amount = data.get('total_amount')
            billing.date_of_payment = data.get('date_of_payment')
            billing.payment_method = data.get('payment_method')
            billing.payment_status = data.get('payment_status')
            billing.save()

            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'message': 'Invalid request method'})

def delete_billing(request, billing_id):
    if request.method == 'POST':
        billing = get_object_or_404(Billing, pk=billing_id)
        billing.delete()
        return JsonResponse({'success': True})

    return JsonResponse({'success': False, 'error': 'Invalid request method.'})

def confirm_payment_method(request, owner_id):
    if request.method == 'POST':
        # payment_method = request.POST.get('payment_method')
        # Process the payment method here (e.g., save to the database)

        # Redirect back to the billing overview page for the given owner_id
        return redirect('billing_overview', owner_id=owner_id)

