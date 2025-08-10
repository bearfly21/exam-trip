from django.shortcuts import redirect, render
from .models import CustomUser, Token
from .serializers import UserSerializer
from django.contrib.auth import login, logout, authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(["POST", "GET"])
def confirm_email(request, token):
    try:
        email_confirm_object = Token.objects.get(token=token)
    except Token.DoesNotExist:
        return Response('Token invalid or expired !')
    user = email_confirm_object.user
    user.is_active = True
    user.is_confirmed_email = True
    user.save()
    email_confirm_object.delete()
    return  Response('Email confirmed', status=status.HTTP_200_OK)

@api_view(["POST"])
def register_api_view(request):
    email = request.data.get("email", None)
    password = request.data.get("password", None)
    conf_password = request.data.get("conf_password", None)
    if not email or not password or not conf_password:
        return Response("fill all datas")
    if password != conf_password:
        return Response("passwords don't match")
    user = CustomUser.objects.filter(email=email).first()
    if user:
        return Response("user already exists")
    user = CustomUser.objects.create_user(email=email, password=password)
    user.save()
    return Response("User registered", status=status.HTTP_201_CREATED)


@api_view(["POST"])
def login_api_view(request):
    email = request.data.get("email", None)
    password = request.data.get("password", None)
    user = authenticate(request, email=email, password = password)
    if user is not None:
        login(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    return Response("invalid credentials", status=status.HTTP_401_UNAUTHORIZED)

@api_view(["GET"])
def logout_api_view(request):
    try:
        logout(request)
        return Response("you are logged out", status=status.HTTP_200_OK)
    except Exception as ex:
        return Response({"error": str(ex)})