from rest_framework import serializers
from .models import *

class ItemSerializer(serializers.ModelSerializer):
    # category = serializers.StringRelatedField()
    Category = serializers.CharField(source = "Category.Title")
    class Meta:
        model = Item
        fields = ['id','Title', 'Inventory', 'Category']