from django import views
from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import viewsets
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

# Create your views here.
class EmployeeDetails(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [AllowAny]

