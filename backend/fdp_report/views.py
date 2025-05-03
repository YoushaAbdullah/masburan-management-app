# from django.shortcuts import render

# # Create your views here.
# from rest_framework import generics, permissions
# from .models import FdpReport
# from .serializers import FdpReportSerializer

# # CREATE
# class FdpReportCreateView(generics.CreateAPIView):
#     queryset = FdpReport.objects.all()
#     serializer_class = FdpReportSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save()

# # UPDATE
# class FdpReportUpdateView(generics.UpdateAPIView):
#     queryset = FdpReport.objects.all()
#     serializer_class = FdpReportSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     lookup_field = 'pk'  # Uses ID in URL for update

# # DELETE
# class FdpReportDeleteView(generics.DestroyAPIView):
#     queryset = FdpReport.objects.all()
#     serializer_class = FdpReportSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     lookup_field = 'pk'  # Uses ID in URL for delete
