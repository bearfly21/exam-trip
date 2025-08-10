from django.shortcuts import render
from .serializerz import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


api_view(["GET", "POST"])
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
def edit_delete_api_view(request, pk):
    trip = Trip.objects.filter(id=pk).first()
    if request.method == "GET":
        serializer = TripSerializer(trip)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = TripSerializer(trip,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        trip.delete()
        return Response(status=status.HTTP_200_OK)

    

