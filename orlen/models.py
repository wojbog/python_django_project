from django.db import models


class PetrolPump(models.Model):
    name = models.CharField(max_length=50)
    current_state = models.FloatField(default=0)
    size = models.FloatField()

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    name = models.CharField(max_length=50)
    max_size_tank = models.FloatField()

    def __str__(self):
        return self.name


class Operation(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    id_vehicle = models.ForeignKey(
        'vehicle', related_name='vehicle', on_delete=models.CASCADE)
    size = models.FloatField()
    id_petrol_pump = models.ForeignKey("petrolPump", on_delete=models.CASCADE)
