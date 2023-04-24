from django.forms import ModelForm
from .models import *
from django import forms

class ItemForm(ModelForm):
    class Meta:
        model = Item
        # fields = ['Inventory', 'Category', 'Title']
        exclude = ['Category', 'Title']
        widgets = {
            'Inventory': forms.TextInput(attrs={'class': 'form-control'}),
        }