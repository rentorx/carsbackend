from django.shortcuts import render
from rest_framework import viewsets
from .models import Company
from .serializers import CompanySerializer
# Create your views here.


class CompanyViewSet(viewsets.ModelViewSet): 
    """
    API endpoint that allows to  
     be viewed or edited.
    """

    queryset = Company.objects.all()
    serializer_class = CompanySerializer


