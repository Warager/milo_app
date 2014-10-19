from random import randint
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    birthday = models.DateField(null=True, blank=True)
    random = models.IntegerField(auto_created=True, default=randint(0, 100))

    REQUIRED_FIELDS = ['birthday', 'random']

