from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='car_images/')
    available = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cars')
    marka_car = models.CharField(max_length=100, default='Unknown')  # Марка автомобиля
    color_car = models.CharField(max_length=100, default='Unknown')  # Цвет автомобиля
    country_car = models.CharField(max_length=100, default='Unknown')  # Страна производства
    year_car = models.PositiveIntegerField(default='Unknown')  # Год изготовления
    mileage_car = models.PositiveIntegerField()  # Пробег
    engine_car = models.CharField(max_length=100, default='Unknown')  # Тип двигателя
    transmission_car = models.CharField(max_length=50, default='Unknown')  # Трансмиссия
    hand_drive = models.CharField(max_length=50, default='Unknown')  # Левый/правый руль
    type_oil = models.CharField(max_length=50, default='Unknown')  # Тип масла
    gear_car = models.CharField(max_length=50, default='Unknown')  # Привод

    def __str__(self):
        return self.name
