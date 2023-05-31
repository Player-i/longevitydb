from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", views.home),
    path("sleep/", views.sleep),
    path("supplements/", views.supplements),
    path("diet/", views.diet),
    path("<slug:slug>/", views.see_study),
]
