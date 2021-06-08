from django.urls import path
from .views import AboutView, ProjectDetailView, ProjectHomeView, CategoryView

app_name = 'projects'

urlpatterns = [
    path('', ProjectHomeView.as_view(), name='project-home'),
    path('project<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('category/<str:category_name>/', CategoryView, name='category-page'),
]