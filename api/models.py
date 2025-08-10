from django.db import models
from accounts.models import CustomUser

class Trip(models.Model):
    location = models.CharField()
    date = models.DateField()
    places = models.IntegerField()

    def __str__(self):
        return self.location
    
class CompanionRequest(models.Model):
    user = models.ForeignKey(CustomUser, related_name='user_companion', on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, related_name="users_trip", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.trip
    
