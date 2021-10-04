from rest_framework import serializers
from .models import Fundings, Ministry


class FundingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fundings
        fields = '__all__'


class MinistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ministry
        fields = '__all__'
