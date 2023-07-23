from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.CharField(max_length=30, verbose_name='Phone', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='Country', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

