from rest_framework import serializers
from .models import *
#Loan Serializer
class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model=Loan
        fields=('first_name','last_name','email','mobile','address')