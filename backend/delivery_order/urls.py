from django.urls import path
from .views import DeliveryOrderCreateView, DeliveryOrderUpdateView, DeliveryOrderDeleteView

urlpatterns = [
    path('delivery-orders/create/', DeliveryOrderCreateView.as_view(), name='deliveryorder-create'),
    path('delivery-orders/<int:pk>/update/', DeliveryOrderUpdateView.as_view(), name='deliveryorder-update'),
    path('delivery-orders/<int:pk>/delete/', DeliveryOrderDeleteView.as_view(), name='deliveryorder-delete'),
]
