from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url
from django.urls import path, include
from projects.views import AboutView
from projects.views import contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls', namespace='projects')),
    path('contact/', contact, name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    url(r'download/(?P<path>.*)$', serve, {'download_root':settings.MEDIA_ROOT})
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
