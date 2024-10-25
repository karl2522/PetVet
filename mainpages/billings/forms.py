from django import forms
from .models import Billing

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = ['owner_id', 'appointment_id', 'total_amount', 'date_of_payment', 'payment_method', 'payment_status']
        widgets = {
            'date_of_payment': forms.DateInput(attrs={'type': 'date'}),
        }