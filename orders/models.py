from django.db import models
from catalog.models import Product

class Inquiry(models.Model):


    class Status(models.TextChoices):
        NEW = 'N', 'New'
        IN_PROGRESS = 'IP', 'In Progress'
        Quoted = 'Q', 'Quoted'
        Completed = 'C', 'Completed'

    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField(max_length=100)
    customer_phone = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.TextField()
    desired_quantity = models.PositiveIntegerField()
    status = models.TextField(choices=Status.choices, default=Status.NEW)
    created_at = models.DateTimeField(auto_now_add=True)