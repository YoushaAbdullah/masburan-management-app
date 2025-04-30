from django.urls import path
from .views import (
    DeliveryOrderDetailsCreateView, 
    DeliveryOrderDetailsUpdateView, 
    DeliveryOrderDetailsDeleteView
)

urlpatterns = [
    path('delivery-order-details/create/', DeliveryOrderDetailsCreateView.as_view(), name='deliveryorderdetails-create'),
    path('delivery-order-details/<int:pk>/update/', DeliveryOrderDetailsUpdateView.as_view(), name='deliveryorderdetails-update'),
    path('delivery-order-details/<int:pk>/delete/', DeliveryOrderDetailsDeleteView.as_view(), name='deliveryorderdetails-delete'),
]
