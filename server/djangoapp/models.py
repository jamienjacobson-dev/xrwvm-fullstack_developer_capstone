from django.db import models
# from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}: {self.description}"


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('HATCHBACK', 'Hatchback'),
        ('SUV', 'SUV'),
        ('COUPE', 'Coupe'),
        ('CONVERTIBLE', 'Convertible')
    ]
    type = models.CharField(max_length=100, choices=CAR_TYPES)
    year = models.IntegerField(default=2023, validators=[
        MaxValueValidator(2023),
        MinValueValidator(2015),
    ])

    def __str__(self):
        return f"{self.car_make} {self.name} ({self.year}): {self.type}"
