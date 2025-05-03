from django.urls import path
from .views import (
    InventoryCreateView,
    InventoryUpdateView,
    InventoryDeleteView
)

urlpatterns = [
    path('create/', InventoryCreateView.as_view(), name='inventory-create'),
    path('<int:pk>/update/', InventoryUpdateView.as_view(), name='inventory-update'),
    path('<int:pk>/delete/', InventoryDeleteView.as_view(), name='inventory-delete'),
]
