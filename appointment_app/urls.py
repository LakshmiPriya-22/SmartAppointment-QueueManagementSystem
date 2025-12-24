from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("receptionist/", views.receptionist_dashboard, name="receptionist"),
    path("live/", views.live_display, name="live_display"),  # 👈 TV VIEW
]
