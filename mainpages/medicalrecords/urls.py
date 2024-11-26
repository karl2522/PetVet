from django.urls import path
from . import views

urlpatterns = [
    path('add_record/', views.add_medical_record, name='add_medical_record'),
    path('medical_record_overview/', views.medical_records_list, name='medicalrecords_list'),
]
