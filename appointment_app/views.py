from django.shortcuts import render
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Appointment
from .serializers import AppointmentSerializer


def home(request):
    return render(request, 'appointment_app/home.html')


def receptionist_dashboard(request):
    appointments = Appointment.objects.all().order_by('token_number')
    return render(
        request,
        'appointment_app/receptionist.html',
        {'appointments': appointments}
    )


@api_view(['POST'])
def book_appointment(request):
    serializer = AppointmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def queue_status(request):
    appointments = Appointment.objects.filter(status='pending').order_by('token_number')
    serializer = AppointmentSerializer(appointments, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def call_next(request):
    appointment = Appointment.objects.filter(status='pending').order_by('token_number').first()
    if not appointment:
        return Response({"message": "No pending appointments"}, status=404)

    appointment.status = 'called'
    appointment.called_at = timezone.now()
    appointment.save()

    serializer = AppointmentSerializer(appointment)
    return Response(serializer.data)
