# from .views import *
from django.urls import path
from . import views


urlpatterns = [
    path('main/', views.MainView),
    path('menu-items/', views.ItemView.as_view()),
]