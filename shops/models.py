from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    """User types"""
    SHOP_OWNER = 'shop_owner'
    SHOP_USER = 'shop_user'
    SHOP_ADMIN = 'admin'

    USER_TYPE_CHOICES = (
        {1, SHOP_USER},
        {2, SHOP_OWNER},
        {3, SHOP_ADMIN},
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)


class Shop(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
