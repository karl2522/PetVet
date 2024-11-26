from django.contrib import admin
from .models import Appointment

# Register your models here.

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('pet', 'date', 'time', 'purpose', 'status')
    search_fields = ('pet__name', 'purpose')
    list_filter = ('status', 'date')
    date_hierarchy = 'date'
