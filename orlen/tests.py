from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase

from .models import PetrolPump, Vehicle


class TestModel(TestCase):

    def test_model_PetrolPump(self):
        obj = PetrolPump.objects.create(name="test", size=5.0)
        self.assertEqual(str(obj), "test")

    def test_model_Vehicle(self):
        obj = Vehicle.objects.create(name="test", max_size_tank=5.0)
        self.assertEqual(str(obj), "test")
