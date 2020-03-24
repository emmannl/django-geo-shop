from django.urls import path, include
from . import views

app_name = 'shops'
urlpatterns = [
    path('', views.home, name='welcome'),
    path('home', views.home),
]
