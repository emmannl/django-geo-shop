from django.urls import path
from . import views

app_name = 'register'

urlpatterns = [
    path('', views.ChooseUserTypeView.as_view(), name='choose-type'),
    path('register/user', views.RegisterAsUser.as_view(), name='as-user'),
    path('register/shop-owner', views.RegisterAsShopOwner.as_view(), name='as-shop-owner')
]
