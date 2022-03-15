from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from .utils import *


# Create your models here.
# class User(models.Model):
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=50)
#     email = models.EmailField(max_length=200)
#
#     def __str__(self):
#         return self.username


class UserDetail(models.Model):
    zipcode = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    phone = models.CharField(max_length=200, validators=[MinLengthValidator(10)])
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.username


class Coffee(models.Model):
    name = models.CharField(max_length=10, choices=COFFEE_CHOICES)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    quantity = models.CharField(max_length=10, choices=QUANTITY_CHOCCES)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name
