from django.db import models

# Create your models here.
class Category(models.Model):
    slug = models.SlugField()
    Title = models.CharField(max_length=255)