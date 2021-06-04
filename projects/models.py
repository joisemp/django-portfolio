from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

class Project(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    post_time = models.TimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/projects')
    file = models.FileField(null=True, blank=True, upload_to='files/projects')
    case_study_file = models.FileField(null=True, blank=True, upload_to='files/projects/case_studies')

    def __str__(self):
        return str(self.title)

@receiver(pre_delete, sender=Project)
def Project_delete(sender, instance, **kwargs):
    instance.image.delete(False)

@receiver(pre_delete, sender=Project)
def Project_delete(sender, instance, **kwargs):
    instance.file.delete(False)

@receiver(pre_delete, sender=Project)
def Project_delete(sender, instance, **kwargs):
    instance.case_study_file.delete(False)