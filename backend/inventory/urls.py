from django.urls import path
from .views import (
    InventoryCreateView,
    InventoryUpdateView,
    InventoryDeleteView
)

urlpatterns = [
    path('inventory/create/', InventoryCreateView.as_view(), name='inventory-create'),
    path('inventory/<int:pk>/update/', InventoryUpdateView.as_view(), name='inventory-update'),
    path('inventory/<int:pk>/delete/', InventoryDeleteView.as_view(), name='inventory-delete'),
]
