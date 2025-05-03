from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Boq
from .serializers import BoqSerializer
from django.contrib.auth.models import User

# Create your views here.
# Create a new Boq
class BoqCreate(generics.ListCreateAPIView):
    queryset = Boq.objects.all()
    serializer_class = BoqSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return Boq.objects.all()

    def perform_create(self, serializer):
        project = self.request.query_params.get('project')

        if serializer.is_valid():
            serializer.save(project=project)
            
        else:
            print(serializer.errors)

# Update an existing Boq
class BoqUpdate(generics.UpdateAPIView):
    queryset = Boq.objects.all()
    serializer_class = BoqSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)

# Delete a Boq
class BoqDelete(generics.DestroyAPIView):
    queryset = Boq.objects.all()
    serializer_class = BoqSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        instance.delete()

class BoqList(APIView):
    queryset = Boq.objects.all()
    serializer_class = BoqSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        boqs = Boq.objects.all()
        serializer = BoqSerializer(boqs, many=True)
        return Response(serializer.data)
