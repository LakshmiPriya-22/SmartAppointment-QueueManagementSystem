from django.db import models

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

    booked_at = models.DateTimeField(auto_now_add=True)
    called_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Token {self.token_number} - {self.name}"
