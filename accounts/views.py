from django.shortcuts import render
from rest_framework import viewsets
from .models import Account
from .serializers import AccountSerializer
# Create your views here.


class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows to  be viewed or edited.
    """

    queryset = Account.objects.all()
    serializer_class = AccountSerializer


