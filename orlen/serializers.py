from rest_framework import serializers
from .models import Operation


class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = ['date', 'id_vehicle', 'size', 'id_petrolPump']
