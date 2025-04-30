from django.urls import path
from .views import (
    InvoiceDetailsCreateView,
    InvoiceDetailsUpdateView,
    InvoiceDetailsDeleteView,
)

urlpatterns = [
    path('invoice-details/create/', InvoiceDetailsCreateView.as_view(), name='invoice-details-create'),
    path('invoice-details/<int:pk>/update/', InvoiceDetailsUpdateView.as_view(), name='invoice-details-update'),
    path('invoice-details/<int:pk>/delete/', InvoiceDetailsDeleteView.as_view(), name='invoice-details-delete'),
]
