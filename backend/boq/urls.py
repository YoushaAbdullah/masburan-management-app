from django.urls import path
from .views import BoqCreateView, BoqUpdateView, BoqDeleteView

urlpatterns = [
    path('boqs/create/', BoqCreateView.as_view(), name='boq-create'),
    path('boqs/<int:pk>/update/', BoqUpdateView.as_view(), name='boq-update'),
    path('boqs/<int:pk>/delete/', BoqDeleteView.as_view(), name='boq-delete'),
]

