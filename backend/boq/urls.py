from django.urls import path
from .views import BoqCreate, BoqUpdate, BoqDelete, BoqList

urlpatterns = [
    path("", BoqList.as_view(), name="boq_list"),
    path('create/', BoqCreate.as_view(), name='boq-create'),
    path('<int:pk>/update/', BoqUpdate.as_view(), name='boq-update'),
    path('<int:pk>/delete/', BoqDelete.as_view(), name='boq-delete'),
]

