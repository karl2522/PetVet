from django.shortcuts import render, redirect
from .forms import PaymentForm
from .models import Billing
from django.contrib import messages

# Existing billing overview view
def billing_overview(request, owner_id):
    billings = Billing.objects.filter(owner_id=owner_id)
    return render(request, 'billing/overview.html', {'billings': billings})

# New add payment view
def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the payment details to the database
            messages.success(request, 'Payment successfully added!')
            return redirect('add_payment')  # Redirect to the same page or another page
    else:
        form = PaymentForm()

    return render(request, 'billing/add_payment.html', {'form': form})
