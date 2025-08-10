from django.urls import path
from .views import *

urlpatterns = [
    path('trips/', create_trip_view, name='create-trip'),
    path('trips/<int:pk>/', trip_edit_delete_api_view, name='edit-delete-trip'),

    path('companions/', create_companion_view, name='create-companion'),
    path('companions/<int:pk>/', companion_edit_delete_api_view, name='edit-delete-companion'),
]

