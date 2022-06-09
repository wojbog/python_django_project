from django.http import HttpResponse
from .serializers import OperationSerializer, OperationListSerializer
from .models import Operation, PetrolPump

from rest_framework import mixins, generics
from rest_framework.response import Response



class OperationListView(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        generics.GenericAPIView):
    queryset = Operation.objects.raw(
        'select orlen_operation.id,orlen_operation.date, orlen_operation.size, orlen_vehicle.name as "vehicle", orlen_petrolpump.name as "petrolpump" from orlen_operation join orlen_vehicle on orlen_vehicle.id=orlen_operation.id_vehicle_id join orlen_petrolpump on orlen_operation.id_petrol_pump_id=orlen_petrolpump.id')
    serializer_class = OperationListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class OperationDetailView(mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          generics.GenericAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
