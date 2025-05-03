from django.urls import path
from .views import (
    ItemListCreateView,
    ItemListUpdateView,
    ItemListDeleteView,
)

urlpatterns = [
    path('create/', ItemListCreateView.as_view(), name='itemlist-create'),
    path('<int:pk>/update/', ItemListUpdateView.as_view(), name='itemlist-update'),
    path('<int:pk>/delete/', ItemListDeleteView.as_view(), name='itemlist-delete'),
]
