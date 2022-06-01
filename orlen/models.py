from django.db import models

# Create your models here.
class PetrolPump(models.Model):
    name = models.CharField(max_length=50)
    current_state= models.FloatField(default=0)
    size = models.FloatField()

class Vehicle(models.Model):
    name = models.CharField( max_length=50)
    max_size_tank = models.FloatField()

class Operation(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    id_vehicle = models.ForeignKey("vehicle", on_delete=models.CASCADE)
    size = models.FloatField()
    id_petrol_pump = models.ForeignKey("petrolPump", on_delete=models.CASCADE)
