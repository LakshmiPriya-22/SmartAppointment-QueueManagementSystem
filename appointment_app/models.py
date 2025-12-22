from django.db import models
from django.utils import timezone


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('called', 'Called'),
        ('done', 'Done'),
    ]

    name = models.CharField(max_length=100)
    service = models.CharField(max_length=100)

    token_number = models.PositiveIntegerField(unique=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )

    booked_at = models.DateTimeField(default=timezone.now)
    called_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.token_number:
            last = Appointment.objects.order_by('-token_number').first()
            self.token_number = 1 if not last else last.token_number + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Token {self.token_number} - {self.name}"
