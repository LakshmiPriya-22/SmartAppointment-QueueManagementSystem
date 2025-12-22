from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('token_number', 'name', 'service', 'status', 'booked_at')
    list_filter = ('status', 'service')
    search_fields = ('name', 'token_number')
    readonly_fields = ('token_number', 'booked_at', 'called_at')
