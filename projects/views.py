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

def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response=HttpResponse(fh.read(), content_type="application/image")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response
    raise Http404
