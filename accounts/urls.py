from django.urls import path
from .views import *

urlpatterns = [
    path("register", register_api_view),
    path("login", login_api_view),
    path("logout", logout_api_view),
]
