from django.db import models

# Create your models here.
class Category(models.Model):
    slug = models.SlugField()
    Title = models.CharField(max_length=255, db_index=True)
    def __str__(self):
        return self.Title
    
class Item(models.Model):
    Title = models.CharField(max_length=255)
    Inventory = models.IntegerField()
    Category = models.ForeignKey(Category, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.Title)
    