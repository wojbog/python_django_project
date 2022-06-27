from rest_framework import serializers
from .models import Operation, PetrolPump, Vehicle


class OperationDetailSerializer(serializers.ModelSerializer):
    size = serializers.FloatField(min_value=0.0)

    class Meta:
        model = Operation
        fields = ['date', 'id_vehicle', 'size', 'id_petrol_pump']
        read_only_fields = ['id_vehicle', 'id_petrol_pump']

class OperationSerializer(serializers.ModelSerializer):
    size = serializers.FloatField(min_value=0.0)

    class Meta:
        model = Operation
        fields = ['id','date', 'id_vehicle', 'size', 'id_petrol_pump']


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['name']


class OperationListSerializer(serializers.Serializer):
    date = serializers.DateField()
    vehicle = serializers.CharField(max_length=50)
    size = serializers.FloatField()
    petrolpump = serializers.CharField(max_length=50)
