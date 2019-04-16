from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import *
from .serializers import EmployeeSerializer


class ListEmployeesView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer