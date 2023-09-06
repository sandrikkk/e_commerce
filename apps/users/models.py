from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.base.models import BaseModelClass
from enumchoicefield import ChoiceEnum, EnumChoiceField


class Role(ChoiceEnum):
    CUSTOMER = 'Customer'
    ADMIN = "Admin"


class User(AbstractUser, BaseModelClass):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)
    username = models.CharField(max_length=255, unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    role = EnumChoiceField(Role, default=Role.CUSTOMER)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
