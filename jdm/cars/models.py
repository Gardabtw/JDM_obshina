from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='car_images/')
    available = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cars')
    marka_car = models.CharField(max_length=100)  # Марка автомобиля
    color_car = models.CharField(max_length=50)  # Цвет автомобиля
    country_car = models.CharField(max_length=100)  # Страна производства
    year_car = models.PositiveIntegerField()  # Год изготовления
    mileage_car = models.PositiveIntegerField()  # Пробег
    engine_car = models.CharField(max_length=100)  # Тип двигателя
    transmission_car = models.CharField(max_length=50)  # Трансмиссия
    hand_drive = models.CharField(max_length=50)  # Левый/правый руль
    type_oil = models.CharField(max_length=50)  # Тип масла
    gear_car = models.CharField(max_length=50)  # Привод

    def __str__(self):
        return self.name
