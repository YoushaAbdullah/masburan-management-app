from django.urls import path
from .views import (
    DeliveryOrderDetailsCreateView, 
    DeliveryOrderDetailsUpdateView, 
    DeliveryOrderDetailsDeleteView
)

urlpatterns = [
    path('create/', DeliveryOrderDetailsCreateView.as_view(), name='deliveryorderdetails-create'),
    path('<int:pk>/update/', DeliveryOrderDetailsUpdateView.as_view(), name='deliveryorderdetails-update'),
    path('<int:pk>/delete/', DeliveryOrderDetailsDeleteView.as_view(), name='deliveryorderdetails-delete'),
]
