# from .views import *
from django.urls import path
from . import views


urlpatterns = [
    path('main/', views.MainView, name='home'),
    path('pantry/', views.PantryView, name='pantry'),
    path('menu-items/', views.ItemView.as_view()),
]