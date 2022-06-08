from django.http import HttpResponse
from .serializers import OperationSerializer, OperationListSerializer
from .models import Operation, PetrolPump

from rest_framework import mixins, generics
from rest_framework.response import Response


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


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
                          generics.GenericAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
