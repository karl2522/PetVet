from django import forms
from medicalrecords.models import MedicalRecord


class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['pet', 'date_recorded', 'symptoms', 'diagnosis', 'treatment', 'prescription']
