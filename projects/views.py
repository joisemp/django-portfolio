from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import render
from .models import Project
from django.core.mail import send_mail

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

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        #send an email
        send_mail(
            subject,
            'Name : '+ name + ' | ' +'Email : ' + email + ' | ' +'Message : ' + message,
            email,
            ['joise1124@gmail.com']
        )
        return render(request, 'projects/contact.html', {'name':name})
    else:
        return render(request, 'projects/contact.html', {})