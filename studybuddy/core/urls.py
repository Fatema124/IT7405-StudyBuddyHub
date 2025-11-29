
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("join-group/", views.join_group, name="join_group"),
]
