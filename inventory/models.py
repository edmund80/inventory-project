from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Inventory(models.Model):
    itemName = models.CharField(max_length=50)
    itemLocation = models.CharField(max_length=50)
    itemQuantity = models.IntegerField()
    dateAdded = models.DateField()

    def __str__(self) -> str:
        return f'{self.itemName}, {self.itemLocation}'
    
    def get_absolute_url(self):
        return reverse('inventory-detail', args=[str(id)])