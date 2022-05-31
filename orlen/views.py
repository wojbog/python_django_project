from django.http import HttpResponse
from .serializers import OperationSerializer
from .models import Operation

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


class OperationDetailView(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        generics.GenericAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
