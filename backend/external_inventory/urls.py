from django.urls import path
from .views import (
    BesterInventoryCreateView, 
    BesterInventoryUpdateView, 
    BesterInventoryDeleteView
)

urlpatterns = [
    path('bester-inventory/create/', BesterInventoryCreateView.as_view(), name='besterinventory-create'),
    path('bester-inventory/<int:pk>/update/', BesterInventoryUpdateView.as_view(), name='besterinventory-update'),
    path('bester-inventory/<int:pk>/delete/', BesterInventoryDeleteView.as_view(), name='besterinventory-delete'),
]
