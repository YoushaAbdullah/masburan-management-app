from django.urls import path
from .views import (
    InvoiceCreateView,
    InvoiceUpdateView,
    InvoiceDeleteView,
)

urlpatterns = [
    path('invoice/create/', InvoiceCreateView.as_view(), name='invoice-create'),
    path('invoice/<int:pk>/update/', InvoiceUpdateView.as_view(), name='invoice-update'),
    path('invoice/<int:pk>/delete/', InvoiceDeleteView.as_view(), name='invoice-delete'),
]
