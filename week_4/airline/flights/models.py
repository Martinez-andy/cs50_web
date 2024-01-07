from django.db import models

# Create your models here.

# Create a class for each table | This is similar to initializing a new SQLite table
class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()