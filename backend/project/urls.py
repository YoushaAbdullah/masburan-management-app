from django.urls import path
from .views import ProjectCreateView, ProjectUpdateView, ProjectDeleteView

urlpatterns = [
    path('create/', ProjectCreateView.as_view(), name='project-create'),
    path('<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
]
