from django.urls import path
from .views import DeliveryOrderCreateView, DeliveryOrderUpdateView, DeliveryOrderDeleteView

urlpatterns = [
    path('create/', DeliveryOrderCreateView.as_view(), name='deliveryorder-create'),
    path('<int:pk>/update/', DeliveryOrderUpdateView.as_view(), name='deliveryorder-update'),
    path('<int:pk>/delete/', DeliveryOrderDeleteView.as_view(), name='deliveryorder-delete'),
]
