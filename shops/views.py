from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.gis.measure import D
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.gis.geos import fromstr, Point, GEOSGeometry
from django.contrib.gis.db.models.functions import Distance
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from .models import Shop


# Create your views here.

def home(request: HttpRequest):
    return render(request, 'shops/welcome.html')


longitude, latitude = 7.9709675, 5.0280591

user_location = GEOSGeometry(f'POINT({longitude} {latitude})', srid=4326)
# user_location = Point(longitude, latitude, srid=4326)


@method_decorator([login_required, user_passes_test(lambda u: u.user_type == 1)], name='dispatch')
class ShopsCloseToUser(ListView):
    model = Shop
    context_object_name = 'shops'
    queryset = Shop.objects.filter(location__distance_lte=(user_location, D(m=1)))
    template_name = 'shops/user_shops.html'
