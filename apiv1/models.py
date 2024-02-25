from django.db import models

class Traveller(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    birth_date = models.DateField()

class TouristPlace(models.Model):
    place_name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)

class TouristAgency(models.Model):
    agency_name = models.CharField(max_length=50)
    package_cost = models.DecimalField(max_digits=10, decimal_places=2)
    subscribers = models.PositiveIntegerField(default=0)
    traveller = models.ForeignKey(Traveller, on_delete=models.CASCADE)
    visited_places = models.ManyToManyField(TouristPlace)
