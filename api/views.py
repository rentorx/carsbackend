from rest_framework import viewsets
from accounts.models import Account
from companies.models import Company
from . import serializers


class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows to  be viewed or edited.
    """

    queryset = Account.objects.all()
    serializer_class = serializers.AccountSerializer


class CompanyViewSet(viewsets.ModelViewSet): 
    """
    API endpoint that allows to  
     be viewed or edited.
    """

    queryset = Company.objects.all()
    serializer_class = serializers.CompanySerializer

