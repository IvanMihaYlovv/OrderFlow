from django.core.validators import MinValueValidator
from django.db import models


class Category(models.Model):
     id = models.AutoField(primary_key=True)
     name = models.CharField(max_length=100)
     description = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
         return self.name



class Material(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Product(models.Model):


    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    materials = models.ManyToManyField(Material, related_name='products')
    image = models.ImageField(upload_to='products')
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

