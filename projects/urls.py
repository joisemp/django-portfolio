from django.urls import path
from .views import ProjectHomeView

app_name = 'projects'

urlpatterns = [
    path('', ProjectHomeView.as_view(), name='project-home')
    ]