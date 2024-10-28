from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CompanySerializers,EmployeeSerializers

from rest_framework.decorators import action

from rest_framework.response import Response
from .models import Company,Employee


class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializers
    
    
    @action(methods=['get'],detail=True)
    def employees(self,request,pk=None):
        
        try:
            company=Company.objects.get(pk=pk)
            emps=Employee.objects.filter(company=company)
            emps_serializer=EmployeeSerializers(emps,many=True,context={'request':request})
            
            return Response(emps_serializer.data)
        except Exception as e:
            
            return Response({
                "msg": "Company might not be exist, ERROR"
            })
    
        
# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializers
    