from django.contrib import admin

from .models import PetrolPump, Operation, Vehicle

admin.site.register(PetrolPump)
admin.site.register(Vehicle)
admin.site.register(Operation)
