from django.shortcuts import render, HttpResponse
from rest_framework import generics, response
from .models import *
from Pantry.serializers import *
from rest_framework.response import Response
from .forms import *

# Create your views here.
def MainView(request):
    return render(request, 'index.html')

def PantryView(request):
    category_data = Category.objects.all()
    form = ItemForm()
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
    main_data = {"category": category_data, "form":form}
    return render(request, 'pantry.html', main_data)    

class ItemView(generics.ListCreateAPIView):
    queryset = Item.objects.all().select_related('Category')
    serializer_class = ItemSerializer