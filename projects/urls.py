from django.urls import path
from .views import AboutView, ProjectDetailView, ProjectHomeView

app_name = 'projects'

urlpatterns = [
    path('', ProjectHomeView.as_view(), name='project-home'),
    path('project<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('about/', AboutView.as_view(), name='about'),
]