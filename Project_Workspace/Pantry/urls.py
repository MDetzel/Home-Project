# from .views import *
from django.urls import path
from Pantry import views


urlpatterns = [
    path('main/', views.MainView),
]