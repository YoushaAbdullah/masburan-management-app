from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import ExternalInventory
from .serializers import ExternalInventorySerializer

# Create
class ExternalInventoryCreateView(generics.ListCreateAPIView):
    queryset = ExternalInventory.objects.all()
    serializer_class = ExternalInventorySerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return ExternalInventory.objects.all()

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)

# Update
class ExternalInventoryUpdateView(generics.UpdateAPIView):
    queryset = ExternalInventory.objects.all()
    serializer_class = ExternalInventorySerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)

# Delete
class ExternalInventoryDeleteView(generics.DestroyAPIView):
    queryset = ExternalInventory.objects.all()
    serializer_class = ExternalInventorySerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        instance.delete()
