from django.urls import path
from .views import (
    ItemListCreateView,
    ItemListUpdateView,
    ItemListDeleteView,
)

urlpatterns = [
    path('itemlist/create/', ItemListCreateView.as_view(), name='itemlist-create'),
    path('itemlist/<int:pk>/update/', ItemListUpdateView.as_view(), name='itemlist-update'),
    path('itemlist/<int:pk>/delete/', ItemListDeleteView.as_view(), name='itemlist-delete'),
]
