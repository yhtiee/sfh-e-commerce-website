from django.urls import path
from . import views

urlpatterns = [
    path("base/", views.basepage, name="base"),
    path("home/", views.homepage, name="home"),

]