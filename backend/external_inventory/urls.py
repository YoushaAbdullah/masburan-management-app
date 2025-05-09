from django.urls import path
from .views import (
    ExternalInventoryCreateView, 
    ExternalInventoryUpdateView, 
    ExternalInventoryDeleteView
)

urlpatterns = [
    path('create/', ExternalInventoryCreateView.as_view(), name='externalinventory-create'),
    path('<int:pk>/update/', ExternalInventoryUpdateView.as_view(), name='externalinventory-update'),
    path('<int:pk>/delete/', ExternalInventoryDeleteView.as_view(), name='externalinventory-delete'),
]
