from django.shortcuts import render, HttpResponse
from rest_framework import generics
from .models import *
from Pantry.serializers import *

# Create your views here.
def MainView(request):
    return HttpResponse("Congratulations! You did it!")

class ItemView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer