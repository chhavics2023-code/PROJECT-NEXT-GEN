from django.db import models
from django.contrib.auth.models import User


class Hall(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='halls_images/')

    def _str_(self):
        return self.name


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    event_date = models.DateField()
    event_type = models.CharField(max_length=50)
    guests = models.IntegerField()
    message = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'Pending'),
            ('Approved', 'Approved'),
            ('Rejected', 'Rejected'),
        ],
        default='Pending'
    )

    def _str_(self):
        return f"{self.name} - {self.event_date}"