from django.conf import settings
from django.http import HttpResponse
from django.http.response import Http404
from django.shortcuts import render
from django.views.generic import ListView
from .models import Project
import os

class ProjectHomeView(ListView):
    template_name = 'projects/index.html'
    queryset = Project.objects.all()
    context_object_name = 'projects'