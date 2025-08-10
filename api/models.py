from django.db import models
from accounts.models import CustomUser

class Trip(models.Model):
    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)
    date = models.DateField()
    places = models.IntegerField()
    price_for_one_person = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.start_location} - {self.end_location}"
    
class CompanionRequest(models.Model):
    user = models.ForeignKey(CustomUser, related_name='user_companion', on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, related_name="users_trip", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.email} request for {self.trip} - {'Accepted' if self.status else 'Pending'}"
    
