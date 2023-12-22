from django.urls import path
from inventory import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inventories', views.InventoryListView.as_view(), name='inventories'),
]