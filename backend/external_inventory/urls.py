from django.urls import path
from .views import (
    BesterInventoryCreateView, 
    BesterInventoryUpdateView, 
    BesterInventoryDeleteView
)

urlpatterns = [
    path('create/', BesterInventoryCreateView.as_view(), name='besterinventory-create'),
    path('<int:pk>/update/', BesterInventoryUpdateView.as_view(), name='besterinventory-update'),
    path('<int:pk>/delete/', BesterInventoryDeleteView.as_view(), name='besterinventory-delete'),
]
