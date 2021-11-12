
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic.base import TemplateView
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('ipapi.urls')),
    url(r'^.*', TemplateView.as_view(template_name="home.html"), name="home")
]
