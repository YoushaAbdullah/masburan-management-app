from django.urls import path
from .views import (
    InvoiceDetailsCreateView,
    InvoiceDetailsUpdateView,
    InvoiceDetailsDeleteView,
)

urlpatterns = [
    path('create/', InvoiceDetailsCreateView.as_view(), name='invoice-details-create'),
    path('<int:pk>/update/', InvoiceDetailsUpdateView.as_view(), name='invoice-details-update'),
    path('<int:pk>/delete/', InvoiceDetailsDeleteView.as_view(), name='invoice-details-delete'),
]
