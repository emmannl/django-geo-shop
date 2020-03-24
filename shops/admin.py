from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from shops.models import Shop

# Register your models here.


@admin.register(Shop)
class ShopAdmin(OSMGeoAdmin):
    pass
    list_display = ('name', 'street_address', 'owner')
