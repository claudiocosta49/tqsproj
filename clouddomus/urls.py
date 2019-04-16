from django.urls import path
from .views import *


urlpatterns = [
    path('employees/', ListEmployeesView.as_view(), name="employees-all")
]