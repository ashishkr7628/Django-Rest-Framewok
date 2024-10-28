from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CompanySerializers,EmployeeSerializers

from .models import Company,Employee


class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializers
    
# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializers
    