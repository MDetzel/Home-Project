from django.shortcuts import render, HttpResponse
from rest_framework import generics, response
from .models import *
from Pantry.serializers import *
from rest_framework.response import Response

# Create your views here.
def MainView(request):
    return render(request, 'index.html')

def PantryView(request):
    pantry_data = Item.objects.all().select_related('Category')
    main_data = {"pantry": pantry_data}
    return render(request, 'pantry.html', main_data)
    # return render(request, 'pantry.html', {"pantry": main_data})

class ItemView(generics.ListCreateAPIView):
    queryset = Item.objects.all().select_related('Category')
    serializer_class = ItemSerializer