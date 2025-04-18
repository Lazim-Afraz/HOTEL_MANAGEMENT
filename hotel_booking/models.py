from django.db import models
from cloudinary.models import CloudinaryField


class Room(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    check_in_date = models.DateField(default='2024-11-17')  # Added check-in date field
    check_out_date = models.DateField(default='2024-11-17')  # Added check-out date field
    duration = models.PositiveIntegerField()  # Duration in nights
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    approved = models.BooleanField(default=False)  # Make sure this field exists!

    def __str__(self):
        return f"Booking by {self.name} for {self.room.name}"
