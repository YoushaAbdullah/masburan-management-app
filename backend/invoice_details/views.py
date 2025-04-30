from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import InvoiceDetails
from .serializers import InvoiceDetailsSerializer

# Create View
class InvoiceDetailsCreateView(generics.CreateAPIView):
    queryset = InvoiceDetails.objects.all()
    serializer_class = InvoiceDetailsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)

# Update View
class InvoiceDetailsUpdateView(generics.UpdateAPIView):
    queryset = InvoiceDetails.objects.all()
    serializer_class = InvoiceDetailsSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)

# Delete View
class InvoiceDetailsDeleteView(generics.DestroyAPIView):
    queryset = InvoiceDetails.objects.all()
    serializer_class = InvoiceDetailsSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        instance.delete()
