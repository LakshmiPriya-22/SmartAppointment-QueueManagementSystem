from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Appointment

# Home Page
def home(request):
    return render(request, "home.html")


# Receptionist Dashboard
def receptionist_dashboard(request):
    if request.method == "POST":
        action = request.POST.get("action")

        if action == "call_next":
            next_appt = Appointment.objects.filter(status="PENDING").order_by("token_number").first()
            if next_appt:
                next_appt.status = "CALLED"
                next_appt.save()

        elif action == "mark_done":
            appt_id = request.POST.get("appointment_id")
            Appointment.objects.filter(id=appt_id).update(status="DONE")

        return redirect("receptionist")

    pending = Appointment.objects.filter(status="PENDING").order_by("token_number")
    called = Appointment.objects.filter(status="CALLED").order_by("-called_at").first()

    return render(
        request,
        "appointment_app/receptionist.html",
        {
            "pending": pending,
            "called": called,
        },
    )


# ✅ LIVE DISPLAY SCREEN (TV VIEW)
def live_display(request):
    current = Appointment.objects.filter(status="CALLED").order_by("-called_at").first()
    upcoming = Appointment.objects.filter(status="PENDING").order_by("token_number")[:5]

    return render(
        request,
        "appointment_app/live_display.html",
        {
            "current": current,
            "upcoming": upcoming,
        },
    )
