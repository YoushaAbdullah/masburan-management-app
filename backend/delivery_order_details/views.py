from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import DeliveryOrderDetails
from .serializers import DeliveryOrderDetailsSerializer

# Create
class DeliveryOrderDetailsCreateView(generics.ListCreateAPIView):
    queryset = DeliveryOrderDetails.objects.all()
    serializer_class = DeliveryOrderDetailsSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return DeliveryOrderDetails.objects.all()

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)

# Update
class DeliveryOrderDetailsUpdateView(generics.UpdateAPIView):
    queryset = DeliveryOrderDetails.objects.all()
    serializer_class = DeliveryOrderDetailsSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)

# Delete
class DeliveryOrderDetailsDeleteView(generics.DestroyAPIView):
    queryset = DeliveryOrderDetails.objects.all()
    serializer_class = DeliveryOrderDetailsSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        instance.delete()
