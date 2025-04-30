from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import BesterInventory
from .serializers import BesterInventorySerializer

# Create
class BesterInventoryCreateView(generics.CreateAPIView):
    queryset = BesterInventory.objects.all()
    serializer_class = BesterInventorySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)

# Update
class BesterInventoryUpdateView(generics.UpdateAPIView):
    queryset = BesterInventory.objects.all()
    serializer_class = BesterInventorySerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)

# Delete
class BesterInventoryDeleteView(generics.DestroyAPIView):
    queryset = BesterInventory.objects.all()
    serializer_class = BesterInventorySerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        instance.delete()
