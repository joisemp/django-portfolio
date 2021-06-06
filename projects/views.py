from django.views.generic import ListView, DetailView, TemplateView
from .models import Project

class ProjectHomeView(ListView):
    template_name = 'projects/index.html'
    queryset = Project.objects.all()
    context_object_name = 'projects'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project-detail.html'
    context_object_name = 'project'

class AboutView(TemplateView):
    template_name = 'projects/about.html'