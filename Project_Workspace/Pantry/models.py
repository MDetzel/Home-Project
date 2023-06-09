from django.db import models

# Create your models here.
class Category(models.Model):
    slug = models.SlugField()
    Title = models.CharField(max_length=255, db_index=True)
    class Meta: 
        ordering = ['Title']
    def __str__(self):
        return self.Title
    
class Item(models.Model):
    Title = models.CharField(max_length=255)
    Inventory = models.IntegerField()
    Category = models.ForeignKey(Category, on_delete=models.PROTECT)
    
    class Meta:
        ordering = ['Category', 'Title']
        
    def update_inventory(self, new_inventory):
        self.Inventory = new_inventory
        self.save()
    
    def __str__(self):
        return str(self.Title)
    