from django.urls import path
from .views import csv_output

urlpatterns = [
    path('user_task', csv_output, name='csv_output'),
]
