from django.urls import path
from .views import ProjectCreateView, ProjectUpdateView, ProjectDeleteView

urlpatterns = [
    path('projects/create/', ProjectCreateView.as_view(), name='project-create'),
    path('projects/<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
]
