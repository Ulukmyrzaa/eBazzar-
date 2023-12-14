from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models


class Basket(models.Model):
    # Модель корзины покупок
    name = models.CharField(max_length=255)
    # Другие поля корзины


class CustomUser(AbstractUser):
    # Дополнительные поля для регистрации
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    surname = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(unique=True)
    credit_card = models.CharField(max_length=16, blank=True, null=True)
    role = models.CharField(max_length=30, blank=True, null=True)
    photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, null=True, blank=True)
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)
    # Дополнительные поля для модели пользователя
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username
