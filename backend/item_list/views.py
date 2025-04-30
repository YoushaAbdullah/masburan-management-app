from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import ItemList
from .serializers import ItemListSerializer

# Create View
class ItemListCreateView(generics.CreateAPIView):
    queryset = ItemList.objects.all()
    serializer_class = ItemListSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)

# Update View
class ItemListUpdateView(generics.UpdateAPIView):
    queryset = ItemList.objects.all()
    serializer_class = ItemListSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)

# Delete View
class ItemListDeleteView(generics.DestroyAPIView):
    queryset = ItemList.objects.all()
    serializer_class = ItemListSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        instance.delete()
