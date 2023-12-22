from django.shortcuts import render
from django.views import generic
from .models import Inventory

# Create your views here.
def index(request):
    return render(request, 'inventory/index.html')

class InventoryListView(generic.ListView):
      model = Inventory
