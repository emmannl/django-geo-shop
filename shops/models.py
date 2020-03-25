from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models as geoModels
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

    def __str__(self):
        return self.username

    def is_shop_owner(self):
        return self.user_type == 2



class Shop(models.Model):
    name = models.CharField(max_length=100)
    location = geoModels.PointField(srid=32140)
    street_address = models.CharField(max_length=255, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
