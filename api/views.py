from django.shortcuts import render
from .serializerz import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET", "POST"])
def create_trip_view(request):
    if request.method == "GET":
        trip = Trip.objects.all()
        serializer = TripSerializer(trip, many= True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = TripSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def trip_edit_delete_api_view(request, pk):
    trip = Trip.objects.filter(id=pk).first()
    if request.method == "GET":
        serializer = TripSerializer(trip)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = TripSerializer(trip, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        trip.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
@api_view(["GET", "POST"])
def create_companion_view(request):
    if request.method == "GET":
        companion = CompanionRequest.objects.all()
        serializer = CompanionSerializer(companion, many= True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CompanionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def companion_edit_delete_api_view(request, pk):
    companion = CompanionRequest.objects.filter(id=pk).first()
    if request.method == "GET":
        serializer = CompanionSerializer(companion)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = CompanionSerializer(companion, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        companion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
