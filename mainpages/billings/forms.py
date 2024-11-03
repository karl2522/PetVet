from django import forms
from .models import Billing
from django.shortcuts import redirect

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = ['owner_id', 'appointment_id', 'total_amount', 'date_of_payment', 'payment_method', 'payment_status']
        widgets = {
            'date_of_payment': forms.DateInput(attrs={'type': 'date'}),
        }


class OwnerSearchForm(forms.Form):
    owner_id = forms.IntegerField(label='Owner ID')

class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = ['appointment_id', 'total_amount', 'date_of_payment', 'payment_method', 'payment_status']    
