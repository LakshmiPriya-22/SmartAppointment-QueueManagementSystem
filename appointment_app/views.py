from django.shortcuts import render, redirect
from django.utils import timezone
from django.db.models import Max

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Appointment
from .serializers import AppointmentSerializer


# Home page (user side)
def home(request):
    return render(request, 'appointment_app/home.html')


# Receptionist dashboard
def receptionist_dashboard(request):
    appointments = Appointment.objects.all().order_by('token_number')
    return render(
        request,
        'appointment_app/receptionist.html',
        {'appointments': appointments}
    )


# Book appointment (token auto-generated)
@api_view(['POST'])
def book_appointment(request):
    last_token = Appointment.objects.aggregate(Max('token_number'))['token_number__max']
    next_token = 1 if last_token is None else last_token + 1

    serializer = AppointmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(
            token_number=next_token,
            booked_at=timezone.now()
        )
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)


# Call next token
def call_next_token(request):
    appointment = Appointment.objects.filter(status='pending').order_by('token_number').first()

    if appointment:
        appointment.status = 'called'
        appointment.called_at = timezone.now()
        appointment.save()

    return redirect('receptionist')
