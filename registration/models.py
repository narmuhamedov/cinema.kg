from django.db import models
from django.contrib.auth.models import User

class CustomUser(User):
    GENDER = (
        ('М', 'Мужчина'),
        ('Ж', 'Женщина')
    )
    phone_number = models.CharField(max_length=13, default='+996', verbose_name='Введите номер телефона')
    gender = models.CharField(max_length=10, choices=GENDER, verbose_name='Ваш пол')
    date_birth = models.DateField(verbose_name='Укажите дату рождения')

    def __str__(self):
        return self.phone_number
