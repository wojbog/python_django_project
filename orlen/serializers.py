from rest_framework import serializers
from .models import Operation, PetrolPump, Vehicle


class OperationSerializer(serializers.ModelSerializer):
    size = serializers.FloatField(min_value=0.0)

    class Meta:
        model = Operation
        fields = ['date', 'id_vehicle', 'size', 'id_petrol_pump']


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['name']


class OperationListSerializer(serializers.Serializer):
    '''
    #id_operations = serializers.PrimaryKeyRelatedField(read_only=True)
    #petrolPump = serializers.StringRelatedField(many=True)
    #vehicle = serializers.StringRelatedField(many=True)
    id_vehicle = VehicleSerializer(read_only=True)

    class Meta:
        model = Operation
        fields = ['date', 'id_vehicle', 'size', 'id_petrolPump']
        depth = 1
    '''
    date = serializers.DateField()
    vehicle = serializers.CharField(max_length=50)
    size = serializers.FloatField()
    petrolpump = serializers.CharField(max_length=50)
