from multiprocessing import AuthenticationError
from django.shortcuts import render
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from .permission import IsReadOnly, IsGet_Post_Pit, IsAuthenticated, IsSuperUser, IsStaff


# Create your views here.
class CustomerDetails(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsGet_Post_Pit, ]
