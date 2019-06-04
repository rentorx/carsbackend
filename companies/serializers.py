from .models import Company
from rest_framework import serializers


# Serializers define the API representation.

class CompanySerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Company
        fields = ('name')
#        fields = '__all__' 
