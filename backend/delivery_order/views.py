from django.shortcuts import render
# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import DeliveryOrder
from .serializers import DeliveryOrderSerializer

# Create a new DeliveryOrder
class DeliveryOrderCreateView(generics.CreateAPIView):
    queryset = DeliveryOrder.objects.all()
    serializer_class = DeliveryOrderSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return DeliveryOrder.objects.all()

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)

# Update an existing DeliveryOrder
class DeliveryOrderUpdateView(generics.UpdateAPIView):
    queryset = DeliveryOrder.objects.all()
    serializer_class = DeliveryOrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)

# Delete a DeliveryOrder
class DeliveryOrderDeleteView(generics.DestroyAPIView):
    queryset = DeliveryOrder.objects.all()
    serializer_class = DeliveryOrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        instance.delete()
