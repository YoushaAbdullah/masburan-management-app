from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Boq
from .serializers import BoqSerializer

# Create your views here.
# Create a new Boq
class BoqCreateView(generics.CreateAPIView):
    queryset = Boq.objects.all()
    serializer_class = BoqSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)

# Update an existing Boq
class BoqUpdateView(generics.UpdateAPIView):
    queryset = Boq.objects.all()
    serializer_class = BoqSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)

# Delete a Boq
class BoqDeleteView(generics.DestroyAPIView):
    queryset = Boq.objects.all()
    serializer_class = BoqSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        instance.delete()
