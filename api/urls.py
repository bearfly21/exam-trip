from django.urls import path
from .views import *

urlpatterns = [
    path('', create_trip_view),
    path('create_trip', create_trip_view),
    path('update_trip', edit_delete_api_view),
    path('delete_trip', edit_delete_api_view),
]
