from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("logout/", views.logout, name="logout"),
    path("customer/<int:key>", views.customer, name="customer"),
    path("delete/<int:key>", views.delete, name="delete"),
    path("update/<int:key>", views.update, name="update"),
    path("create/", views.create, name="create")
]