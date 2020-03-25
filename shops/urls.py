from django.urls import path, include
from . import views

app_name = 'shops'
urlpatterns = [
    path('', views.home, name='welcome'),
    path('close-by', views.ShopsCloseToUser.as_view(), name='close-by'),
    path('management/', include([
        path('create', views.ShopCreate.as_view()),
    ])),
]
