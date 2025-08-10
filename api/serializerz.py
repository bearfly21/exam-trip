from rest_framework.serializers import ModelSerializer
from .models import *

class TripSerializer(ModelSerializer):
    class Meta:
        model = Trip
        fieds = '__all__'

class CompanionSerializer(ModelSerializer):
    class Meta:
        model = CompanionRequest
        fields = '__all__'