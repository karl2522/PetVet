from django.shortcuts import render, redirect
from .forms import MedicalRecordForm
from .models import MedicalRecord


def add_medical_record(request):
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicalrecords_list')  # Redirect to the list view
    else:
        form = MedicalRecordForm()
    return render(request, 'add_record.html', {'form': form})


def medical_records_list(request):
    records = MedicalRecord.objects.all()
    return render(request, 'record_list.html', {'records': records})
