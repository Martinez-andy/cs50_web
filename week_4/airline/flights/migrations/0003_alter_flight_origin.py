# Generated by Django 5.0 on 2024-01-07 19:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_airport_alter_flight_destination_alter_flight_origin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='origin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deoartures', to='flights.airport'),
        ),
    ]
