from django.urls import path
from .views import (
    InvoiceCreateView,
    InvoiceUpdateView,
    InvoiceDeleteView,
)

urlpatterns = [
    path('create/', InvoiceCreateView.as_view(), name='invoice-create'),
    path('<int:pk>/update/', InvoiceUpdateView.as_view(), name='invoice-update'),
    path('<int:pk>/delete/', InvoiceDeleteView.as_view(), name='invoice-delete'),
]
