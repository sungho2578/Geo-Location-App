from django.urls import path
from GeoLocationApp import views

urlpatterns = [
    path("", views.home, name="home"),
]