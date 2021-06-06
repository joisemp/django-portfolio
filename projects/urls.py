from django.urls import path
from .views import ProjectDetailView, ProjectHomeView

app_name = 'projects'

urlpatterns = [
    path('', ProjectHomeView.as_view(), name='project-home'),
    path('project<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
]