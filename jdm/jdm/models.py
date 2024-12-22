from django.db import models

class Car(models.Model):
    car_make = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_year = models.PositiveIntegerField()
    car_owner = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.car_make} {self.car_model} ({self.car_year})"