from django.contrib.auth.models import AbstractUser
from django.db import models


class UserEmployee(AbstractUser):
    """Сотрудники"""

    class Positions(models.TextChoices):
        DIRECTOR = 'Director'
        COOK = 'Cook'
        DELIVERER = 'Deliverer'
        ADMIN = 'Admin'

    phone = models.CharField(max_length=35, verbose_name='Телефон', null=True, blank=True)
    position = models.CharField(max_length=30, verbose_name='Должность', null=True, blank=True,
                                choices=Positions.choices, default=Positions.COOK)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ('last_name',)
