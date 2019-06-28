from rest_framework import serializers
from accounts.models import Account
from companies.models import Company


# Serializers define the API representation.
class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'


#class AccountSerializer(serializers.HyperlinkedModelSerializer):
class AccountSerializer(serializers.ModelSerializer):

#company = serializers.PrimaryKeyRelatedField(many=True, queryset=Company.objects.all())
    class Meta:
        model = Account
        fields = '__all__'
