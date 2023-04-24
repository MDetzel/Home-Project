# from .views import *
from django.urls import path
from . import views


urlpatterns = [
    path('main/', views.MainView, name='home'),
    path('pantry/', views.PantryView, name='pantry'),
    path('menu-items/', views.ItemView.as_view()),
    path('pantry/edit/<int:pk>', views.update_inventory, name='edit_pantry')
]