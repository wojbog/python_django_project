from django.test import TransactionTestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITransactionTestCase

from .models import Operation, PetrolPump, Vehicle


class TestModel(TransactionTestCase):
    reset_sequences = True

    def test_model_PetrolPump(self):
        obj = PetrolPump.objects.create(name="test", size=5.0)
        self.assertEqual(str(obj), "test")

    def test_model_Vehicle(self):
        obj = Vehicle.objects.create(name="test", max_size_tank=5.0)
        self.assertEqual(str(obj), "test")


class TestView(APITransactionTestCase):

    reset_sequences = True

    def setUp(self):
        data_vehicle1 = {"name": "test", "max_size_tank": 25.0}
        data_PetrolPump1 = {"name": "dystrybutor",
                            "current_state": 25.0, "size": 100.0}
        vehicle = Vehicle.objects.create(**data_vehicle1)
        petrolpump = PetrolPump.objects.create(**data_PetrolPump1)
        data_operation1 = {"date": "2010-05-05",
                           "id_vehicle": vehicle, "size": 25.0, "id_petrol_pump": petrolpump}
        data_operation2 = {"date": "2010-05-05",
                           "id_vehicle": vehicle, "size": 25.0, "id_petrol_pump": petrolpump}

        Operation.objects.create(**data_operation1)
        Operation.objects.create(**data_operation2)
        self.count = Operation.objects.count()

    def test_OperationLIstView(self):
        response = self.client.get('/orlen/operations/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), self.count)

    def test_operation_get(self):
        response = self.client.get('/orlen/operations/1/')
        self.assertEqual(response.status_code, 200)
        data = {"date": "2010-05-05",
                "id_vehicle": 1, "size": 25.0, "id_petrol_pump": 1}
        self.assertEqual(response.data, data)

    def test_operation_post(self):
        data = {"date": "2010-05-05", "id_vehicle": 1,
                "size": 27.0, "id_petrol_pump": 1}
        response = self.client.post(
            '/orlen/operations/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        op = Operation.objects.latest('id')
        self.assertEqual(op.size, data['size'])

    def test_Operation_delete(self):
        response = self.client.delete('/orlen/operations/2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        count = Operation.objects.count()
        self.assertEqual(count, 1)

    def test_operation_path(self):
        data = {"size": 27.0}
        response = self.client.patch(
            '/orlen/operations/1/', data, format='json')
        self.assertEqual(response.status_code, 200)
        op = Operation.objects.get(id=1)
        self.assertEqual(op.size, 27.0)
