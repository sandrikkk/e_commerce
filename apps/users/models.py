from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.base.models import BaseModelClass


class User(AbstractUser, BaseModelClass):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)
    username = models.CharField(max_length=255, unique=True)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
