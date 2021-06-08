from django.urls import reverse
from django.db import models
from django.db.models.fields import NullBooleanField
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.contrib.auth.models import AbstractUser
from colorfield.fields import ColorField

class UserProfile(AbstractUser):
    pass

class Categorie(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

choices = Categorie.objects.all().values_list('name', 'name')
choice_list = []
for item in choices:
    choice_list.append(item)

class Project(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=255, default='Figma', choices=choice_list)
    post_date = models.DateField(auto_now_add=True)
    post_time = models.TimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/projects')
    file = models.FileField(null=True, blank=True, upload_to='files/projects')
    case_study_file = models.FileField(null=True, blank=True, upload_to='files/projects/case_studies')
    color_palette = models.BooleanField(default=False)
    color = ColorField(null=True, blank=True)
    color1 = ColorField(null=True, blank=True)
    color2 = ColorField(null=True, blank=True)
    color3 = ColorField(null=True, blank=True)

    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse('project:project-home')

@receiver(pre_delete, sender=Project)
def Project_delete(sender, instance, **kwargs):
    instance.image.delete(False)

@receiver(pre_delete, sender=Project)
def Project_delete(sender, instance, **kwargs):
    instance.file.delete(False)

@receiver(pre_delete, sender=Project)
def Project_delete(sender, instance, **kwargs):
    instance.case_study_file.delete(False)