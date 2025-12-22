from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('receptionist/', views.receptionist_dashboard, name='receptionist'),
    path('book/', views.book_appointment, name='book_appointment'),
    path('queue/', views.queue_status, name='queue_status'),
    path('call-next/', views.call_next, name='call_next'),
]
