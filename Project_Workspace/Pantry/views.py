from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from rest_framework import generics, response
from .models import Item
from Pantry.serializers import *
from rest_framework.response import Response
from .forms import ItemForm

# Create your views here.
def MainView(request):
    return render(request, 'index.html')

# def PantryView(request):
#     category_data = Category.objects.all()
#     # form = ItemForm()
#     # if request.method == "POST":
#     #     form = ItemForm(request.POST)
#     #     if form.is_valid():
#     #         form.save()
#     main_data = {"category": category_data}
#     return render(request, 'pantry.html', main_data)  

def PantryView(request):
    category_data = Category.objects.all()
    main_data = {"category": category_data}
    return render(request, 'pantry.html', main_data) 

# def update_inventory(request):
#     # item = Item.objects.all()
#     if request.method == "POST":
#         form = ItemForm(request.POST)
#         if form.is_valid():
#             # Item.update_inventory(form.cleaned_data)
#             form.save()
#             return render(request, 'edit_pantry.html')
#         else:
#             return HttpResponse("You have encountered an error. The form data must not be valid")
#     # else:
#     #     form = ItemForm()
#     # context={'pantry': item, 'form':form}
    
#     # return render(request, 'pantry', context)  

# def update_inventory(request, pk):
#    item = get_object_or_404(Item,pk=pk)
#    if request.method == 'POST':
#        form = ItemForm(request.POST, instance = item) 
#        if form.is_valid():
#            form.save()
#            return redirect('pantry')
#    else:
#        form = ItemForm(instance = item)
#        return render (request, 'edit_pantry.html', {'form':form})

def update_inventory(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('pantry')
    else:
        form = ItemForm(instance=item)

    return render(request, 'edit_pantry.html', {'form': form})

class ItemView(generics.ListCreateAPIView):
    queryset = Item.objects.all().select_related('Category')
    serializer_class = ItemSerializer