from django.contrib import admin
from .models import Categorie, Project, UserProfile

admin.site.register(Project)
admin.site.register(UserProfile)
admin.site.register(Categorie)