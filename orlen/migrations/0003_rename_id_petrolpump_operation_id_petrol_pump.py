# Generated by Django 3.2.13 on 2022-06-07 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orlen', '0002_alter_operation_id_vehicle'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operation',
            old_name='id_petrolPump',
            new_name='id_petrol_pump',
        ),
    ]