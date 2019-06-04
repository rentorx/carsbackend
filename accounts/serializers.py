from .models import Account
from rest_framework import serializers


# Serializers define the API representation.

class AccountSerializer(serializers.HyperlinkedModelSerializer):
   # company = CompanySerializer()


    class Meta:
        model = Account
        fields = ('user',)
#        fields = '__all__' 


